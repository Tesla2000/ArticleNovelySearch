from __future__ import annotations

import hashlib
from abc import abstractmethod

import numpy as np
from numpy import load
from numpy import save
from sklearn.metrics.pairwise import cosine_similarity

from src.Config import Config
from src.uniqueness_calculators.uniqueness_metric import UniquenessMetric


class UniquenessCalculator:
    def _get_cosine_similarity(self, X: np.ndarray) -> np.ndarray:
        X.flags.writeable = False
        hash_value = hashlib.sha1(X.data.tobytes()).hexdigest()
        path = Config.cosine_caches.joinpath(hash_value).with_suffix(".npy")
        if path.exists():
            return load(path)
        pairwise_cosine = cosine_similarity(X)
        save(path, pairwise_cosine)
        return pairwise_cosine

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
