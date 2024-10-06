from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from ..uniqueness_calculator import UniquenessCalculator
from ..uniqueness_calculator_name import UniquenessCalculatorName
from .uniqueness_metrics.uniqueness_metric import DistanceUniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    DistanceUniquenessMetricName,
)

if TYPE_CHECKING:
    from ...Config import Config


class DistanceUniquenessCalculator(UniquenessCalculator):
    type = UniquenessCalculatorName.DISTANCE
    uniqueness_metric_name_scope = DistanceUniquenessMetricName
    uniqueness_metric_scope = DistanceUniquenessMetric

    def _get_uniqueness_score(
        self, X: np.ndarray, config: "Config"
    ) -> np.ndarray:
        """
        Calculates the uniqueness score based on pairwise similarity of the
        input data.
        :param X: A numpy array containing the input data for which the
        uniqueness score is calculated.
        :param config: An instance of Config that contains configuration
        parameters for the similarity calculation.
        :return: An array of pairwise similarity scores.
        """
        self.pairwise_similarity = (
            self.similarity_calculator.calculate_similarity(X, config)
        )
        return self.pairwise_similarity
