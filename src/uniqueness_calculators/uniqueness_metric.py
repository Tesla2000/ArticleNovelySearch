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
        """
        Applies a uniqueness metric to the provided uniqueness score array,
        returning a transformed array based on the metric's implementation.
        :param uniqueness_score: An array of uniqueness scores to be processed.
        :param cls: The class that implements the uniqueness metric.
        :return: Transformed uniqueness scores as a numpy array.
        """
        raise NotImplementedError

    @classmethod
    def pick_and_apply(
        cls, type: str, clusters: np.ndarray, **kwargs
    ) -> np.ndarray:
        """
        Selects a valid uniqueness metric type and applies it to the provided
        clusters.
        :param cls: The class from which the method is called, typically a
        subclass of UniquenessMetric.
        :param clusters: A numpy array representing the clusters to which the
        metric will be applied.
        :param type: A string representing the type of uniqueness metric to
        apply.
        :return: Transformed clusters as a numpy array.
        """
        for class_ in cls.__subclasses__():
            if class_.is_valid(type):
                return class_(**kwargs).apply(clusters)
        raise ValueError(
            f"{type=} is not a valid {cls} metric valid types are "
            f"{list(class_.type.value for class_ in cls.__subclasses__())}"
        )

    @classmethod
    def is_valid(cls, type: str) -> bool:
        """
        Checks if the given type matches the class's type attribute.
        :param cls: The class that is being checked for type validity.
        :param type: The type string to validate against the class's type.
        :return: True if valid, otherwise False
        """
        return cls.type == type
