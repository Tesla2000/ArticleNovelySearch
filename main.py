from __future__ import annotations

from itertools import islice

import numpy as np

from src.arxiv_searcher import search_arxiv
from src.Config import Config
from src.Config import create_config_with_args
from src.Config import parse_arguments
from src.embedding_holder import EmbeddingHolder
from src.pdf_reader import title_from_arxiv
from src.uniqueness_calculators.uniqueness_calculator import (
    UniquenessCalculator,
)


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    vector_db = EmbeddingHolder(
        collection=config.topic.lower().replace(" ", "_"), db_url=config.db_url
    )
    embeddings, metadata = _get_embeddings(config, vector_db)
    least_relevant_title = metadata[-1]["title"]
    print(f"The least relevant article is {least_relevant_title}")

    if config.calc_commonness:
        distance_uniqueness_calculator = UniquenessCalculator.create(
            config.commonness_calculator_type
        )
        most_common_articles = _get_most_common(
            config, embeddings, metadata, distance_uniqueness_calculator
        )
        print(f"Most common articles {most_common_articles}")

    if config.calc_uniqueness:
        clustering_uniqueness_calculator = UniquenessCalculator.create(
            config.uniqueness_calculator_type
        )
        most_unique_articles = _get_most_unique(
            config, embeddings, metadata, clustering_uniqueness_calculator
        )
        print(f"Most unique articles {most_unique_articles}")

    if config.compared_article_title:
        clustering_uniqueness_calculator = UniquenessCalculator.create(
            config.uniqueness_calculator_type
        )
        _print_uniqueness(
            config,
            embeddings,
            vector_db,
            clustering_uniqueness_calculator,
            metadata,
        )


def _get_embeddings(
    config: Config, vector_db: EmbeddingHolder
) -> tuple[np.ndarray, list[dict[str, str]]]:
    vector_db.create()
    if vector_db.get_count() < config.n_checked_articles:
        vector_db.insert(
            map(
                title_from_arxiv,
                search_arxiv(
                    config.topic, max_results=config.n_checked_articles
                ),
            ),
            config.batch_size,
        )
    return vector_db.get_embeddings(limit=config.n_checked_articles)


def _get_most_common(
    config: Config,
    embeddings: np.ndarray,
    metadata: list[dict[str, str]],
    uniqueness_calculator: UniquenessCalculator,
) -> list[dict[str, str]]:
    uniqueness_rank = uniqueness_calculator.rank_uniqueness(
        embeddings,
        config.commonness_metric_name,
        config,
        **config.commonness_kwargs,
    )
    return list(
        map(
            metadata.__getitem__,
            islice(reversed(uniqueness_rank), config.displayed_n_articles),
        )
    )


def _get_most_unique(
    config: Config,
    embeddings: np.ndarray,
    metadata: list[dict[str, str]],
    uniqueness_calculator: UniquenessCalculator,
) -> list[dict[str, str]]:
    uniqueness_rank = uniqueness_calculator.rank_uniqueness(
        embeddings,
        config.uniqueness_metric_name,
        config,
        **config.uniqueness_kwargs,
    )
    return list(
        map(
            metadata.__getitem__,
            uniqueness_rank[: config.displayed_n_articles],
        )
    )


def _print_uniqueness(
    config: Config,
    embeddings: np.ndarray,
    vector_db: EmbeddingHolder,
    uniqueness_calculator: UniquenessCalculator,
    metadata: list[dict[str, str]],
):
    embeddings = np.append(
        embeddings,
        np.array(
            [vector_db.embedder.get_embedding(config.compared_article_title)]
        ),
        axis=0,
    )
    uniqueness_rank = uniqueness_calculator.rank_uniqueness(
        embeddings,
        config.uniqueness_metric_name,
        config,
        **config.uniqueness_kwargs,
    )
    highest_similarities = np.argsort(
        uniqueness_calculator.pairwise_similarity[-1]
    )[
        -config.n_most_similar - 1 : -1  # noqa: E203
    ]
    similar = list(map(metadata.__getitem__, highest_similarities))
    print(
        f'"{config.compared_article_title}" ranked as '
        f"{np.argmax(uniqueness_rank)} the most "
        f"similar articles are {similar}"
    )


if __name__ == "__main__":
    exit(main())
