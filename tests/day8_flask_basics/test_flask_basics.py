#!/usr/bin/env python3
"""Using pytest-flask to test Flask app"""


import pytest
from notes.day8_flask_basics.hello import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.mark.parametrize(
    "path",
    [
        "/",
        "/number/330",
        "/number/one",
        "/greet/Winnie",
        "/try",
    ],
)
def test_status_200(client, path):
    """Some routes should work and return 200 OK"""
    assert client.get(path).status_code == 200


def test_status_404(client):
    """Some routes should return a valid 404 Not Found"""
    assert client.get("/foo").status_code == 404


def test_hello_world(client):
    """Testing default route"""
    assert client.get("/").data.decode() == "Hello, World"


@pytest.mark.parametrize("num", [10, 330])
def test_generate_number(client, num):
    """Testing the number route"""
    assert "prime number" in client.get(f"/number/{num}").data.decode()


def test_generate_number_warning(client):
    """Testing the number sink"""
    assert client.get("/number/one").data.decode() == "one is not even a number!"


@pytest.mark.parametrize("name", ["Winnie", "Piglet", "Kanga"])
def test_hello_user(client, name):
    """Testing the individualized greeting"""
    assert (
        client.get(f"/greet/{name}").data.decode() == f"Hello, <strong>{name}</strong>"
    )


def test_hello(client):
    """Testing if the returned html contains `form`"""
    assert "form" in client.get("/try").data.decode()


@pytest.mark.parametrize("name", ["Winnie", "Piglet", "Kanga"])
def test_hello_with_args(client, name):
    assert (
        client.get(f"/try?firstname={name}").data.decode()
        == f"Hello, <strong>{name}</strong>"
    )


if __name__ == "__main__":
    pytest.main(["-v", "test_flask_basics.py"])
