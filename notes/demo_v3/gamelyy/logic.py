"""
GamelYY logic

@author: Roman Yasinovskyy
@version: 2026.10
"""

from flask import current_app

from gamelyy.model import Game


def game_lookup(title: str) -> Game:
    for a_game in current_app.config["DB"]:
        if a_game["names"] == title:
            return Game(*a_game.values())
    raise ValueError(f"There is no game with tile {title} in our dataset")
