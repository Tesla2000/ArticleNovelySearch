from __future__ import annotations

from abc import ABC

import numpy as np

from ...uniqueness_metric import UniquenessMetric
from .uniqueness_metric_name import ClusteringUniquenessMetricName


class ClusteringUniquenessMetric(UniquenessMetric, ABC):
    type: ClusteringUniquenessMetricName

    @staticmethod
    def pick_and_apply(
        type: ClusteringUniquenessMetricName | str, clusters: np.ndarray
    ) -> np.ndarray:
        for class_ in ClusteringUniquenessMetric.__subclasses__():
            if class_.is_valid(type):
                return class_().apply(clusters)

    @classmethod
    def is_valid(cls, type: ClusteringUniquenessMetricName | str) -> bool:
        return cls.type == type
