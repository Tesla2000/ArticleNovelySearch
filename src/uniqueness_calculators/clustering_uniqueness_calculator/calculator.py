from __future__ import annotations

import hashlib

import numpy as np
from numpy import load
from numpy import save
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity

from ..uniqueness_calculator import UniquenessCalculator
from .uniqueness_metrics.uniqueness_metric import UniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    ClusteringUniquenessMetricName,
)
from src.Config import Config


class ClusteringUniquenessCalculator(UniquenessCalculator):
    def _get_cosine_similarity(self, X: np.ndarray) -> np.ndarray:
        X.flags.writeable = False
        hash_value = hashlib.sha1(X.data.tobytes()).hexdigest()
        path = Config.cosine_caches.joinpath(hash_value).with_suffix(".npy")
        if path.exists():
            return load(path)
        pairwise_cosine = cosine_similarity(X)
        save(path, pairwise_cosine)
        return pairwise_cosine

    def _cluster(self, X: np.ndarray) -> np.ndarray:
        pairwise_cosine = self._get_cosine_similarity(X)
        return np.array(
            tuple(
                AgglomerativeClustering(
                    n_clusters=i,
                    metric="precomputed",
                    memory=str(Config.hierarchical_caches),
                    compute_full_tree=True,
                    linkage="complete",
                )
                .fit(pairwise_cosine)
                .labels_
                for i in range(2, X.shape[0])
            )
        )

    def _get_uniqueness_score(self, X: np.ndarray) -> np.ndarray:
        clusters = self._cluster(X)
        uniqueness_score = np.empty_like(clusters)
        for n_clusters, row in enumerate(clusters, 2):
            for value in range(n_clusters):
                where_value = np.where(row == value)[0]
                uniqueness_score[n_clusters - 2][where_value] = len(
                    where_value
                )
        return uniqueness_score

    def rank_uniqueness(
        self,
        X: np.ndarray,
        metric: (
            UniquenessMetric | ClusteringUniquenessMetricName
        ) = ClusteringUniquenessMetricName.SUM_OF_CONNECTIONS,
    ) -> np.ndarray:
        uniqueness_score = self._get_uniqueness_score(X)
        if isinstance(metric, UniquenessMetric):
            return metric.apply(uniqueness_score)
        return UniquenessMetric.pick_and_apply(metric, uniqueness_score)
