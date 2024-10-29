#!/usr/bin/env python3
"""
Using pytest-playwright to test the front end

@authors: Roman Yasinovskyy
@version: 2024.10
"""

import os
import subprocess
from itertools import product

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Create the server fixture"""
    os.chdir("exercises/jokes")
    module.server = subprocess.Popen(["flask", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.server.terminate()


def test_click_button(page: Page) -> None:
    """Click a button without making any changes to the default selection"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
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
    page.goto("http://localhost:5000/")
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == 1


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
    page.goto("http://localhost:5000/")
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
    page.goto("http://localhost:5000/")
    page.select_option("#selCat", category)
    page.select_option("#selLang", language)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == number


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
def test_get_jokes_error(page: Page, language: str) -> None:
    """There are no jokes about Chuck Norris in some languages"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#selCat", "chuck")
    page.select_option("#selLang", language)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > article")) == 1


if __name__ == "__main__":
    pytest.main(["-v", __file__])
