from __future__ import annotations

import numpy as np

from .uniqueness_metric import DistanceUniquenessMetric
from .uniqueness_metric_name import DistanceUniquenessMetricName


class DistanceMetric(DistanceUniquenessMetric):
    type: DistanceUniquenessMetricName = DistanceUniquenessMetricName.DISTANCE

    def __init__(self, power: float = 1):
        """
        Initializes the DistanceMetric class with a specified power for
        distance calculations.
        :param power: Specifies the exponent used in distance calculations,
        defaulting to 1.
        :return: None
        """
        self.power = power

    def apply(self, cosine_distance_matrix: np.ndarray) -> np.array:
        """
        Calculates the uniqueness score from a cosine distance matrix and
        returns the indices that would sort this score.
        :param cosine_distance_matrix: A 2D numpy array representing the cosine
        distance between items.
        :return: Indices of sorted uniqueness scores.
        """
        uniqueness_score = np.sum(cosine_distance_matrix**self.power, axis=0)
        return np.argsort(uniqueness_score)
