#!/usr/bin/env python3
"""
Test the routes

@authors: Roman Yasinovskyy
@version: 2025.12
"""

import pathlib
import sys
from importlib import util

import pytest

try:
    util.find_spec("exercises." + pathlib.Path(__file__).parts[-2], "authorization")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.authorization.panda import create_app


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_main_route(client) -> None:
    """GET should work"""
    assert client.get("/").status_code == 200


def test_auth_login(client) -> None:
    """GET should redirect"""
    assert client.get("/auth/login").status_code == 302


def test_auth_logout(client) -> None:
    """GET should redirect"""
    assert client.get("/auth/logout").status_code == 302


if __name__ == "__main__":
    pytest.main(["-v", __file__])
