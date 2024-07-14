from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from enum import Enum

import numpy as np


class UniquenessMetric(ABC):
    type: Enum

    @classmethod
    @abstractmethod
    def apply(cls, uniqueness_score: np.ndarray) -> np.array:
        raise NotImplementedError

    @classmethod
    def pick_and_apply(
        cls, type: str, clusters: np.ndarray, **kwargs
    ) -> np.ndarray:
        for class_ in cls.__subclasses__():
            if class_.is_valid(type):
                return class_(**kwargs).apply(clusters)
        raise ValueError(
            f"{type=} is not a valid {cls} metric valid types are "
            f"{list(class_.type.value for class_ in cls.__subclasses__())}"
        )

    @classmethod
    def is_valid(cls, type: str) -> bool:
        return cls.type == type
