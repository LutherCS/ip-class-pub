"""
GamelYY with FastAPI
Logic

@author: Roman Yasinovskyy
@version: 2026.11
"""

from .config import settings
from .model import Game


def game_lookup(title: str) -> Game:
    for a_game in settings.db:
        if a_game["names"] == title:
            return Game(*a_game.values())
    raise ValueError(f"There is no game with tile {title} in our dataset")
