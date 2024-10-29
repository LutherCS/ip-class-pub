#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2024.10
"""

import pathlib
import sys
from importlib import util
from itertools import product

import pytest

try:
    util.find_spec("exercises." + pathlib.Path(__file__).parts[-2], "jokes")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.jokes.app import app, get_jokes


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_status_get(client) -> None:
    """GET should work"""
    assert client.get("/").status_code == 200


@pytest.mark.parametrize(
    "language, category",
    product(
        ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"],
        ["all", "chuck", "neutral"],
    ),
)
def test_status_post(client, language: str, category: str) -> None:
    """POST with various combinations of language/category should work"""
    assert (
        client.post("/", data=dict(language=language, category=category)).status_code
        == 200
    )


def test_status_post_error(client) -> None:
    """POST without any data should not work"""
    assert client.post("/").status_code == 405


@pytest.mark.parametrize(
    "language, category",
    product(
        ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"],
        ["all", "chuck", "neutral"],
    ),
)
def test_get_a_joke(language: str, category: str) -> None:
    """Various combinations of language/category should be handled and return a single joke"""
    assert len(get_jokes(language, category)) == 1


@pytest.mark.parametrize(
    "language, category, number",
    product(
        ["cs", "de", "en", "es", "it", "pl"],
        ["all", "chuck", "neutral"],
        range(1, 10),
    ),
)
def test_get_n_jokes(language: str, category: str, number: int) -> None:
    """Some combinations of language/category should return multiple jokes"""
    assert len(get_jokes(language, category, number)) == number


@pytest.mark.parametrize(
    "language, category, number",
    [
        ("cs", "all", 41),
        ("de", "all", 127),
        ("en", "all", 283),
        ("es", "all", 44),
        ("eu", "all", 5),
        ("fr", "all", 26),
        ("gl", "all", 14),
        ("hu", "all", 9),
        ("it", "all", 159),
        ("lt", "all", 30),
        ("pl", "all", 174),
        ("sv", "all", 41),
        ("cs", "chuck", 12),
        ("de", "chuck", 68),
        ("en", "chuck", 103),
        ("es", "chuck", 16),
        ("hu", "chuck", 1),
        ("it", "chuck", 87),
        ("pl", "chuck", 99),
        ("cs", "neutral", 29),
        ("de", "neutral", 59),
        ("en", "neutral", 180),
        ("es", "neutral", 28),
        ("eu", "neutral", 5),
        ("fr", "neutral", 26),
        ("gl", "neutral", 14),
        ("hu", "neutral", 8),
        ("it", "neutral", 72),
        ("lt", "neutral", 30),
        ("pl", "neutral", 75),
        ("sv", "neutral", 41),
    ],
)
def test_get_all_jokes(language: str, category: str, number: int) -> None:
    """There is a limited number of jokes in each category/language"""
    assert len(get_jokes(language, category, 330)) == number


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
def test_get_jokes_error(language: str) -> None:
    """There are no Chuck Norris jokes in some languages"""
    assert get_jokes(language, "chuck") == ["No kidding!"]


if __name__ == "__main__":
    pytest.main(["-v", __file__])
