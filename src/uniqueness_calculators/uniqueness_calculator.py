from __future__ import annotations

from abc import abstractmethod
from typing import Optional

import numpy as np

from src.similarity_calculators.cosine_similarity_calculator import (
    CosineSimilarityCalculator,
)
from src.similarity_calculators.similarity_calculator import (
    SimilarityCalculator,
)
from src.uniqueness_calculators.uniqueness_metric import UniquenessMetric


class UniquenessCalculator:
    pairwise_similarity: np.ndarray

    def __init__(
        self, similarity_calculator: Optional[SimilarityCalculator] = None
    ):
        similarity_calculator = (
            similarity_calculator or CosineSimilarityCalculator()
        )
        self.similarity_calculator = similarity_calculator

    @abstractmethod
    def _get_uniqueness_score(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def rank_uniqueness(
        self,
        X: np.ndarray,
        metric: UniquenessMetric | str,
    ) -> np.ndarray:
        uniqueness_score = self._get_uniqueness_score(X)
        if isinstance(metric, UniquenessMetric):
            return metric.apply(uniqueness_score)
        return UniquenessMetric.pick_and_apply(metric, uniqueness_score)
