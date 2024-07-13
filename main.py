from __future__ import annotations

import os

from dotenv import load_dotenv

from src.arxiv_searcher import search_arxiv
from src.Config import Config
from src.embedding_holder import EmbeddingHolder
from src.pdf_reader import from_arxiv
from src.topics import Topic
from src.uniqueness_calculator import UniquenessCalculator
from src.uniqueness_metrics.sum_of_connections_metric import (
    SumOfConnectionsMetric,
)

# from src.uniqueness_metrics.longest_sole_in_node_metric import \
#     LongestSoleInNodeMetric

load_dotenv()
db_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
db_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db_name}"


def main():
    topic = Topic.REINFORCEMENT_LEARNING
    vector_db = EmbeddingHolder(
        collection=topic.replace(" ", "_"), db_url=db_url
    )
    vector_db.create()
    vector_db.insert(
        map(
            from_arxiv,
            search_arxiv(topic, max_results=Config.n_checked_articles),
        )
    )

    ids, embeddings = vector_db.get_embeddings()
    uniqueness_rank = UniquenessCalculator().rank_uniqueness(
        embeddings, metric=SumOfConnectionsMetric(20)
    )
    sorted_by_uniqueness = tuple(map(ids.__getitem__, uniqueness_rank))
    print(
        "Most unique articles",
        sorted_by_uniqueness[: Config.displayed_n_articles],
    )
    print(
        "Most common articles",
        tuple(reversed(sorted_by_uniqueness))[: Config.displayed_n_articles],
    )


if __name__ == "__main__":
    exit(main())
