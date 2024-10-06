from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from enum import Enum
from typing import Optional
from typing import Self
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from src.Config import Config
from src.similarity_calculators.cosine_similarity_calculator import (
    CosineSimilarityCalculator,
)
from src.similarity_calculators.similarity_calculator import (
    SimilarityCalculator,
)
from src.uniqueness_calculators.uniqueness_calculator_name import (
    UniquenessCalculatorName,
)
from src.uniqueness_calculators.uniqueness_metric import UniquenessMetric


class UniquenessCalculator(ABC):
    type: UniquenessCalculatorName
    pairwise_similarity: np.ndarray
    uniqueness_metric_name_scope = Enum
    uniqueness_metric_scope = UniquenessMetric

    def __init__(
        self, similarity_calculator: Optional[SimilarityCalculator] = None
    ):
        """
        Initializes the UniquenessCalculator with a specified similarity
        calculator or defaults to CosineSimilarityCalculator.
        :param similarity_calculator: An optional similarity calculator used
        for computing similarity metrics.
        :return: None
        """
        similarity_calculator = (
            similarity_calculator or CosineSimilarityCalculator()
        )
        self.similarity_calculator = similarity_calculator

    @classmethod
    def create(cls, type: str, **kwargs) -> Self:
        """
        Creates an instance of a subclass of UniquenessCalculator based on the
        specified type.
        :param type: A string representing the type of uniqueness calculator to
        create.
        :param cls: The class from which to create an instance.
        :return: An instance of a subclass of UniquenessCalculator.
        """
        for uniqueness_calculator in cls.__subclasses__():
            if uniqueness_calculator.type == type:
                return uniqueness_calculator(**kwargs)
        raise ValueError(
            f"{type=} is not a valid {cls} valid types are "
            f"{list(class_.type.value for class_ in cls.__subclasses__())}"
        )

    @abstractmethod
    def _get_uniqueness_score(
        self, X: np.ndarray, config: "Config"
    ) -> np.ndarray:
        """
        Calculates the uniqueness score for a given dataset based on the
        provided configuration.
        :param config: Configuration settings for the uniqueness calculation.
        :param X: Input data as a NumPy array.
        :return: An array of uniqueness scores.
        """
        raise NotImplementedError

    def rank_uniqueness(
        self,
        X: np.ndarray,
        metric: uniqueness_metric_scope | uniqueness_metric_name_scope,
        config: "Config",
        **kwargs,
    ) -> np.ndarray:
        """
        Calculates and ranks the uniqueness of the input data based on the
        specified metric and configuration.
        :param config: Configuration object for the uniqueness calculation.
        :param metric: The metric used to evaluate uniqueness.
        :param X: Input data array for which uniqueness scores are calculated.
        :return: An array of ranked uniqueness scores.
        """
        uniqueness_score = self._get_uniqueness_score(X, config)
        if isinstance(metric, self.uniqueness_metric_scope):
            return metric.apply(uniqueness_score)
        return self.uniqueness_metric_scope.pick_and_apply(
            metric, uniqueness_score, **kwargs
        )
