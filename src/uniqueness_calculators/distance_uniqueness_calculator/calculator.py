from __future__ import annotations

import numpy as np

from ..uniqueness_calculator import UniquenessCalculator
from .uniqueness_metrics.uniqueness_metric import DistanceUniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    DistanceUniquenessMetricName,
)


class DistanceUniquenessCalculator(UniquenessCalculator):

    def _get_uniqueness_score(self, X: np.ndarray) -> np.ndarray:
        self.pairwise_similarity = (
            self.similarity_calculator.calculate_similarity(X)
        )
        return self.pairwise_similarity

    def rank_uniqueness(
        self,
        X: np.ndarray,
        metric: (
            DistanceUniquenessMetric | DistanceUniquenessMetricName
        ) = DistanceUniquenessMetricName.DISTANCE,
    ) -> np.ndarray:
        uniqueness_score = self._get_uniqueness_score(X)
        if isinstance(metric, DistanceUniquenessMetric):
            return metric.apply(uniqueness_score)
        return DistanceUniquenessMetric.pick_and_apply(
            metric, uniqueness_score
        )
