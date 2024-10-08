from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


if TYPE_CHECKING:
    from src.Config import Config
from src.similarity_calculators.similarity_calculator import (
    SimilarityCalculator,
)


class CosineSimilarityCalculator(SimilarityCalculator):
    def calculate_similarity(
        self, embeddings: np.ndarray, config: "Config"
    ) -> np.ndarray:
        """
        Calculates the cosine similarity between given embeddings and caches
        the result for future use.
        :param config: Configuration object containing cache path settings.
        :param embeddings: Numpy array of embeddings to compute similarity for.
        :return: Pairwise cosine similarity matrix
        """
        embeddings.flags.writeable = False
        hash_value = hashlib.sha1(embeddings.data.tobytes()).hexdigest()
        path = config.cosine_caches.joinpath(hash_value).with_suffix(".npy")
        if path.exists():
            return np.load(path)
        pairwise_similarity = cosine_similarity(embeddings)
        np.save(path, pairwise_similarity)
        return pairwise_similarity
