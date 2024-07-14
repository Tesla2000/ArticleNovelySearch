from __future__ import annotations

from enum import Enum


class UniquenessCalculatorName(str, Enum):
    CLUSTERING = "clustering"
    DISTANCE = "distance"
