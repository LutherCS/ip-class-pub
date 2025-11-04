#!/usr/bin/env python3
"""
Test jokes_api server routes

@author: Roman Yasinovskyy
@version: 2025.11
"""

import pathlib
import sys
from importlib import util

import pytest

try:
    util.find_spec("projects." + pathlib.Path(__file__).parts[-2])
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from projects.jokes_api.server.joker import create_app


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_get_all_jokes_status(client) -> None:
    """There are jokes"""
    assert client.get("/api/v1/jokes/any/any/all").status_code == 200


def test_get_all_jokes_route(client) -> None:
    """There are jokes"""
    assert len(client.get("/api/v1/jokes/any/any/all").get_json().get("jokes")) == 953


@pytest.mark.parametrize(
    "language", ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"]
)
def test_get_jokes_by_language_status(client, language: str) -> None:
    """There are jokes in various languages"""
    assert client.get(f"/api/v1/jokes/{language}/any/all").status_code == 200


@pytest.mark.parametrize(
    "language, expected",
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
def test_get_jokes_by_language_route(client, language: str, expected: int) -> None:
    """There is a limited number of jokes in each language"""
    assert len(client.get(f"/api/v1/jokes/{language}/any/all").get_json().get("jokes")) == expected


@pytest.mark.parametrize(
    "language", ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"]
)
def test_get_neutral_jokes_by_language_status(client, language: str) -> None:
    """There are neutral jokes in various languages"""
    assert client.get(f"/api/v1/jokes/{language}/neutral/all").status_code == 200


@pytest.mark.parametrize(
    "language, expected",
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
def test_get_neutral_jokes_by_language_route(client, language: str, expected: int) -> None:
    """The is a limited number of neutral jokes in each language"""
    assert (
        len(client.get(f"/api/v1/jokes/{language}/neutral/all").get_json().get("jokes")) == expected
    )


@pytest.mark.parametrize(
    "language", ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"]
)
def test_get_chuck_jokes_by_language_status(client, language: str) -> None:
    """There are chuck jokes in some languages"""
    assert client.get(f"/api/v1/jokes/{language}/chuck/all").status_code == 200


@pytest.mark.parametrize(
    "language, expected",
    [
        ("cs", 12),
        ("de", 68),
        ("en", 103),
        ("es", 16),
        ("eu", 0),
        ("fr", 0),
        ("gl", 0),
        ("hu", 1),
        ("it", 87),
        ("lt", 0),
        ("pl", 99),
        ("sv", 0),
    ],
)
def test_get_chuck_jokes_by_language_route(client, language: str, expected: int) -> None:
    """The is a limited number of chuck jokes in some languages"""
    assert (
        len(client.get(f"/api/v1/jokes/{language}/chuck/all").get_json().get("jokes")) == expected
    )


@pytest.mark.parametrize("category", ["neutral", "chuck"])
def test_get_jokes_by_category_status(client, category: str) -> None:
    """There are chuck jokes in various languages"""
    assert client.get(f"/api/v1/jokes/any/{category}/all").status_code == 200


@pytest.mark.parametrize("category, expected", [("neutral", 567), ("chuck", 386)])
def test_get_jokes_by_category_route(client, category: str, expected: int) -> None:
    """The is a limited number of chuck jokes in each language"""
    assert len(client.get(f"/api/v1/jokes/any/{category}/all").get_json().get("jokes")) == expected


@pytest.mark.parametrize(
    "language, category, number, expected",
    [
        ("cs", "any", 33, 33),
        ("cs", "any", 330, 41),
        ("de", "any", 33, 33),
        ("de", "any", 330, 127),
        ("en", "any", 33, 33),
        ("en", "any", 330, 283),
        ("es", "any", 33, 33),
        ("es", "any", 330, 44),
        ("eu", "any", 3, 3),
        ("eu", "any", 330, 5),
        ("fr", "any", 3, 3),
        ("fr", "any", 330, 26),
        ("gl", "any", 3, 3),
        ("gl", "any", 330, 14),
        ("hu", "any", 3, 3),
        ("hu", "any", 330, 9),
        ("it", "any", 33, 33),
        ("it", "any", 330, 159),
        ("lt", "any", 3, 3),
        ("lt", "any", 330, 30),
        ("pl", "any", 33, 33),
        ("pl", "any", 330, 174),
        ("sv", "any", 33, 33),
        ("sv", "any", 330, 41),
    ],
)
def test_get_n_jokes_staus(
    client, language: str, category: str, number: int, expected: int
) -> None:
    """The is a limited number of jokes in any language"""
    assert client.get(f"/api/v1/jokes/{language}/{category}/{number}").status_code == 200


@pytest.mark.parametrize(
    "language, category, number, expected",
    [
        ("cs", "any", 33, 33),
        ("cs", "any", 330, 41),
        ("de", "any", 33, 33),
        ("de", "any", 330, 127),
        ("en", "any", 33, 33),
        ("en", "any", 330, 283),
        ("es", "any", 33, 33),
        ("es", "any", 330, 44),
        ("eu", "any", 3, 3),
        ("eu", "any", 330, 5),
        ("fr", "any", 3, 3),
        ("fr", "any", 330, 26),
        ("gl", "any", 3, 3),
        ("gl", "any", 330, 14),
        ("hu", "any", 3, 3),
        ("hu", "any", 330, 9),
        ("it", "any", 33, 33),
        ("it", "any", 330, 159),
        ("lt", "any", 3, 3),
        ("lt", "any", 330, 30),
        ("pl", "any", 33, 33),
        ("pl", "any", 330, 174),
        ("sv", "any", 33, 33),
        ("sv", "any", 330, 41),
    ],
)
def test_get_n_jokes_route(
    client, language: str, category: str, number: int, expected: int
) -> None:
    """The is a limited number of jokes in any language"""
    assert (
        len(client.get(f"/api/v1/jokes/{language}/{category}/{number}").get_json().get("jokes"))
        == expected
    )


@pytest.mark.parametrize("joke_id", [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 952])
def test_get_the_joke_status(client, joke_id: int) -> None:
    """Get a specific joke"""
    assert client.get(f"/api/v1/jokes/{joke_id}").status_code == 200


@pytest.mark.parametrize(
    "joke_id, joke_text",
    [
        (0, "Webmaster vyplňuje dotazník: Věk: 25 Výška: 185 Barva očí: #4040FF"),
        (
            100,
            "Chuck Norris streichelt keine Tiere, die Tiere streicheln sich selbst, wenn er in der Nähe ist",
        ),
        (200, "Why did Microsoft name their search engine BING? Because It's Not Google."),
        (300, "Don't compute and drive; the life you save may be your own."),
        (400, "Chuck Norris can spawn threads that complete before they are started."),
        (500, "Quel Pokemon a une mitraillette? Ratatatatatatatatata"),
        (600, "Ci sono 10 tipi di persone: quelli che comprendono l'esadecimale e altri 15."),
        (
            700,
            "Chuck Norris potrebbe usare qualsiasi cosa in java.util.* per ucciderti, inclusi i javadoc.",
        ),
        (800, "Ilość dni od ostatniej pomyłki o 1: 0."),
        (900, "Chuck Norris jest powodem Niebieskiego Ekranu Śmierci."),
        (952, "Tryck valfri tangent för att fortsätta eller någon annan tangent för att avsluta."),
    ],
)
def test_get_the_joke_route(client, joke_id: int, joke_text: str) -> None:
    """Get a specific joke"""
    assert client.get(f"/api/v1/jokes/{joke_id}").get_json().get("joke").get("text") == joke_text


@pytest.mark.parametrize("language", ["ru", "zxx"])
def test_get_jokes_by_language_error(client, language: str) -> None:
    """There are no jokes in some languages"""
    assert client.get(f"/api/v1/jokes/{language}/any/all").status_code == 404


@pytest.mark.parametrize("category", ["computer", "all"])
def test_get_jokes_by_category_error(client, category: str) -> None:
    """There are no jokes in some categories"""
    assert client.get(f"/api/v1/jokes/any/{category}/all").status_code == 404


@pytest.mark.parametrize("joke_id", [-1, 999])
def test_get_joke_by_id_error(client, joke_id: int) -> None:
    """There is a finite number of jokes"""
    assert client.get(f"/api/v1/jokes/{joke_id}").status_code == 404


if __name__ == "__main__":
    pytest.main(["-v", __file__])
