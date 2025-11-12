#!/usr/bin/env python3
"""
Testing `geo` user interface

@author: Roman Yasinovskyy
@version: 2025.11
"""

import os
import subprocess

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)
APP_URL = "http://localhost:5000"


def setup_module(module):
    """Create the server fixture"""
    os.chdir("exercises/geo")
    module.server = subprocess.Popen(["flask", "--app", "alex", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.server.terminate()


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.route(
        "https://cdn.jsdelivr.net/**",
        lambda route: route.fulfill(status=404),
    )
    yield


def test_world(page: Page) -> None:
    """Retrieve region information"""
    page.goto(f"{APP_URL}")
    expect(page.locator("main > h2")).to_contain_text("250 countries and territories of the world")
    expect(page.locator("#information > tbody > tr")).to_have_count(250)


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
    page.goto(f"{APP_URL}/region")
    page.select_option("#selRegion", region)
    page.click("#btnInfo")
    expect(page.locator("main > h2")).to_contain_text(
        f"{countries} countries and territories of {region}"
    )
    expect(page.locator("#information > tbody > tr")).to_have_count(countries)


@pytest.mark.parametrize(
    "name",
    [
        "North America",
        "South America",
        "Eurasia",
        "Australia and Oceania",
    ],
)
def test_region_error(page: Page, name: str) -> None:
    """Fail to retrieve region information"""
    page.goto(f"{APP_URL}/region/{name}")
    expect(page.locator("article.message")).to_have_count(1)


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
    page.goto(f"{APP_URL}/subregion")
    page.select_option("#selSubregion", subregion)
    page.click("#btnInfo")
    expect(page.locator("main > h2")).to_contain_text(
        f"{countries} countries and territories of {subregion}"
    )
    expect(page.locator("#information > tbody > tr")).to_have_count(countries)


@pytest.mark.parametrize(
    "name",
    [
        "Middle East",
        "Southeastern Asia",
        "Latin America",
    ],
)
def test_subregion_error(page: Page, name: str) -> None:
    """Fail to retrieve subregion information"""
    page.goto(f"{APP_URL}/subregion/{name}")
    expect(page.locator("article.message")).to_have_count(1)


@pytest.mark.parametrize(
    "country, cities, capital",
    [
        ("Côte d'Ivoire", 14, "Yamoussoukro"),
        ("Madagascar", 10, "Antananarivo"),
        ("Réunion", 2, "Saint-Denis"),
        ("Ukraine", 25, "Kyiv"),
        ("United States", 182, "Washington"),
    ],
)
def test_country(page: Page, country: str, cities: int, capital: str):
    """Retrieve country information"""
    page.goto(f"{APP_URL}/country")
    page.select_option("#selCountry", country)
    page.click("#btnInfo")
    expect(page.locator("main > h2")).to_contain_text(f"{cities} cities of {country}")
    expect(page.locator("#information > tbody > tr")).to_have_count(cities)
    expect(page.locator("#information > tbody > tr.is-selected")).to_contain_text(capital)


@pytest.mark.parametrize(
    "country",
    [
        "Antarctica",
        "Bouvet Island",
        "Cocos (Keeling) Islands",
        "French Southern and Antarctic Lands",
        "Heard Island and McDonald Islands",
        "Tokelau",
    ],
)
def test_country_with_no_cities(page: Page, country: str):
    """Retrieve country information"""
    page.goto(f"{APP_URL}/country")
    page.select_option("#selCountry", country)
    page.click("#btnInfo")
    expect(page.locator("main > p")).to_contain_text("No cities found in this country.")


@pytest.mark.parametrize(
    "name",
    [
        "Aldovia",
        "Wakanda",
        "United States of America",
    ],
)
def test_country_error(page: Page, name: str) -> None:
    """Fail to retrieve country information"""
    page.goto(f"{APP_URL}/country/{name}")
    expect(page.locator("article.message")).to_have_count(1)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
