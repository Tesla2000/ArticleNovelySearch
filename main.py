from __future__ import annotations

import os
from itertools import islice

from dotenv import load_dotenv

from src.Config import Config
from src.embedding_holder import EmbeddingHolder
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
    topic = Topic.LARGE_LEARNING_MODELS
    title = "_title"
    vector_db = EmbeddingHolder(
        collection=f'{topic.replace(" ", "_")}{title}', db_url=db_url
    )
    # vector_db.create()
    # vector_db.insert(
    #     map(
    #         title_from_arxiv if title == "_title" else content_from_arxiv,
    #         search_arxiv(topic, max_results=Config.n_checked_articles),
    #     )
    # )

    print("Calculating clusterization")
    embeddings, metadata = vector_db.get_embeddings(
        limit=Config.n_checked_articles
    )
    print(f"The least relevant article is {metadata[-1]}")
    uniqueness_rank = DistanceUniquenessCalculator().rank_uniqueness(
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
    uniqueness_rank = ClusteringUniquenessCalculator().rank_uniqueness(
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


if __name__ == "__main__":
    exit(main())
