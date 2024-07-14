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
        raise NotImplementedError
