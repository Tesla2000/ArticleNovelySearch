from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

import numpy as np


if TYPE_CHECKING:
    from src.Config import Config


class SimilarityCalculator(ABC):
    @abstractmethod
    def calculate_similarity(
        self, embeddings: np.ndarray, config: "Config"
    ) -> np.ndarray:
        raise NotImplementedError
