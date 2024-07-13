from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    root = Path(__file__).parent


for variable in dir(Config):
    value = getattr(Config, variable)
    if isinstance(value, Path) and value.suffix == "" and not value.exists():
        value.mkdir(parents=True)
