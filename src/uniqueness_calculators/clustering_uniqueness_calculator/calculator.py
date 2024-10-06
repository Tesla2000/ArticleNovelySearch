from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from sklearn.cluster import AgglomerativeClustering

from ..uniqueness_calculator import UniquenessCalculator
from ..uniqueness_calculator_name import UniquenessCalculatorName
from .uniqueness_metrics.uniqueness_metric import ClusteringUniquenessMetric
from .uniqueness_metrics.uniqueness_metric_name import (
    ClusteringUniquenessMetricName,
)

if TYPE_CHECKING:
    from ...Config import Config


class ClusteringUniquenessCalculator(UniquenessCalculator):
    type = UniquenessCalculatorName.CLUSTERING
    uniqueness_metric_name_scope = ClusteringUniquenessMetricName
    uniqueness_metric_scope = ClusteringUniquenessMetric

    def _cluster(self, X: np.ndarray, config: "Config") -> np.ndarray:
        """
        Clusters the input data using agglomerative clustering based on
        pairwise similarity calculated from the input data and configuration
        settings.
        :param X: A 2D numpy array containing the data points to be clustered.
        :param config: An instance of the Config class containing configuration
        settings for clustering.
        :return: An array of cluster labels for each number of clusters.
        """
        self.pairwise_similarity = (
            self.similarity_calculator.calculate_similarity(X, config)
        )
        return np.array(
            tuple(
                AgglomerativeClustering(
                    n_clusters=i,
                    metric="precomputed",
                    memory=str(config.hierarchical_caches),
                    compute_full_tree=True,
                    linkage="complete",
                )
                .fit(self.pairwise_similarity)
                .labels_
                for i in range(2, X.shape[0])
            )
        )

    def _get_uniqueness_score(
        self, X: np.ndarray, config: Config
    ) -> np.ndarray:
        """
        Calculates the uniqueness score for clusters derived from the input
        data based on the provided configuration.
        :param X: A NumPy array representing the input data points to be
        clustered.
        :param config: An instance of Config containing parameters for
        clustering.
        :return: An array of uniqueness scores for each cluster.
        """
        clusters = self._cluster(X, config)
        uniqueness_score = np.empty_like(clusters)
        for n_clusters, row in enumerate(clusters, 2):
            for value in range(n_clusters):
                where_value = np.where(row == value)[0]
                uniqueness_score[n_clusters - 2][where_value] = len(
                    where_value
                )
        return uniqueness_score
