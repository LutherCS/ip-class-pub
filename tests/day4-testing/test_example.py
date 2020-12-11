#!/usr/bin/env python3
import subprocess

import pytest
from playwright.sync_api import Page 


def setup_module(module):
    http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory=notes/day4-testing/"]

    )
    module.pid = http_server.pid


def teardown_module(module):
    subprocess.Popen(["kill", "-9", f"{module.pid}"])


def test_example_is_working(page: Page):
    page.goto("http://localhost:8000/") 
    assert page.innerText("h1") == "Take a note!"


# def test_click_red_button(page: Page):
#     page.goto("http://localhost:8000/")
#     page.click("#btnRed")
#     assert page.querySelector("h1").getAttribute("style") == "color: red"


# def test_click_blue_button(page: Page):
#     page.goto("http://localhost:8000/")
#     page.click("#btnBlue")
#     assert page.querySelector("h1").getAttribute("style") == "color: blue"


@pytest.mark.parametrize("color", ["Red", "Blue"])
def test_click_paint_button(page: Page, color):
    page.goto("http://localhost:8000/")
    page.click(f"#btn{color}")
    assert page.querySelector("h1").getAttribute("style") == f"color: {color.lower()}"


def test_click_add_note_button(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#newNote", "Sample note")
    page.click("#btnAddNote")
    assert len(page.querySelectorAll("div[id='allNotes'] > p")) == 1
    page.fill("#newNote", "Another note")
    page.click("#btnAddNote")
    assert len(page.querySelectorAll("div[id='allNotes'] > p")) == 2
