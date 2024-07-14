from __future__ import annotations

from enum import Enum


class ClusteringUniquenessMetricName(str, Enum):
    SUM_OF_CONNECTIONS = "sum_of_connections"
    SOLE_IN_NODE = "sole_in_node"
