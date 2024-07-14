from __future__ import annotations

from abc import ABC

from ...uniqueness_metric import UniquenessMetric
from .uniqueness_metric_name import DistanceUniquenessMetricName


class DistanceUniquenessMetric(UniquenessMetric, ABC):
    type: DistanceUniquenessMetricName
