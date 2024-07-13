from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    n_checked_articles = 1000
    displayed_n_articles = 10
    root = Path(__file__).parent
    caches = root / "caches"
    hierarchical_caches = caches / "hierarchical"
    cosine_caches = caches / "cosine"


for variable in dir(Config):
    value = getattr(Config, variable)
    if isinstance(value, Path) and value.suffix == "" and not value.exists():
        value.mkdir(parents=True)
