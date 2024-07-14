from __future__ import annotations

import numpy as np
from sklearn.cluster import AgglomerativeClustering

from ..uniqueness_calculator import UniquenessCalculator
from .uniqueness_metrics.uniqueness_metric import ClusteringUniquenessMetric
from .uniqueness_metrics.uniqueness_metric import UniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    ClusteringUniquenessMetricName,
)
from src.Config import Config


class ClusteringUniquenessCalculator(UniquenessCalculator):
    def _cluster(self, X: np.ndarray) -> np.ndarray:
        self.pairwise_similarity = (
            self.similarity_calculator.calculate_similarity(X)
        )
        return np.array(
            tuple(
                AgglomerativeClustering(
                    n_clusters=i,
                    metric="precomputed",
                    memory=str(Config.hierarchical_caches),
                    compute_full_tree=True,
                    linkage="complete",
                )
                .fit(self.pairwise_similarity)
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
            ClusteringUniquenessMetric | ClusteringUniquenessMetricName
        ) = ClusteringUniquenessMetricName.SOLE_IN_NODE,
    ) -> np.ndarray:
        uniqueness_score = self._get_uniqueness_score(X)
        if isinstance(metric, UniquenessMetric):
            return metric.apply(uniqueness_score)
        return ClusteringUniquenessMetric.pick_and_apply(
            metric, uniqueness_score
        )
