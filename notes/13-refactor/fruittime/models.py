#!/usr/bin/env python3

"""
Fruittime models

@author: CS330
@version: 2025.11
"""


class Reviews:
    def __init__(self) -> None:
        self.reviews: list[dict] = []

    def add(self, review: dict) -> None:
        self.reviews.append(review)

    def remove(self, idx: int) -> None:
        self.reviews.pop(idx)

    def __len__(self) -> int:
        return len(self.reviews)

    def __iter__(self):
        return iter(self.reviews)
