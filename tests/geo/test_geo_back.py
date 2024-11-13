#!/usr/bin/env python3
"""
Testing `geo` backend

@authors: Roman Yasinovskyy
@version: 2024.11
"""

import pathlib
import sys
from importlib import util

import pytest

try:
    util.find_spec("exercises." + pathlib.Path(__file__).parts[-2], "geo")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.geo.app import app, get_data_from_db


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    with app.test_client() as the_client:
        with app.app_context():
            yield the_client


@pytest.mark.parametrize(
    "route",
    [
        "/",
        "/country",
        "/region",
        "/subregion",
    ],
)
def test_http_get(client, route: str) -> None:
    """GET should work"""
    assert client.get(route).status_code == 200


@pytest.mark.parametrize(
    "country",
    [
        "Albania",
        "Bouvet Island",
        "Chad",
        "Côte d'Ivoire",
        "Heard Island and McDonald Islands",
        "Tokelau",
        "United States",
        "Ukraine",
    ],
)
def test_http_get_country(client, country: str) -> None:
    """GET should work"""
    assert client.get(f"/country/{country}").status_code == 200


@pytest.mark.parametrize(
    "country",
    ["Aldovia", "Wakanda"],
)
def test_http_get_country_error(client, country: str) -> None:
    """GET should work"""
    assert client.get(f"/country/{country}").status_code == 404


@pytest.mark.parametrize(
    "region", ["Asia", "Europe", "Africa", "Oceania", "Americas", "Antarctica"]
)
def test_http_get_region(client, region: str) -> None:
    """GET should work"""
    assert client.get(f"/region/{region}").status_code == 200


@pytest.mark.parametrize(
    "region",
    ["North America", "South America", "Australia and Oceania", "Eurasia"],
)
def test_http_get_region_error(client, region: str) -> None:
    """GET should work"""
    assert client.get(f"/region/{region}").status_code == 404


@pytest.mark.parametrize(
    "subregion",
    [
        "Australia and New Zealand",
        "Caribbean",
        "Central America",
        "Central Asia",
        "Eastern Africa",
        "Eastern Asia",
        "Eastern Europe",
        "Melanesia",
        "Micronesia",
        "Middle Africa",
        "Northern Africa",
        "Northern America",
        "Northern Europe",
        "Polynesia",
        "South America",
        "South-eastern Asia",
        "Southern Africa",
        "Southern Asia",
        "Southern Europe",
        "Western Africa",
        "Western Asia",
        "Western Europe",
    ],
)
def test_http_get_subregion(client, subregion: str) -> None:
    """GET should work"""
    assert client.get(f"/subregion/{subregion}").status_code == 200


@pytest.mark.parametrize(
    "subregion",
    ["Middle East", "Southeastern Asia", "Latin America"],
)
def test_http_get_subregion_error(client, subregion: str) -> None:
    """GET should work"""
    assert client.get(f"/subregion/{subregion}").status_code == 404


@pytest.mark.parametrize(
    "query, results",
    [
        ("select country.name from country;", 250),
        ("select country.name from country join city on country.capital=city.id;", 244),
        ("select distinct continental_region from country;", 6),
        ("select distinct subregion from country where subregion is not null;", 22),
    ],
)
def test_query_all(query: str, results: int) -> None:
    """Read all countries"""
    assert len(get_data_from_db(query)) == results


@pytest.mark.parametrize(
    "name, results",
    [
        ("Aldovia", 0),
        ("Wakanda", 0),
        ("United States of America", 0),
        ("Tokelau", 1),
        ("Antarctica", 1),
        ("Bouvet Island", 1),
        ("Cocos (Keeling) Islands", 1),
        ("French Southern and Antarctic Lands", 1),
        ("Heard Island and McDonald Islands", 1),
        ("United States", 1),
    ],
)
def test_query_country(name: str, results: int) -> None:
    """Read specific countries"""
    query = "select * from country where name=?;"
    assert len(get_data_from_db(query, (name,))) == results


@pytest.mark.parametrize(
    "name, results",
    [
        ("Africa", 59),
        ("Americas", 56),
        ("Antarctica", 5),
        ("Asia", 50),
        ("Europe", 53),
        ("Oceania", 27),
    ],
)
def test_query_region(name, results):
    """Read specific continental region"""
    query = "select * from country where continental_region=?;"
    assert len(get_data_from_db(query, (name,))) == results


@pytest.mark.parametrize(
    "name, results",
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
def test_query_subregion(name: str, results: int) -> None:
    """Read specific subregion"""
    query = "select * from country where subregion=?;"
    assert len(get_data_from_db(query, (name,))) == results


if __name__ == "__main__":
    pytest.main(["-v", __file__])
