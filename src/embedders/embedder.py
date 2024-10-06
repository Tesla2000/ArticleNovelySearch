from __future__ import annotations

from typing import Sequence
from typing import TYPE_CHECKING

import numpy as np
from pydantic import BaseModel
from pydantic import ConfigDict

if TYPE_CHECKING:
    from src.Config import Config


class Embedder(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_embeddings(
        self, text: Sequence[str], config: "Config"
    ) -> np.ndarray:
        """
        Retrieves embeddings for a given sequence of text using a specified
        configuration.
        :param config: Configuration settings for the embedding process.
        :param text: A sequence of strings for which embeddings are to be
        generated.
        :return: An array of embeddings for the input text.
        """
        raise NotImplementedError
