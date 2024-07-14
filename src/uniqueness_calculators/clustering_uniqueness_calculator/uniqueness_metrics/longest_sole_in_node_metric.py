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
        self.neighbours = neighbours

    def apply(self, uniqueness_score: np.ndarray) -> np.array:
        uniqueness_score = np.sum(uniqueness_score <= self.neighbours, axis=0)
        return np.argsort(uniqueness_score)
