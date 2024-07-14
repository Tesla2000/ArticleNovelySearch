from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import numpy as np


class SimilarityCalculator(ABC):
    @abstractmethod
    def calculate_similarity(self, embeddings: np.ndarray) -> np.ndarray:
        raise NotImplementedError
