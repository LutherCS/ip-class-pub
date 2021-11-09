#!/usr/bin/env python3
"""Using pytest-flask to test Flask app"""

import os
import subprocess
import pytest
from playwright.sync_api import Page


def setup_module(module):
    """Create the server fixture"""
    os.chdir("exercises/geo")
    module.server = subprocess.Popen(["flask", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.server.terminate()


@pytest.mark.parametrize("country", ["USA", "UKR", "MDG"])
def test_country(page: Page, country):
    page.goto("http://localhost:5000/country")
    page.select_option("#selCountry", country)
    page.click("#btnInfo")
    assert len(page.query_selector_all("#information > tbody > tr")) == 1


@pytest.mark.parametrize(
    "region, countries",
    [("Caribbean", 24), ("Middle East", 18), ("Eastern Europe", 10)],
)
def test_region(page: Page, region, countries):
    page.goto("http://localhost:5000/region")
    page.select_option("#selRegion", region)
    page.click("#btnInfo")
    assert len(page.query_selector_all("#information > tbody > tr")) == countries


@pytest.mark.parametrize(
    "continent, countries", [("Oceania", 27), ("South America", 14)]
)
def test_continent(page: Page, continent, countries):
    page.goto("http://localhost:5000/continent")
    page.select_option("#selContinent", continent)
    page.click("#btnInfo")
    assert len(page.query_selector_all("#information > tbody > tr")) == countries


if __name__ == "__main__":
    pytest.main(["-v", __file__])
