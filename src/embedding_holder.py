from __future__ import annotations

import threading
from hashlib import md5
from itertools import batched
from typing import Any
from typing import Generator
from typing import Iterable

import numpy as np
from more_itertools import unzip
from phi.document import Document
from phi.utils.log import logger
from phi.vectordb.pgvector.pgvector2 import PgVector2
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.expression import select
from tqdm import tqdm


class EmbeddingHolder(PgVector2):
    def get_embeddings(self) -> tuple[list[str], list[str], np.ndarray]:
        with self.Session() as sess:
            with sess.begin():
                stmt = select(
                    self.table.c.id, self.table.c.name, self.table.c.embedding
                ).select_from(self.table)
                ids, names, embeddings = unzip(sess.execute(stmt).fetchall())
                return list(ids), list(names), np.array(tuple(embeddings))

    def insert(
        self, documents: Iterable[Document], batch_size: int = 10
    ) -> None:
        try:
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
        except Exception as e:
            logger.info(f"Unexpected error occurred {e}")
        finally:
            logger.info("Done searching")

    def _insert(self, document: Document, sess):
        document.embed(embedder=self.embedder)
        cleaned_content = document.content.replace("\x00", "\ufffd")
        content_hash = md5(cleaned_content.encode()).hexdigest()
        _id = document.id or content_hash
        stmt = postgresql.insert(self.table).values(
            id=_id,
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
        with self.Session() as sess:
            with sess.begin():
                stmt = select(self.table.c.id)
                result = sess.execute(stmt).all()
                database_ids = {row[0] for row in result}

        return (doc for doc in documents if doc.id not in database_ids)
