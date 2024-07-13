from __future__ import annotations

import os
from itertools import islice

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
        collection=f'{topic.replace(" ", "_")}_title', db_url=db_url
    )
    vector_db.create()
    vector_db.insert(
        map(
            title_from_arxiv,
            search_arxiv(topic, max_results=Config.n_checked_articles),
        )
    )

    print("Calculating clusterization")
    ids, names, embeddings = vector_db.get_embeddings()
    uniqueness_rank = DistanceUniquenessCalculator().rank_uniqueness(
        embeddings, metric=DistanceMetric(0.1)
    )
    print(
        "Most common articles",
        {
            ids[index]: names[index]
            for index in islice(
                reversed(uniqueness_rank), Config.displayed_n_articles
            )
        },
    )
    uniqueness_rank = ClusteringUniquenessCalculator().rank_uniqueness(
        embeddings, metric=LongestSoleInNodeMetric()
    )
    print(
        "Most unique articles",
        {
            ids[index]: names[index]
            for index in uniqueness_rank[: Config.displayed_n_articles]
        },
    )


if __name__ == "__main__":
    exit(main())
