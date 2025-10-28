#!/usr/bin/env python3
"""
Using pytest-playwright to test the front end

@authors: Roman Yasinovskyy
@version: 2025.10
"""

import os
import subprocess
from itertools import product

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)


@pytest.fixture(scope="module", autouse=True)
def server():
    """Create the server fixture"""
    os.chdir("exercises/jokes")
    server = subprocess.Popen(["flask", "run"])
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
    page.goto("http://localhost:5000/")


def test_click_button(page: Page) -> None:
    """Click a button without making any changes to the default selection"""
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(1)


@pytest.mark.parametrize(
    "language, category",
    product(
        ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "sv"],
        ["all", "chuck", "neutral"],
    ),
)
def test_get_a_joke(page: Page, language: str, category: str) -> None:
    """Various combinations of language/category should be handled and return a single joke"""
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(1)


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
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(number)


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
    page.select_option("#selLang", language)
    page.select_option("#selCat", category)
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(number)


@pytest.mark.parametrize(
    "language",
    ["eu", "fr", "gl", "lt", "sv"],
)
def test_get_chuck_error(page: Page, language: str) -> None:
    """There are no jokes about Chuck Norris in some languages"""
    page.select_option("#selLang", language)
    page.select_option("#selCat", "chuck")
    page.click("#btnAmuse")
    expect(page.get_by_role("article")).to_have_count(1)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
