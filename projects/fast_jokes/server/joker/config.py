"""
fast jokes api configuration

@author:
@version: 2026.11
"""

from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    languages: dict[
        Literal["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"], str
    ] = {
        "cs": "CZECH",
        "de": "GERMAN",
        "en": "ENGLISH",
        "es": "SPANISH",
        "eu": "BASQUE",
        "fr": "FRENCH",
        "gl": "GALICIAN",
        "hu": "HUNGARIAN",
        "it": "ITALIAN",
        "lt": "LITHUANIAN",
        "pl": "POLISH",
        "sv": "SWEDISH",
    }
    categories: dict[Literal["neutral", "chuck"], str] = {
        "neutral": "Neutral",
        "chuck": "Chuck Norris",
    }


settings = Settings()
