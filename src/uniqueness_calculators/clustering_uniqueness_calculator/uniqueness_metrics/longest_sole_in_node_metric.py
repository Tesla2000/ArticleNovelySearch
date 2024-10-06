from __future__ import annotations

import numpy as np

from .uniqueness_metric import ClusteringUniquenessMetric
from .uniqueness_metric_name import ClusteringUniquenessMetricName


class LongestSoleInNodeMetric(ClusteringUniquenessMetric):
    """Very good for finding niche subjects in a small number"""

    type: ClusteringUniquenessMetricName = (
        ClusteringUniquenessMetricName.SOLE_IN_NODE
    )

    def __init__(self, neighbours: int = 1):
        """
        Initializes the LongestSoleInNodeMetric with a specified number of
        neighbours.
        :param neighbours: The number of neighbours to consider for the metric.
        :return: None
        """
        self.neighbours = neighbours

    def apply(self, uniqueness_score: np.ndarray) -> np.array:
        """
        Applies a uniqueness scoring method to determine the order of elements
        based on their uniqueness scores relative to a specified number of
        neighbors.
        :param uniqueness_score: Calculates how many uniqueness scores are less
        than or equal to the specified number of neighbors.
        :return: Sorted indices of uniqueness scores.
        """
        uniqueness_score = np.sum(uniqueness_score <= self.neighbours, axis=0)
        return np.argsort(uniqueness_score)
