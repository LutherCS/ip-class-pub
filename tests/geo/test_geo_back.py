#!/usr/bin/env python3
"""Using pytest-flask to test Flask app"""

import pytest
from exercises.geo.app import app, get_data_from_db


@pytest.fixture
def client():
    """Create the client fixture"""
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.mark.parametrize(
    "query, results",
    [
        ("select * from country;", 239),
        ("select * from country where region='Eastern Africa';", 20),
        ("select * from country where region='Eastern Asia';", 8),
        ("select * from country where region='Eastern Europe';", 10),
        ("select * from country where continent='Asia';", 51),
        ("select * from country where continent='Europe';", 46),
        ("select * from country where continent='North America';", 37),
        ("select * from country where continent='Africa';", 58),
        ("select * from country where continent='Oceania';", 28),
        ("select * from country where continent='South America';", 14),
        ("select * from country where continent='Antarctica';", 5),
    ],
)
def test_db(query, results):
    """Querying the database"""
    assert len(get_data_from_db(query)) == results


def test_index_get(client):
    """GET should work"""
    assert client.get("/").status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", "test_geo.py"])
