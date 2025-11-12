#!/usr/bin/env python3
"""
Testing `geo` routes

@author: Roman Yasinovskyy
@version: 2025.11
"""

import pathlib
import sys
from importlib import util

import pytest

try:
    util.find_spec("exercises." + pathlib.Path(__file__).parts[-2])
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.geo.alex import create_app


@pytest.fixture(name="client", autouse=True)
def fixture_client():
    """Create the client fixture"""
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


@pytest.mark.parametrize(
    "route",
    [
        "/",
        "/region",
        "/subregion",
        "/country",
    ],
)
def test_get_top_routes(client, route: str) -> None:
    """GET should return 200 OK"""
    assert client.get(route).status_code == 200


@pytest.mark.parametrize(
    "region", ["Asia", "Europe", "Africa", "Oceania", "Americas", "Antarctica"]
)
def test_get_real_region(client, region: str) -> None:
    """GET should return 200 OK"""
    assert client.get(f"/region/{region}").status_code == 200


@pytest.mark.parametrize(
    "region",
    ["North America", "South America", "Australia and Oceania", "Eurasia"],
)
def test_get_fictional_region(client, region: str) -> None:
    """GET should return 404 Not Found"""
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
def test_get_real_subregion(client, subregion: str) -> None:
    """GET should return 200 OK"""
    assert client.get(f"/subregion/{subregion}").status_code == 200


@pytest.mark.parametrize(
    "subregion",
    ["Middle East", "Southeastern Asia", "Latin America"],
)
def test_get_fictional_subregion(client, subregion: str) -> None:
    """GET should return 404 Not Found"""
    assert client.get(f"/subregion/{subregion}").status_code == 404


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
def test_get_real_country(client, country: str) -> None:
    """GET should return 200 OK"""
    assert client.get(f"/country/{country}").status_code == 200


@pytest.mark.parametrize(
    "country",
    ["Aldovia", "Atlantis", "Wakanda"],
)
def test_get_fictional_country(client, country: str) -> None:
    """GET should return 404 Not Found"""
    assert client.get(f"/country/{country}").status_code == 404


if __name__ == "__main__":
    pytest.main(["-v", __file__])
