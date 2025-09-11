#!/usr/bin/env python3
"""
Testing primes

@authors: Roman Yasinovskyy
@version: 2025.9
"""

import subprocess
from math import ceil
from random import randint

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/primes"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.http_server.terminate()


@pytest.mark.parametrize(
    "name, greeting",
    [
        ("Wu", "Hello, Wu"),
        ("Garmadon", "Hello, Garmadon"),
        ("Misako", "Hello, Misako"),
        ("Lloyd", "Hello, Lloyd"),
    ],
)
def test_case_1_greeting(page: Page, name: str, greeting: str):
    page.goto(f"http://localhost:8000/index.html?name={name}&number=3")
    expect(page.locator("#greeting")).to_have_text(greeting)


@pytest.mark.parametrize(
    "number, result",
    [
        (1, "1 is not a prime number"),
        (2, "2 is a prime number"),
        (3, "3 is a prime number"),
        (4, "4 is not a prime number"),
    ],
)
def test_case_1_number(page: Page, number: int, result: str):
    page.goto(f"http://localhost:8000/index.html?name=Lloyd&number={number}")
    expect(page.locator("#numberInfo")).to_have_text(result)


@pytest.mark.parametrize("number", [randint(100, 1000) for _ in range(4)])
def test_case_1_table(page: Page, number):
    page.goto(f"http://localhost:8000/index.html?name=Lloyd&number={number}")
    expect(page.locator("table[id='nPrimes'] > tbody > tr")).to_have_count(
        ceil(number / 10)
    )


@pytest.mark.parametrize(
    "name, greeting",
    [
        ("Wu", "Hello, Wu"),
        ("Garmadon", "Hello, Garmadon"),
        ("Misako", "Hello, Misako"),
        ("Lloyd", "Hello, Lloyd"),
    ],
)
def test_case_2_greeting(page: Page, name: str, greeting: str):
    page.goto(f"http://localhost:8000/index.html?name={name}")
    expect(page.locator("#greeting")).to_have_text(greeting)


def test_case_2_number(page: Page):
    page.goto("http://localhost:8000/index.html?name=Lloyd")
    expect(page.locator("#numberInfo")).to_have_text("330 is not a prime number")


def test_case_2_table(page: Page):
    page.goto("http://localhost:8000/index.html?name=Lloyd")
    expect(page.locator("table[id='nPrimes'] > tbody > tr")).to_have_count(33)


def test_case_3_greeting(page: Page):
    page.goto("http://localhost:8000/index.html?number=42")
    expect(page.locator("#greeting")).to_have_text("Hello, student")


@pytest.mark.parametrize(
    "number, result",
    [
        (1, "1 is not a prime number"),
        (2, "2 is a prime number"),
        (3, "3 is a prime number"),
        (4, "4 is not a prime number"),
    ],
)
def test_case_3_number(page: Page, number: int, result: str):
    page.goto(f"http://localhost:8000/index.html?number={number}")
    expect(page.locator("#numberInfo")).to_have_text(result)


@pytest.mark.parametrize("number", [randint(100, 1000) for _ in range(4)])
def test_case_3_table(page: Page, number):
    page.goto(f"http://localhost:8000/index.html?number={number}")
    expect(page.locator("table[id='nPrimes'] > tbody > tr")).to_have_count(
        ceil(number / 10)
    )


def test_case_4_greeting(page: Page):
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("#greeting")).to_have_text("Hello, student")


def test_case_4_number(page: Page):
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("#numberInfo")).to_have_text("330 is not a prime number")


def test_case_4_table(page: Page):
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("table[id='nPrimes'] > tbody > tr")).to_have_count(33)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
