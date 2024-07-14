from __future__ import annotations

import os
from itertools import islice

import numpy as np
from dotenv import load_dotenv

from src.arxiv_searcher import search_arxiv
from src.Config import Config
from src.embedding_holder import EmbeddingHolder
from src.pdf_reader import title_from_arxiv
from src.topics import Topic
from src.uniqueness_calculators.clustering_uniqueness_calculator.calculator import (  # noqa: E501
    ClusteringUniquenessCalculator,
)
from src.uniqueness_calculators.clustering_uniqueness_calculator.uniqueness_metrics.longest_sole_in_node_metric import (  # noqa: E501
    LongestSoleInNodeMetric,
)
from src.uniqueness_calculators.distance_uniqueness_calculator.calculator import (  # noqa: E501
    DistanceUniquenessCalculator,
)
from src.uniqueness_calculators.distance_uniqueness_calculator.uniqueness_metrics.distance import (  # noqa: E501
    DistanceMetric,
)

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
    if vector_db.get_count() < Config.n_checked_articles:
        vector_db.insert(
            map(
                title_from_arxiv,
                search_arxiv(topic, max_results=Config.n_checked_articles),
            )
        )
    embeddings, metadata = vector_db.get_embeddings(
        limit=Config.n_checked_articles
    )
    least_relevant_title = metadata[-1]["title"]
    print(f"The least relevant article is {least_relevant_title}")
    distance_uniqueness_calculator = DistanceUniquenessCalculator()
    uniqueness_rank = distance_uniqueness_calculator.rank_uniqueness(
        embeddings, metric=DistanceMetric()
    )
    print(
        "Most common articles",
        list(
            map(
                metadata.__getitem__,
                islice(reversed(uniqueness_rank), Config.displayed_n_articles),
            )
        ),
    )
    clustering_uniqueness_calculator = ClusteringUniquenessCalculator()
    uniqueness_rank = clustering_uniqueness_calculator.rank_uniqueness(
        embeddings, metric=LongestSoleInNodeMetric()
    )
    print(
        "Most unique articles",
        list(
            map(
                metadata.__getitem__,
                uniqueness_rank[: Config.displayed_n_articles],
            )
        ),
    )
    if Config.compared_article_title:
        embeddings = np.append(
            embeddings,
            np.array([
                vector_db.embedder.get_embedding(Config.compared_article_title)
            ]),
            axis=0,
        )
        uniqueness_rank = clustering_uniqueness_calculator.rank_uniqueness(
            embeddings, metric=LongestSoleInNodeMetric()
        )
        highest_similarities = np.argsort(
            clustering_uniqueness_calculator.pairwise_similarity[-1]
        )[
            -Config.n_most_similar - 1 : -1  # noqa: E203
        ]
        similar = list(map(metadata.__getitem__, highest_similarities))
        print(
            f'"{Config.compared_article_title}" ranked as '
            f"{np.argmax(uniqueness_rank)} the most "
            f"similar articles are {similar}"
        )


if __name__ == "__main__":
    exit(main())
