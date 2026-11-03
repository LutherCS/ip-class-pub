"""
GamelYY with FastAPI
Configuration and settings

@author: Roman Yasinovskyy
@version: 2026.11
"""

import csv
import pathlib
from typing import ClassVar

from pydantic_settings import BaseSettings

from .model import Library


class Settings(BaseSettings):
    datasource: ClassVar
    this_dir: pathlib.Path = pathlib.Path(__file__).parent
    with open(this_dir.parent / pathlib.Path("dataset.csv")) as datasource:
        db: list[dict[str, str | int | float]] = list(csv.DictReader(datasource))
    shelf: Library = Library()


settings = Settings()
