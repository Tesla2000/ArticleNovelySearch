from __future__ import annotations

import sys

import numpy as np

from src.uniqueness_metrics.uniqueness_metric import UniquenessMetric
from src.uniqueness_metrics.uniqueness_metric_name import UniquenessMetricName


class SumOfConnectionsMetric(UniquenessMetric):
    """Very good for finding most common subjects"""

    type: UniquenessMetricName = UniquenessMetricName.SUM_OF_CONNECTIONS

    def __init__(self, connections_cap=sys.maxsize):
        self.connections_cap = connections_cap

    def apply(self, uniqueness_score: np.ndarray) -> np.array:
        uniqueness_score = np.sum(
            np.clip(uniqueness_score, 0, self.connections_cap), axis=0
        )
        return np.argsort(uniqueness_score)
