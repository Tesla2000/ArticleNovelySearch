from __future__ import annotations

import sys

import numpy as np

from .uniqueness_metric import ClusteringUniquenessMetric
from .uniqueness_metric_name import ClusteringUniquenessMetricName


class SumOfConnectionsMetric(ClusteringUniquenessMetric):
    """Very good for finding most common subjects"""

    type: ClusteringUniquenessMetricName = (
        ClusteringUniquenessMetricName.SUM_OF_CONNECTIONS
    )

    def __init__(self, connections_cap=sys.maxsize):
        self.connections_cap = connections_cap

    def apply(self, uniqueness_score: np.ndarray) -> np.array:
        uniqueness_score = np.sum(
            np.clip(uniqueness_score, 0, self.connections_cap), axis=0
        )
        return np.argsort(uniqueness_score)
