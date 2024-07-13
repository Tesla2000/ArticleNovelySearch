from __future__ import annotations

from phi.vectordb.pgvector import PgVector2
from sqlalchemy import select


class EmbeddingHolder(PgVector2):
    def get_embeddings(self):
        with self.Session() as sess:
            with sess.begin():
                stmt = select(self.table.c.embedding).select_from(self.table)
                return sess.execute(stmt).fetchall()
