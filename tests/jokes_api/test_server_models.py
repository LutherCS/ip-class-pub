#!/usr/bin/env python3
"""
Test jokes_api server models

@author: Roman Yasinovskyy
@version: 2025.11
"""

import pathlib
import random
import string
import sys
from importlib import util
from itertools import product

import pytest

try:
    util.find_spec("projects." + pathlib.Path(__file__).parts[-2])
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from projects.jokes_api.server.joker.models import Joke


@pytest.mark.parametrize(
    "language, category, text",
    product(
        ["".join(random.sample(string.ascii_lowercase, 2))],
        ["".join(random.sample(string.ascii_lowercase, 4))],
        ["Lorem impsum dolor sit amet..."],
    ),
)
def test_create_a_joke(language: str, category: str, text: str) -> None:
    """Joke is a dataclass"""
    joke = Joke(language, category, text)
    assert isinstance(joke, Joke)
    assert joke.language == language
    assert joke.category == category
    assert joke.text == text


if __name__ == "__main__":
    pytest.main(["-v", __file__])
