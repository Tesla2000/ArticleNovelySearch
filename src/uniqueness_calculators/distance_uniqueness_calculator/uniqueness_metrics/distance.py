from __future__ import annotations

import numpy as np

from .uniqueness_metric import DistanceUniquenessMetric
from .uniqueness_metric_name import DistanceUniquenessMetricName


class DistanceMetric(DistanceUniquenessMetric):
    type: DistanceUniquenessMetricName = DistanceUniquenessMetricName.DISTANCE

    def __init__(self, power: float = 1):
        self.power = power

    def apply(self, cosine_distance_matrix: np.ndarray) -> np.array:
        uniqueness_score = np.sum(cosine_distance_matrix**self.power, axis=0)
        return np.argsort(uniqueness_score)
