from __future__ import annotations

import hashlib
from typing import Sequence
from typing import TYPE_CHECKING

import numpy as np
from pydantic import Field
from sklearn.feature_extraction.text import TfidfVectorizer


if TYPE_CHECKING:
    from src.Config import Config
from src.embedders.embedder import Embedder


class TFIDFEmbedder(Embedder):
    vectorizer: TfidfVectorizer = Field(default_factory=TfidfVectorizer)

    def get_embeddings(
        self, texts: Sequence[str], config: "Config"
    ) -> np.ndarray:
        """
        Generates or retrieves TF-IDF embeddings for a given sequence of texts,
        caching the result for future use.
        :param texts: A sequence of strings representing the texts to be
        embedded.
        :param config: Configuration object containing settings for caching
        embeddings.
        :return: A NumPy array of embeddings.
        """
        hash_value = hashlib.sha1(str(texts).encode()).hexdigest()
        path = config.embeddings_caches.joinpath(hash_value).with_suffix(
            ".npy"
        )
        if path.exists():
            return np.load(path)
        embedding = self.vectorizer.fit_transform(texts).toarray()
        np.save(path, embedding)
        return embedding
