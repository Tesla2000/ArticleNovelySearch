from __future__ import annotations

from typing import Sequence

import numpy as np
from pydantic import BaseModel
from pydantic import ConfigDict


class Embedder(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_embeddings(self, text: Sequence[str]) -> np.ndarray:
        raise NotImplementedError
