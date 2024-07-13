from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import numpy as np

from src.uniqueness_metrics.uniqueness_metric_name import UniquenessMetricName


class UniquenessMetric(ABC):
    type: UniquenessMetricName

    @classmethod
    @abstractmethod
    def apply(cls, uniqueness_score: np.ndarray) -> np.array:
        raise NotImplementedError

    @staticmethod
    def pick_and_apply(
        type: UniquenessMetricName | str, clusters: np.ndarray
    ) -> np.ndarray:
        for class_ in UniquenessMetric.__subclasses__():
            if class_.is_valid(type):
                return class_().apply(clusters)

    @classmethod
    def is_valid(cls, type: UniquenessMetricName | str) -> bool:
        return cls.type == type
