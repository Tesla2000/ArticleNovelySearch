from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    n_checked_articles = 1000
    displayed_n_articles = 10
    batch_size = 10
    root = Path(__file__).parent
    caches = root / "caches"
    hierarchical_caches = caches / "hierarchical"
    cosine_caches = caches / "cosine"
    embeddings_caches = caches / "embeddings"
    compared_article_title = "Using Beam Search to master Splendor game"
    # compared_article_title = ""
    n_most_similar = 5


for variable in dir(Config):
    value = getattr(Config, variable)
    if isinstance(value, Path) and value.suffix == "" and not value.exists():
        value.mkdir(parents=True)
