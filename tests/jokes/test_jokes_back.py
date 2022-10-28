#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2022.10
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec("exercises." + pathlib.Path(__file__).parts[-2], "jokes")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.jokes.app import app, send_joke


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_status_get(client):
    """GET should work"""
    assert client.get("/").status_code == 200


def test_status_post(client):
    """POST should not work without any data"""
    assert client.post("/").status_code == 500


@pytest.mark.parametrize(
    "language, category",
    [
        ("de", "all"),
        ("de", "chuck"),
        ("de", "neutral"),
        ("en", "all"),
        ("en", "chuck"),
        ("en", "neutral"),
        ("es", "all"),
        ("es", "chuck"),
        ("es", "neutral"),
    ],
)
def test_index_post(client, language, category):
    """Various combinations of language/category should be handled"""
    assert (
        client.post("/", data=dict(language=language, category=category)).status_code
        == 200
    )


@pytest.mark.parametrize(
    "language, category",
    [
        ("de", "all"),
        ("de", "chuck"),
        ("de", "neutral"),
        ("en", "all"),
        ("en", "chuck"),
        ("en", "neutral"),
        ("es", "all"),
        ("es", "chuck"),
        ("es", "neutral"),
    ],
)
def test_send_joke(language, category):
    """Various combinations of language/category should be handled"""
    assert len(send_joke(language, category)) == 1


def test_send_joke_error():
    """There are no Chuck Norris jokes in Spanish"""
    assert send_joke("es", "chuck") == ["No kidding!"]


@pytest.mark.parametrize(
    "language, category, number",
    [
        ("de", "all", 146),
        ("en", "chuck", 103),
        ("es", "neutral", 14),
    ],
)
def test_send_jokes(language, category, number):
    """There is a limited number of jokes in each category/language"""
    assert len(send_joke(language, category, 330)) == number


if __name__ == "__main__":
    pytest.main(["-v", __file__])
