from __future__ import annotations

from abc import ABC

from ...uniqueness_metric import UniquenessMetric
from .uniqueness_metric_name import ClusteringUniquenessMetricName


class ClusteringUniquenessMetric(UniquenessMetric, ABC):
    type = ClusteringUniquenessMetricName
