#!/usr/bin/env python3
"""Using pytest-flask to test Flask app"""

import pytest
from exercises.jokes.app import app, send_joke


@pytest.fixture
def client():
    """Create the client fixture"""
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_status(client):
    """GET should work while POST should not"""
    assert client.get("/").status_code == 200
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


@pytest.mark.skip
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
    pytest.main(["-v", "test_jokes.py"])
