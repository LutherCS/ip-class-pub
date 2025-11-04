#!/usr/bin/env python3
"""
jokes api logic

@author:
@version: 2025.11
"""

import pathlib
import random
import tomllib
from functools import cache

import pyjokes
from pyjokes.exc import CategoryNotFoundError, LanguageNotFoundError

from .models import Joke


class Joker:
    """
    A layer to retrieve jokes from the pyjokes package

    :raises ValueError: the dataset has not been initialized
    :raises ValueError: the language is invalid
    :raises ValueError: the category is invalid
    :raises ValueError: the joke id is invalid
    :raises ValueError: requested number of jokes is below 0
    """

    @classmethod
    def init_dataset(cls):
        """
        Initialize the dataset

        Load jokes from the `pyjokes` package into a list of jokes
        """
        # TODO: Implement this method

    @classmethod
    def get_jokes(cls, language: str = "any", category: str = "any", number: int = 0) -> list[Joke]:
        """Get all jokes in the specified language/category combination

        :param language: language of the joke
        :param category: category of the joke
        :param number: number of jokes to return, 0 to return all
        """
        # TODO: Implement this method

    @classmethod
    def get_the_joke(cls, joke_id: int) -> Joke:
        """Get a specific joke by id

        :param joke_id: joke id
        """
        # TODO: Implement this method
