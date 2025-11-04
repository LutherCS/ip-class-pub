#!/usr/bin/env python3
"""
Using playwright to test `jokes_api` client
This module does not use the backend and relies on mock responses

@author: Roman Yasinovskyy
@version: 2025.11
"""

import json
import pathlib
import subprocess
from itertools import product

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)
APP_URL = "http://localhost:8000/"


@pytest.fixture(scope="module", autouse=True)
def frontend_server():
    """Set up front-end server"""
    server = subprocess.Popen(["python3", "-m", "http.server", "-d", "projects/jokes_api/client"])
    try:
        server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass
    yield
    server.terminate()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.route(
        "https://cdn.jsdelivr.net/**",
        lambda route: route.abort(),
    )
    page.goto(APP_URL)
    yield


def test_get_all_jokes(page: Page) -> None:
    """Clicking a button without selecting any category/language
    should return all jokes in any language/category"""
    page.route(
        "**/any/any/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * 953)])),
        ),
    )
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(953)


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
def test_get_all_jokes_by_language(page: Page, language: str, expected: int) -> None:
    """The is a limited number of jokes in each language"""
    page.route(
        f"**/{language}/any/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * expected)])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", "any")
    page.select_option("#selNum", "all")
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(expected)


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
def test_get_neutral_jokes_by_language(page: Page, language: str, expected: int) -> None:
    """The is a limited number of neutral jokes in each language"""
    page.route(
        f"**/{language}/neutral/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * expected)])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", "neutral")
    page.select_option("#selNum", "all")
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(expected)


@pytest.mark.parametrize(
    "language, expected",
    [
        ("any", 386),
        ("cs", 12),
        ("de", 68),
        ("en", 103),
        ("es", 16),
        ("eu", 1),
        ("fr", 1),
        ("gl", 1),
        ("hu", 1),
        ("it", 87),
        ("lt", 1),
        ("pl", 99),
        ("sv", 1),
    ],
)
def test_get_chuck_jokes_by_language(page: Page, language: str, expected: int) -> None:
    """The is a limited number of chuck jokes in each language"""
    page.route(
        f"**/{language}/chuck/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * expected)])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", "chuck")
    page.select_option("#selNum", "all")
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(expected)


@pytest.mark.parametrize(
    "category, expected",
    [
        ("neutral", 567),
        ("chuck", 386),
    ],
)
def test_get_jokes_by_category(page: Page, category: str, expected: int) -> None:
    """The is a limited number of jokes in each category"""
    page.route(
        f"**/any/{category}/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * expected)])),
        ),
    )

    page.select_option("#selLang", "any")
    page.select_option("#selCat", category)
    page.select_option("#selNum", "all")
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(expected)


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
def test_get_chuck_error(page: Page, language: str) -> None:
    """There are no jokes about Chuck Norris in some languages"""
    page.route(
        f"**/{language}/chuck/all",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", [])])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", "chuck")
    page.click("#btnAmuse")
    expect(page.get_by_role("article").first).to_contain_text(
        "There are no jokes in the chosen combination of languages and categories"
    )


@pytest.mark.parametrize(
    "language, category, number",
    product(
        ["any", "cs", "de", "en", "es", "it", "pl"],
        ["any", "chuck", "neutral"],
        [1, 5, 10],
    ),
)
def test_get_n_jokes(page: Page, language: str, category: str, number: int) -> None:
    """Some combinations of language/category return the requested number of jokes"""
    page.route(
        f"**/{language}/{category}/{number}",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * number)])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(number)


@pytest.mark.parametrize(
    "language, category, number",
    product(
        ["eu", "fr", "gl", "hu", "lt", "sv"],
        ["any", "neutral"],
        range(1, 3),
    ),
)
def test_get_fewer_jokes(page: Page, language: str, category: str, number: int) -> None:
    """Some combinations of language/category return fewer than the requested number of jokes"""
    page.route(
        f"**/{language}/{category}/{number}",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("jokes", ["Lorem ipsum dolor sit amet."] * number)])),
        ),
    )

    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(number)


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
def test_get_the_joke_by_id(page: Page, joke_id: int, joke_text: str) -> None:
    """Get a specific joke"""
    page.route(
        f"**/{joke_id}",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(dict([("joke", joke_text)])),
        ),
    )

    page.fill("#jokeId", str(joke_id))
    page.click("#btnAmuse")
    expect(page.get_by_role("article").first).to_contain_text(joke_text)


@pytest.mark.parametrize(
    "joke_id, error_message",
    [
        (999, "404 Not Found: Joke 999 not found, try an id between 0 and 952"),
    ],
)
def test_get_the_joke_by_id_error(page: Page, joke_id: int, error_message: str) -> None:
    """There is a finite number of jokes"""
    page.route(
        f"**/{joke_id}",
        lambda route: route.fulfill(
            status=404,
            content_type="application/json",
            body=json.dumps(dict([("error", error_message)])),
        ),
    )
    page.fill("#jokeId", str(joke_id))
    page.click("#btnAmuse")
    expect(page.get_by_role("article").first).to_contain_text(error_message)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
