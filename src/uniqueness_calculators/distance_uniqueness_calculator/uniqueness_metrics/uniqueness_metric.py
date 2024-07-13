from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import numpy as np

from .uniqueness_metric_name import DistanceUniquenessMetricName


class DistanceUniquenessMetric(ABC):
    type: DistanceUniquenessMetricName

    @classmethod
    @abstractmethod
    def apply(cls, uniqueness_score: np.ndarray) -> np.array:
        raise NotImplementedError

    @staticmethod
    def pick_and_apply(
        type: DistanceUniquenessMetricName | str, clusters: np.ndarray
    ) -> np.ndarray:
        for class_ in DistanceUniquenessMetric.__subclasses__():
            if class_.is_valid(type):
                return class_().apply(clusters)

    @classmethod
    def is_valid(cls, type: DistanceUniquenessMetricName | str) -> bool:
        return cls.type == type
