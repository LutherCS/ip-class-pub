#!/usr/bin/env python3
"""
Using pytest-playwright to test the front end

@authors: Roman Yasinovskyy
@version: 2022.10
"""

import os
import subprocess

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


def test_click_button(page: Page):
    """Click a button without selecting any category/language"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize("language", ["de", "en", "es"])
def test_select_language(page: Page, language):
    """Select different languages"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#selLang", language)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize("category", ["all", "chuck", "neutral"])
def test_select_category(page: Page, category):
    """Select different categories"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#selCat", category)
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > p")) == 1


def test_select_chuck_in_spanish(page: Page):
    """There are no jokes about Chuck Norris in Spanish"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#selCat", "chuck")
    page.select_option("#selLang", "es")
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize("number", [1, 5, 10])
def test_select_number(page: Page, number):
    """Select different number of jokes"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#selNum", str(number))
    page.click("#btnAmuse")
    assert len(page.query_selector_all("#jokes > p")) == number


if __name__ == "__main__":
    pytest.main(["-v", __file__])
