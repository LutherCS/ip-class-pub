#!/usr/bin/env python3
"""
Test jokes_api server logic

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
    from projects.jokes_api.server.joker.logic import Joker


@pytest.fixture(name="joker", scope="module")
def fixture_joker():
    """Create the client fixture"""
    Joker.init_dataset()


def test_get_all_jokes(joker) -> None:
    """Get all the jokes in all available languages"""
    assert len(Joker.get_jokes()) == 953


@pytest.mark.parametrize(
    "language, expected",
    [
        ("any", 953),
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
def test_get_jokes_by_language(joker, language: str, expected: int) -> None:
    """The is a limited number of jokes in each language"""
    assert len(Joker.get_jokes(language=language, category="any")) == expected


@pytest.mark.parametrize(
    "language, expected",
    [
        ("any", 567),
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
def test_get_neutral_jokes_by_language(joker, language: str, expected: int) -> None:
    """The is a limited number of neutral jokes in each language"""
    assert len(Joker.get_jokes(language=language, category="neutral")) == expected


@pytest.mark.parametrize(
    "language, expected",
    [
        ("any", 386),
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
def test_get_chuck_jokes_by_language(joker, language: str, expected: int) -> None:
    """The is a limited number of chuck jokes in each language"""
    assert len(Joker.get_jokes(language=language, category="chuck")) == expected


@pytest.mark.parametrize(
    "category, expected",
    [
        ("neutral", 567),
        ("chuck", 386),
    ],
)
def test_get_jokes_by_category(joker, category: str, expected: int) -> None:
    """The is a limited number of chuck jokes in each language"""
    assert len(Joker.get_jokes(language="any", category=category)) == expected


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
def test_get_n_jokes(joker, language: str, category: str, number: int, expected: int) -> None:
    """The is a limited number of jokes in any language"""
    assert len(Joker.get_jokes(language, category, number)) == expected


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
def test_get_joke_by_id(joker, joke_id: int, joke_text: str) -> None:
    """Get a specific joke"""
    assert Joker.get_the_joke(joke_id).text == joke_text


@pytest.mark.parametrize(
    "language, error_message",
    [
        ("ru", "Language ru does not exist"),
        ("zxx", "Language zxx does not exist"),
    ],
)
def test_get_jokes_by_language_error(joker, language: int, error_message: str) -> None:
    """There are no jokes in some languages"""
    with pytest.raises(ValueError) as excinfo:
        Joker.get_jokes(language=language)
    assert str(excinfo.value) == error_message


@pytest.mark.parametrize(
    "category, error_message",
    [
        ("computer", "Category computer does not exist"),
        ("all", "Category all does not exist"),
    ],
)
def test_get_jokes_by_category_error(joker, category: int, error_message: str) -> None:
    """There are no jokes in some languages"""
    with pytest.raises(ValueError) as excinfo:
        Joker.get_jokes(category=category)
    assert str(excinfo.value) == error_message


@pytest.mark.parametrize(
    "joke_id, error_message",
    [
        (-1, "Joke -1 not found, try an id between 0 and 952"),
        (999, "Joke 999 not found, try an id between 0 and 952"),
    ],
)
def test_get_joke_by_id_error(joker, joke_id: int, error_message: str) -> None:
    """There is a finite number of jokes"""
    with pytest.raises(ValueError) as excinfo:
        Joker.get_the_joke(joke_id)
    assert str(excinfo.value) == error_message


if __name__ == "__main__":
    pytest.main(["-v", __file__])
