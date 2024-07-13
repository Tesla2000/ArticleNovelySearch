from __future__ import annotations

import hashlib

import numpy as np
from numpy import load
from numpy import save
from sklearn.metrics.pairwise import cosine_similarity

from ..uniqueness_calculator import UniquenessCalculator
from .uniqueness_metrics.uniqueness_metric import DistanceUniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    DistanceUniquenessMetricName,
)
from src.Config import Config


class DistanceUniquenessCalculator(UniquenessCalculator):
    def _get_cosine_similarity(self, X: np.ndarray) -> np.ndarray:
        X.flags.writeable = False
        hash_value = hashlib.sha1(X.data.tobytes()).hexdigest()
        path = Config.cosine_caches.joinpath(hash_value).with_suffix(".npy")
        if path.exists():
            return load(path)
        pairwise_cosine = cosine_similarity(X)
        save(path, pairwise_cosine)
        return pairwise_cosine

    def _get_uniqueness_score(self, X: np.ndarray) -> np.ndarray:
        return self._get_cosine_similarity(X)

    def rank_uniqueness(
        self,
        X: np.ndarray,
        metric: (
            DistanceUniquenessMetric | DistanceUniquenessMetricName
        ) = DistanceUniquenessMetricName.DISTANCE,
    ) -> np.ndarray:
        uniqueness_score = self._get_uniqueness_score(X)
        if isinstance(metric, DistanceUniquenessMetric):
            return metric.apply(uniqueness_score)
        return DistanceUniquenessMetric.pick_and_apply(
            metric, uniqueness_score
        )
