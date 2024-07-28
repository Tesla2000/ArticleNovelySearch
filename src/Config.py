from __future__ import annotations

import os
from pathlib import Path
from typing import Type

from dotenv import load_dotenv
from pydantic import BaseModel

from src._custom_argument_parser import CustomArgumentParser
from src.uniqueness_calculators.clustering_uniqueness_calculator.uniqueness_metrics.uniqueness_metric_name import (  # noqa: E501
    ClusteringUniquenessMetricName,
)
from src.uniqueness_calculators.distance_uniqueness_calculator.uniqueness_metrics.uniqueness_metric_name import (  # noqa: E501
    DistanceUniquenessMetricName,
)
from src.uniqueness_calculators.uniqueness_calculator_name import (
    UniquenessCalculatorName,
)

load_dotenv()
db_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")


class Config(BaseModel):
    _root: Path = Path(__file__).parent
    _caches: Path = _root / "caches"
    hierarchical_caches: Path = _caches / "hierarchical"
    cosine_caches: Path = _caches / "cosine"
    embeddings_caches: Path = _caches / "embeddings"
    db_url: str = os.getenv("DATABASE_URL") or (
        f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db_name}"
    )
    n_checked_articles: int = 1000
    displayed_n_articles: int = 10
    batch_size: int = 10
    compared_article_title: str = ""
    n_most_similar: int = 5
    topic: str = ""

    calc_uniqueness: bool = True
    uniqueness_calculator_type: str = UniquenessCalculatorName.CLUSTERING.value
    uniqueness_metric_name: str = (
        ClusteringUniquenessMetricName.SOLE_IN_NODE.value
    )
    uniqueness_kwargs: dict = {}

    calc_commonness: bool = True
    commonness_calculator_type: str = UniquenessCalculatorName.DISTANCE.value
    commonness_metric_name: str = DistanceUniquenessMetricName.DISTANCE.value
    commonness_kwargs: dict = {}


def parse_arguments(config_class: Type[Config]):
    parser = CustomArgumentParser(
        description="Configure the application settings."
    )

    for name, value in config_class.model_fields.items():
        if name.startswith("_"):
            continue
        parser.add_argument(
            f"--{name}",
            type=value.annotation,
            default=value.default,
            help=f"Default: {value}",
        )

    return parser.parse_args()


def create_config_with_args(config_class: Type[Config], args) -> Config:
    config = config_class(
        **{name: getattr(args, name) for name in config_class.model_fields}
    )
    for variable in config.model_fields:
        value = getattr(config, variable)
        if (
            isinstance(value, Path)
            and value.suffix == ""
            and not value.exists()
        ):
            value.mkdir(parents=True)
    return config
