from __future__ import annotations

import os

from dotenv import load_dotenv
from phi.knowledge.pdf import PDFUrlKnowledgeBase

from src.embedding_holder import EmbeddingHolder
from src.pdf_reader import PDFAbsractReader

load_dotenv()
db_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
db_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db_name}"


def main():
    vector_db = EmbeddingHolder(collection="articles", db_url=db_url)
    knowledge_base = PDFUrlKnowledgeBase(
        reader=PDFAbsractReader(),
        urls=["https://arxiv.org/pdf/1612.08242"],
        vector_db=vector_db,
    )

    knowledge_base.load()

    vector_db.get_embeddings()


if __name__ == "__main__":
    exit(main())
