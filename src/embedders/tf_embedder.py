from __future__ import annotations

import hashlib
from typing import Sequence

import numpy as np
from pydantic import Field
from sklearn.feature_extraction.text import CountVectorizer

from src.Config import Config
from src.embedders.embedder import Embedder


class TFEmbedder(Embedder):
    vectorizer: CountVectorizer = Field(default_factory=CountVectorizer)

    def get_embeddings(self, texts: Sequence[str]) -> np.ndarray:
        hash_value = hashlib.sha1(str(texts).encode()).hexdigest()
        path = Config.embeddings_caches.joinpath(hash_value).with_suffix(
            ".npy"
        )
        if path.exists():
            return np.load(path)
        embedding = self.vectorizer.fit_transform(texts).toarray()
        np.save(path, embedding)
        return embedding
