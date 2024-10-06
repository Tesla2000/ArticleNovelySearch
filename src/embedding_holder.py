from __future__ import annotations

import sys
import threading
from hashlib import md5
from itertools import batched
from typing import Any
from typing import Generator
from typing import Iterable
from typing import Optional

import numpy as np
from more_itertools import unzip
from pgvector.sqlalchemy import Vector
from phi.document import Document
from phi.utils.log import logger
from phi.vectordb.pgvector.pgvector2 import PgVector2
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import Column
from sqlalchemy.schema import Table
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.expression import text
from sqlalchemy.types import DateTime
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from tqdm import tqdm

from src.embedders.embedder import Embedder


class EmbeddingHolder(PgVector2):
    def get_embeddings(
        self,
        limit: int = sys.maxsize,
        embedder: Optional[Embedder] = None,
    ) -> tuple[np.ndarray, list[dict[str, str]]]:
        """
        Fetches embeddings and associated metadata from the database,
        optionally using a specified embedder to generate embeddings from
        content.
        :param embedder: An optional embedder used to generate embeddings from
        content if provided.
        :param limit: The maximum number of records to retrieve from the
        database.
        :return: A tuple of embeddings and metadata
        """
        with self.Session() as sess:
            with sess.begin():
                stmt = (
                    select(
                        (
                            self.table.c.embedding
                            if embedder is None
                            else self.table.c.content
                        ),
                        self.table.c.meta_data,
                    )
                    .select_from(self.table)
                    .order_by(self.table.c.id)
                    .limit(limit)
                )
                if embedder is None:
                    embeddings, metadata = unzip(sess.execute(stmt).fetchall())
                else:
                    content, metadata = unzip(sess.execute(stmt).fetchall())
                    embeddings = embedder.get_embeddings(tuple(content))
                return np.array(tuple(embeddings)), list(metadata)

    def insert(
        self,
        documents: Iterable[Document],
        batch_size: int = 10,
    ) -> None:
        """
        Inserts a batch of documents into the database using multithreading for
        efficiency.
        :param documents: An iterable collection of Document objects to be
        inserted.
        :param batch_size: The number of documents to process in each batch.
        :return: None
        """
        documents = self.filter_documents(documents)
        with self.Session() as sess:
            for batch in tqdm(
                batched(documents, batch_size), "Searching articles..."
            ):
                threads = tuple(
                    threading.Thread(
                        target=self._insert, args=(document, sess)
                    )
                    for document in batch
                )
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()

                sess.commit()
        logger.info("Done searching")

    def _insert(self, document: Document, sess):
        """
        Inserts a document into the database after embedding and cleaning its
        content.
        :param sess: A session object used to execute database operations.
        :param document: The Document object containing data to be inserted.
        :return: None
        """
        document.embed(embedder=self.embedder)
        cleaned_content = document.content.replace("\x00", "\ufffd")
        content_hash = md5(cleaned_content.encode()).hexdigest()
        stmt = postgresql.insert(self.table).values(
            name=document.name,
            meta_data=document.meta_data,
            content=cleaned_content,
            embedding=document.embedding,
            usage=document.usage,
            content_hash=content_hash,
        )
        sess.execute(stmt)

    def filter_documents(
        self, documents: Iterable[Document]
    ) -> Generator[Document, Any, None]:
        """
        Filters out documents that already exist in the database based on their
        metadata ID.
        :param documents: An iterable collection of Document objects to be
        filtered.
        :return: A generator of filtered documents.
        """
        with self.Session() as sess:
            with sess.begin():
                stmt = select(self.table.c.meta_data)
                result = sess.execute(stmt).all()
                database_meta_data = {row[0]["id"] for row in result}

        return (
            doc
            for doc in documents
            if doc.meta_data["id"] not in database_meta_data
        )

    def get_table(self) -> Table:
        """
        Creates and returns a SQLAlchemy Table object representing the
        structure of the database table for storing embeddings and related
        metadata.
        :return: SQLAlchemy Table object
        """
        return Table(
            self.collection,
            self.metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("name", String),
            Column(
                "meta_data",
                postgresql.JSONB,
                server_default=text("'{}'::jsonb"),
            ),
            Column("content", postgresql.TEXT),
            Column("embedding", Vector(self.dimensions)),
            Column("usage", postgresql.JSONB),
            Column(
                "created_at",
                DateTime(timezone=True),
                server_default=text("now()"),
            ),
            Column(
                "updated_at", DateTime(timezone=True), onupdate=text("now()")
            ),
            Column("content_hash", String),
            extend_existing=True,
        )
