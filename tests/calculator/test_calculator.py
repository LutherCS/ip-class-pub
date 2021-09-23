#!/usr/bin/env python3
"""Testing todo_list"""

import subprocess

import pytest
from playwright.sync_api import Page


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "projects/calculator"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.http_server.terminate()


def test_eval(page: Page):
    page.goto("http://localhost:8000/calculator.html")
    page.click("#btnEql")
    # page.screenshot(path=f"boo.png")
    assert page.query_selector("#result").inner_text() == "0"


def test_clear(page: Page):
    page.goto("http://localhost:8000/calculator.html")
    page.click("#btn1")
    page.click("#btnClr")
    assert page.query_selector("#result").inner_text() == "0"


def test_error(page: Page):
    page.goto("http://localhost:8000/calculator.html")
    page.click("#btn1")
    page.click("#btnSum")
    page.click("#btnSum")
    page.click("#btn2")
    page.click("#btnEql")
    assert page.query_selector("#result").inner_text() == "ERROR"


def test_infinity(page: Page):
    page.goto("http://localhost:8000/calculator.html")
    page.click("#btn1")
    page.click("#btnDiv")
    page.click("#btn0")
    page.click("#btnEql")
    assert page.query_selector("#result").inner_text() == "Infinity"


@pytest.mark.parametrize(
    "buttons, result",
    [
        ([1, 2, "Sum", 3, 4, "Eql"], 46),
        ([4, 5, "Sub", 5, 6, "Eql"], -11),
        ([6, 7, "Mul", 8, 9, "Eql"], 5963),
        ([9, 0, "Div", 1, 0, "Eql"], 9),
    ],
)
def test_integer_operations(page: Page, buttons, result):
    page.goto("http://localhost:8000/calculator.html")
    for btn in buttons:
        page.click(f"#btn{btn}")
    assert int(page.query_selector("#result").inner_text()) == result


@pytest.mark.parametrize(
    "buttons, result",
    [
        ([1, "Dot", 2, "Sum", 3, "Dot", 4, "Eql"], 4.6),
        ([4, "Dot", 5, "Sub", 5, "Dot", 6, "Eql"], -1.1),
        ([6, "Dot", 7, "Mul", 8, "Dot", 9, "Eql"], 59.63),
        ([1, "Dot", 0, "Div", 9, "Dot", 0, "Eql"], 0.1111),
    ],
)
def test_floating_point_operations(page: Page, buttons, result):
    page.goto("http://localhost:8000/calculator.html")
    for btn in buttons:
        page.click(f"#btn{btn}")
    assert float(page.query_selector("#result").inner_text()) == pytest.approx(
        result, 0.001
    )
