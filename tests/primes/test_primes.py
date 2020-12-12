#!/usr/bin/env python3
"""Testing JavaScript"""

import subprocess
from time import sleep


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


def test_case_1_greeting(page):
    page.goto("http://localhost:8000/primes.html?name=Roman&n=3")
    assert page.querySelector("#greeting").innerText() == "Hello Roman"


def test_case_1_n(page):
    page.goto("http://localhost:8000/primes.html?name=Roman&n=3")
    assert page.querySelector("#primeInfo").innerText() == "3 is a prime number"


def test_case_1_table(page):
    page.goto("http://localhost:8000/primes.html?name=Roman&n=3")
    assert len(page.querySelectorAll("table[id='nPrimes'] > tbody > tr")) == 3


def test_case_2_greeting(page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert page.querySelector("#greeting").innerText() == "Hello Roman"


def test_case_2_n(page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert page.querySelector("#primeInfo").innerText() == "330 is not a prime number"


def test_case_2_table(page):
    page.goto("http://localhost:8000/primes.html?name=Roman")
    assert len(page.querySelectorAll("table[id='nPrimes'] > tbody > tr")) == 330


def test_case_3_greeting(page):
    page.goto("http://localhost:8000/primes.html?n=3")
    assert page.querySelector("#greeting").innerText() == "Hello student"


def test_case_3_n(page):
    page.goto("http://localhost:8000/primes.html?n=3")
    assert page.querySelector("#primeInfo").innerText() == "3 is a prime number"


def test_case_3_table(page):
    page.goto("http://localhost:8000/primes.html?n=3")
    assert len(page.querySelectorAll("table[id='nPrimes'] > tbody > tr")) == 3


def test_case_4_greeting(page):
    page.goto("http://localhost:8000/primes.html")
    assert page.querySelector("#greeting").innerText() == "Hello student"


def test_case_4_n(page):
    page.goto("http://localhost:8000/primes.html")
    assert page.querySelector("#primeInfo").innerText() == "330 is not a prime number"


def test_case_4_table(page):
    page.goto("http://localhost:8000/primes.html")
    assert len(page.querySelectorAll("table[id='nPrimes'] > tbody > tr")) == 330
