"""
GamelYY model

@author: Roman Yasinovskyy
@version: 2026.10
"""

from dataclasses import dataclass


@dataclass
class Game:
    rank: int
    bgg_url: str
    game_id: int
    names: str
    min_players: int
    max_players: int
    avg_time: int
    min_time: int
    max_time: int
    year: int
    avg_rating: float
    geek_rating: float
    num_votes: int
    image_url: str
    age: int
    mechanic: str
    owned: int
    category: str
    designer: str
    weight: float


class Library:
    def __init__(self) -> None:
        self.items: list[Game] = []

    def __iter__(self):
        return iter(self.items)

    def add(self, new_game) -> None:
        self.items.append(new_game)
