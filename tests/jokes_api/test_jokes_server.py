#!/usr/bin/env python3
"""
Using pytest-flask to test `jokes_api` server

@authors: Roman Yasinovskyy
@version: 2024.11
"""

import pathlib
import sys
from importlib import util
from itertools import product

import pytest
import werkzeug

try:
    util.find_spec("projects." + pathlib.Path(__file__).parts[-2], "jokes_api")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from projects.jokes_api.server.app import (
        app,
        get_all_jokes,
        get_n_jokes,
        get_the_joke,
    )


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


@pytest.mark.parametrize(
    "language", ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"]
)
def test_get_all_status(client, language: str) -> None:
    """There are jokes in various languages"""
    assert client.get(f"/api/v1/jokes/{language}/all").status_code == 200


@pytest.mark.parametrize(
    "language", ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"]
)
def test_get_neutral_status(client, language: str) -> None:
    """There are neutral jokes in various languages"""
    assert client.get(f"/api/v1/jokes/{language}/neutral").status_code == 200


@pytest.mark.parametrize("language", ["cs", "de", "en", "es", "hu", "it", "pl"])
def test_get_chuck_status(client, language: str) -> None:
    """There are chuck jokes in some languages"""
    assert client.get(f"/api/v1/jokes/{language}/chuck").status_code == 200


@pytest.mark.parametrize("language", ["eu", "fr", "gl", "lt", "sv"])
def test_get_chuck_status_error(client, language: str) -> None:
    """There are no chuck jokes in some languages"""
    assert client.get(f"/api/v1/jokes/{language}/chuck").status_code == 404


@pytest.mark.parametrize(
    "language, number",
    [
        ("cs", 41),
        ("de", 127),
        ("en", 283),
        ("es", 44),
        ("eu", 5),
        ("fr", 26),
        ("gl", 14),
        ("hu", 9),
        ("it", 159),
        ("lt", 30),
        ("pl", 174),
        ("sv", 41),
    ],
)
def test_get_all_quantity(language: str, number: int) -> None:
    """The is a limited number of jokes in each language"""
    with app.app_context():
        assert len(get_all_jokes(language, "all").json["jokes"]) == number


@pytest.mark.parametrize(
    "language, number",
    [
        ("cs", 29),
        ("de", 59),
        ("en", 180),
        ("es", 28),
        ("eu", 5),
        ("fr", 26),
        ("gl", 14),
        ("hu", 8),
        ("it", 72),
        ("lt", 30),
        ("pl", 75),
        ("sv", 41),
    ],
)
def test_get_neutral_quantity(language: str, number: int) -> None:
    """The is a limited number of neutral jokes in each language"""
    with app.app_context():
        assert len(get_all_jokes(language, "neutral").json["jokes"]) == number


@pytest.mark.parametrize(
    "language, number",
    [
        ("cs", 12),
        ("de", 68),
        ("en", 103),
        ("es", 16),
        ("hu", 1),
        ("it", 87),
        ("pl", 99),
    ],
)
def test_get_chuck_quantity(language: str, number: int) -> None:
    """The is a limited number of chuck jokes in some languages"""
    with app.app_context():
        assert len(get_all_jokes(language, "chuck").json["jokes"]) == number


@pytest.mark.parametrize(
    "language, error_message",
    [
        ("eu", "404 Not Found: There are no chuck jokes in Basque"),
        ("fr", "404 Not Found: There are no chuck jokes in French"),
        ("gl", "404 Not Found: There are no chuck jokes in Galician"),
        ("lt", "404 Not Found: There are no chuck jokes in Lithuanian"),
        ("sv", "404 Not Found: There are no chuck jokes in Swedish"),
    ],
)
def test_get_chuck_error(language: str, error_message: str) -> None:
    """The are no chuck jokes in some languages"""
    with app.app_context():
        with pytest.raises(werkzeug.exceptions.NotFound) as excinfo:
            get_all_jokes(language, "chuck")
        assert str(excinfo.value) == error_message


@pytest.mark.parametrize(
    "language, category, number, expected",
    [
        ("cs", "all", 33, 33),
        ("cs", "all", 330, 41),
        ("de", "all", 33, 33),
        ("de", "all", 330, 127),
        ("en", "all", 33, 33),
        ("en", "all", 330, 283),
        ("es", "all", 33, 33),
        ("es", "all", 330, 44),
        ("eu", "all", 3, 3),
        ("eu", "all", 330, 5),
        ("fr", "all", 3, 3),
        ("fr", "all", 330, 26),
        ("gl", "all", 3, 3),
        ("gl", "all", 330, 14),
        ("hu", "all", 3, 3),
        ("hu", "all", 330, 9),
        ("it", "all", 33, 33),
        ("it", "all", 330, 159),
        ("lt", "all", 3, 3),
        ("lt", "all", 330, 30),
        ("pl", "all", 33, 33),
        ("pl", "all", 330, 174),
        ("sv", "all", 33, 33),
        ("sv", "all", 330, 41),
    ],
)
def test_get_n_jokes(language: str, category: str, number: int, expected: int) -> None:
    """The is a limited number of jokes in any language"""
    with app.app_context():
        assert len(get_n_jokes(language, category, number).json["jokes"]) == expected


@pytest.mark.parametrize(
    "joke_id, joke_text",
    [
        (0, "Webmaster vyplňuje dotazník: Věk: 25 Výška: 185 Barva očí: #4040FF"),
        (
            100,
            "Chuck Norris streichelt keine Tiere, die Tiere streicheln sich selbst, wenn er in der Nähe ist",
        ),
        (
            200,
            "Why did Microsoft name their search engine BING? Because It's Not Google.",
        ),
        (300, "Don't compute and drive; the life you save may be your own."),
        (400, "Chuck Norris can spawn threads that complete before they are started."),
        (500, "Quel Pokemon a une mitraillette? Ratatatatatatatatata"),
        (
            600,
            "Ci sono 10 tipi di persone: quelli che comprendono l'esadecimale e altri 15.",
        ),
        (
            700,
            "Chuck Norris potrebbe usare qualsiasi cosa in java.util.* per ucciderti, inclusi i javadoc.",
        ),
        (800, "Ilość dni od ostatniej pomyłki o 1: 0."),
        (900, "Chuck Norris jest powodem Niebieskiego Ekranu Śmierci."),
        (
            952,
            "Tryck valfri tangent för att fortsätta eller någon annan tangent för att avsluta.",
        ),
    ],
)
def test_get_the_joke(joke_id: int, joke_text: str) -> None:
    """Get a specific joke"""
    with app.app_context():
        assert get_the_joke(joke_id).json["jokes"] == joke_text


@pytest.mark.parametrize(
    "joke_id, error_message",
    [
        (-1, "404 Not Found: Joke -1 not found, try an id between 0 and 952"),
        (999, "404 Not Found: Joke 999 not found, try an id between 0 and 952"),
    ],
)
def test_get_the_joke_error(joke_id: int, error_message: str) -> None:
    """There is a finite number of jokes"""
    with app.app_context():
        with pytest.raises(werkzeug.exceptions.NotFound) as excinfo:
            get_the_joke(joke_id)
        assert str(excinfo.value) == error_message


if __name__ == "__main__":
    pytest.main(["-v", __file__])
