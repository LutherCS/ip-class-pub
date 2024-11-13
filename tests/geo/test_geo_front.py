#!/usr/bin/env python3
"""
Testing `geo` frontend

@authors: Roman Yasinovskyy
@version: 2024.11
"""

import os
import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


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


@pytest.mark.parametrize(
    "country, capital",
    [
        ("Madagascar", "Antananarivo"),
        ("Côte d'Ivoire", "Yamoussoukro"),
        ("Réunion", "Saint-Denis"),
        ("Ukraine", "Kyiv"),
        ("United States", "Washington"),
        ("Tokelau", ""),
        ("Antarctica", ""),
        ("Bouvet Island", ""),
        ("Cocos (Keeling) Islands", ""),
        ("French Southern and Antarctic Lands", ""),
        ("Heard Island and McDonald Islands", ""),
    ],
)
def test_country(page: Page, country, capital):
    """Retrieve country information"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/country")
    page.select_option("#selCountry", country)
    page.click("#btnInfo")
    page.wait_for_selector("#information > tbody > tr")
    assert len(page.query_selector_all("#information > tbody > tr")) == 1
    assert (
        page.query_selector_all("#information > tbody > tr > td")[1].inner_text()
        == capital
    )


@pytest.mark.parametrize(
    "region, countries",
    [
        ("Africa", 59),
        ("Americas", 56),
        ("Antarctica", 5),
        ("Asia", 50),
        ("Europe", 53),
        ("Oceania", 27),
    ],
)
def test_region(page: Page, region: str, countries: int) -> None:
    """Retrieve region information"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/region")
    page.select_option("#selRegion", region)
    page.click("#btnInfo")
    page.wait_for_selector("#information > tbody > tr")
    assert len(page.query_selector_all("#information > tbody > tr")) == countries


@pytest.mark.parametrize(
    "subregion, countries",
    [
        ("Australia and New Zealand", 5),
        ("Caribbean", 28),
        ("Central America", 7),
        ("Central Asia", 5),
        ("Eastern Africa", 21),
        ("Eastern Asia", 8),
        ("Eastern Europe", 10),
        ("Melanesia", 5),
        ("Micronesia", 7),
        ("Middle Africa", 9),
        ("Northern Africa", 7),
        ("Northern America", 7),
        ("Northern Europe", 16),
        ("Polynesia", 10),
        ("South America", 14),
        ("South-eastern Asia", 11),
        ("Southern Africa", 5),
        ("Southern Asia", 9),
        ("Southern Europe", 18),
        ("Western Africa", 17),
        ("Western Asia", 17),
        ("Western Europe", 9),
    ],
)
def test_subregion(page: Page, subregion: str, countries: int) -> None:
    """Retrieve subregion information"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/subregion")
    page.select_option("#selSubregion", subregion)
    page.click("#btnInfo")
    page.wait_for_selector("#information > tbody > tr")
    assert len(page.query_selector_all("#information > tbody > tr")) == countries


if __name__ == "__main__":
    pytest.main(["-v", __file__])
