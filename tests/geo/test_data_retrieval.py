#!/usr/bin/env python3
"""
Testing `geo` data retrieval

@author: Roman Yasinovskyy
@version: 2025.11
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
    from exercises.geo.alex import create_app
    from exercises.geo.alex.retrieval import get_data_from_db


@pytest.fixture(name="app", autouse=True)
def fixture_app():
    """Create the client fixture"""
    app = create_app()
    with app.test_client() as this_app:
        with app.app_context():
            yield this_app


@pytest.mark.parametrize(
    "query, results",
    [
        ("select * from country;", 250),
        ("select * from city;", 3821),
        ("select * from country join city on country.capital=city.id;", 244),
        ("select distinct continental_region from country;", 6),
        ("select distinct subregion from country;", 23),
    ],
)
def test_query_all(query: str, results: int) -> None:
    """Retrieve all record with minor filtering"""
    assert len(get_data_from_db(query)) == results


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
def test_query_real_region(name: str, results: int):
    """Retrieve specific continental region"""
    query = "select * from country where continental_region=?;"
    assert len(get_data_from_db(query, (name,))) == results


@pytest.mark.parametrize(
    "name",
    [
        "North America",
        "South America",
        "Eurasia",
        "Australia and Oceania",
    ],
)
def test_query_fictional_region(name: str):
    """Should not crash while retrieving fictinoal continental region"""
    query = "select * from country where continental_region=?;"
    assert len(get_data_from_db(query, (name,))) == 0


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
def test_query_real_subregion(name: str, results: int) -> None:
    """Retrieve specific subregion"""
    query = "select * from country where subregion=?;"
    assert len(get_data_from_db(query, (name,))) == results


@pytest.mark.parametrize(
    "name",
    [
        "Middle East",
        "Southeastern Asia",
        "Latin America",
    ],
)
def test_query_fictional_subregion(name: str):
    """Should not crash while retrieving fictinoal subregion"""
    query = "select * from country where subregion=?;"
    assert len(get_data_from_db(query, (name,))) == 0


@pytest.mark.parametrize(
    "name, results",
    [
        ("Antarctica", 1),
        ("Bouvet Island", 1),
        ("Cocos (Keeling) Islands", 1),
        ("French Southern and Antarctic Lands", 1),
        ("Heard Island and McDonald Islands", 1),
        ("Tokelau", 1),
        ("United States", 1),
    ],
)
def test_query_real_country(name: str, results: int) -> None:
    """Read specific countries"""
    query = "select * from country where name=?;"
    assert len(get_data_from_db(query, (name,))) == results


@pytest.mark.parametrize(
    "name, results",
    [
        ("Aldovia", 0),
        ("Wakanda", 0),
        ("United States of America", 0),
    ],
)
def test_query_fictional_country(name: str, results: int) -> None:
    """Read specific countries"""
    query = "select * from country where name=?;"
    assert len(get_data_from_db(query, (name,))) == results


if __name__ == "__main__":
    pytest.main(["-v", __file__])
