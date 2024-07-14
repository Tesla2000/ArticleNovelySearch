from __future__ import annotations

import hashlib

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.Config import Config
from src.similarity_calculators.similarity_calculator import (
    SimilarityCalculator,
)


class CosineSimilarityCalculator(SimilarityCalculator):
    def calculate_similarity(self, embeddings: np.ndarray) -> np.ndarray:
        embeddings.flags.writeable = False
        hash_value = hashlib.sha1(embeddings.data.tobytes()).hexdigest()
        path = Config.cosine_caches.joinpath(hash_value).with_suffix(".npy")
        if path.exists():
            return np.load(path)
        pairwise_similarity = cosine_similarity(embeddings)
        np.save(path, pairwise_similarity)
        return pairwise_similarity
