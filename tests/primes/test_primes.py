#!/usr/bin/env python3
"""
Testing JavaScript

@authors: Roman Yasinovskyy
@version: 2022.9
"""

import subprocess

import pytest
from playwright.sync_api import Page


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


def test_case_1_greeting(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman&number=3")
    assert page.query_selector("#greeting").inner_text() == "Hello Roman"


def test_case_1_number(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman&number=3")
    assert page.query_selector("#numberInfo").inner_text() == "3 is a prime number"


def test_case_1_table(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman&number=3")
    assert len(page.query_selector_all("table[id='nPrimes'] > tbody > tr")) == 3


def test_case_2_greeting(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert page.query_selector("#greeting").inner_text() == "Hello Roman"


def test_case_2_number(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert (
        page.query_selector("#numberInfo").inner_text() == "330 is not a prime number"
    )


def test_case_2_table(page: Page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert len(page.query_selector_all("table[id='nPrimes'] > tbody > tr")) == 330


def test_case_3_greeting(page: Page):
    page.goto("http://localhost:8000/primes.html?number=3")
    assert page.query_selector("#greeting").inner_text() == "Hello student"


def test_case_3_number(page: Page):
    page.goto("http://localhost:8000/primes.html?number=3")
    assert page.query_selector("#numberInfo").inner_text() == "3 is a prime number"


def test_case_3_table(page: Page):
    page.goto("http://localhost:8000/primes.html?number=3")
    assert len(page.query_selector_all("table[id='nPrimes'] > tbody > tr")) == 3


def test_case_4_greeting(page: Page):
    page.goto("http://localhost:8000/primes.html")
    assert page.query_selector("#greeting").inner_text() == "Hello student"


def test_case_4_number(page: Page):
    page.goto("http://localhost:8000/primes.html")
    assert (
        page.query_selector("#numberInfo").inner_text() == "330 is not a prime number"
    )


def test_case_4_table(page: Page):
    page.goto("http://localhost:8000/primes.html")
    assert len(page.query_selector_all("table[id='nPrimes'] > tbody > tr")) == 330


if __name__ == "__main__":
    pytest.main(["-v", __file__])
