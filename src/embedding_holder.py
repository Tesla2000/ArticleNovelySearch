from __future__ import annotations

from hashlib import md5
from itertools import filterfalse
from typing import Iterable

import numpy as np
from more_itertools import unzip
from phi.document import Document
from phi.utils.log import logger
from phi.vectordb.pgvector.pgvector2 import PgVector2
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.expression import select


class EmbeddingHolder(PgVector2):
    def get_embeddings(self) -> tuple[list[str], np.ndarray]:
        with self.Session() as sess:
            with sess.begin():
                stmt = select(
                    self.table.c.id, self.table.c.embedding
                ).select_from(self.table)
                ids, embeddings = unzip(sess.execute(stmt).fetchall())
                return list(ids), np.array(tuple(embeddings))

    def insert(
        self, documents: Iterable[Document], batch_size: int = 10
    ) -> None:
        with self.Session() as sess:
            counter = 0
            for document in filterfalse(self.doc_exists, documents):
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
                counter += 1
                logger.debug(f"Inserted document: {document.name}")

                if counter >= batch_size:
                    sess.commit()
                    logger.info(f"Committed {counter} documents")
                    counter = 0

            # Commit any remaining documents
            if counter > 0:
                sess.commit()
                logger.info(f"Committed {counter} documents")
