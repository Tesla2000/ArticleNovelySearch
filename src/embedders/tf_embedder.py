from __future__ import annotations

import hashlib
from typing import Sequence
from typing import TYPE_CHECKING

import numpy as np
from pydantic import Field
from sklearn.feature_extraction.text import CountVectorizer


if TYPE_CHECKING:
    from src.Config import Config
from src.embedders.embedder import Embedder


class TFEmbedder(Embedder):
    vectorizer: CountVectorizer = Field(default_factory=CountVectorizer)

    def get_embeddings(
        self, texts: Sequence[str], config: "Config"
    ) -> np.ndarray:
        """
        Generates embeddings for a sequence of texts using a vectorizer,
        caching the results for efficiency.
        :param texts: A sequence of strings representing the texts to be
        embedded.
        :param config: A configuration object containing settings for caching
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
