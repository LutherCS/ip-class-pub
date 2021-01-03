#!/usr/bin/env python3
"""Using pytest-flask to test Flask app"""

import os
import subprocess
import pytest
from playwright.sync_api import Page


def setup_module(module):
    """Create the server fixture"""
    os.chdir("exercises/jokes")
    module.server = subprocess.Popen(["flask", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.server.terminate()


def test_click_button(page: Page):
    page.goto("http://localhost:5000/")
    page.click("#btnAmuse")
    assert len(page.querySelectorAll("#jokes > p")) == 1


@pytest.mark.parametrize("language", ["de", "en", "es"])
def test_select_language(page: Page, language):
    page.goto("http://localhost:5000/")
    page.selectOption("#selLang", language)
    page.click("#btnAmuse")
    assert len(page.querySelectorAll("#jokes > p")) == 1


@pytest.mark.parametrize("category", ["all", "chuck", "neutral"])
def test_select_category(page: Page, category):
    page.goto("http://localhost:5000/")
    page.selectOption("#selCat", category)
    page.click("#btnAmuse")
    assert len(page.querySelectorAll("#jokes > p")) == 1


def test_select_chuck_in_spanish(page: Page):
    page.goto("http://localhost:5000/")
    page.selectOption("#selCat", "chuck")
    page.selectOption("#sellang", "es")
    page.click("#btnAmuse")
    assert len(page.querySelectorAll("#jokes > p")) == 1


@pytest.mark.skip
@pytest.mark.parametrize("number", [1, 5, 10])
def test_select_number(page: Page, number):
    page.goto("http://localhost:5000/")
    page.selectOption("#selNum", str(number))
    page.click("#btnAmuse")
    assert len(page.querySelectorAll("#jokes > p")) == number


if __name__ == "__main__":
    pytest.main(["-v", "test_jokes_front.py"])
