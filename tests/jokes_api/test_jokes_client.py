#!/usr/bin/env python3
"""
Using playwright to test `jokes_api` client

@authors: Roman Yasinovskyy
@version: 2024.11
"""

import os
import subprocess
from itertools import product

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000
APP_URL = "http://localhost:8000/"


def setup_module(module):
    """Set up servers"""
    # Create the front-end server fixture
    module.fserver = subprocess.Popen(
        ["python", "-m", "http.server", "-d", "projects/jokes_api/client"]
    )
    # Create the back-end server fixture
    os.chdir("projects/jokes_api/server")
    module.bserver = subprocess.Popen(["flask", "run"])
    try:
        module.fserver.wait(timeout=1)
        module.bserver.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.fserver.terminate()
    module.bserver.terminate()


def test_click_button(page: Page):
    """Click a button without selecting any category/language"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == 1


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
def test_get_all_jokes(page: Page, language: str, number: int) -> None:
    """The is a limited number of jokes in each language"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.select_option("#selCat", "all")
    page.select_option("#selLang", language)
    page.select_option("#selNum", "all")
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == number


@pytest.mark.parametrize(
    "language, category, number",
    product(
        ["cs", "de", "en", "es", "it", "pl"],
        ["all", "chuck", "neutral"],
        range(1, 10),
    ),
)
def test_get_n_jokes(page: Page, language: str, category: str, number: int) -> None:
    """Some combinations of language/category should return multiple jokes"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == number


@pytest.mark.parametrize(
    "language, category, number",
    product(
        ["eu", "fr", "gl", "hu", "lt", "sv"],
        ["all", "neutral"],
        range(1, 5),
    ),
)
def test_get_fewer_jokes(page: Page, language: str, category: str, number: int) -> None:
    """Test various combinations of languages, categories, and number of jokes"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.select_option("#selCat", category)
    page.select_option("#selLang", language)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == number


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
def test_get_chuck_error(page: Page, language: str) -> None:
    """There are no jokes about Chuck Norris in some languages"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.select_option("#selCat", "chuck")
    page.select_option("#selLang", language)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == 1


@pytest.mark.parametrize(
    "language, category",
    product(
        ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"],
        ["all", "chuck", "neutral"],
    ),
)
def test_get_a_joke(page: Page, language: str, category: str) -> None:
    """Various combinations of language/category should be handled and return a single joke"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == 1


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
def test_get_the_joke(page: Page, joke_id: int, joke_text: str) -> None:
    """Get a specific joke"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.fill("#jokeId", str(joke_id))
    page.click("#btnAmuse")
    assert page.query_selector_all("#jokes > article")[0].inner_text() == joke_text


@pytest.mark.parametrize(
    "joke_id, error_message",
    [
        (999, "404 Not Found: Joke 999 not found, try an id between 0 and 952"),
    ],
)
def test_get_the_joke_error(page: Page, joke_id: int, error_message: str) -> None:
    """There is a finite number of jokes"""
    page.set_default_timeout(TIMEOUT)
    page.goto(APP_URL)
    page.fill("#jokeId", str(joke_id))
    page.click("#btnAmuse")
    assert page.query_selector_all("#jokes > article")[0].inner_text() == error_message


if __name__ == "__main__":
    pytest.main(["-v", __file__])
