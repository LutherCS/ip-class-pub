#!/usr/bin/env python3
"""
Testing notebook

@authors: Roman Yasinovskyy
@version: 2025.9
"""

import random
import string
import subprocess

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)


def setup_module(module):
    """Set up"""
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "projects/notebook"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Tear down"""
    module.http_server.terminate()


def test_no_title_no_text(page: Page):
    """Button clicked without title or text"""
    page.goto("http://localhost:8000/")
    page.click("#addNote")
    for p in page.locator(".field p").all():
        expect(p).not_to_have_class("is-hidden")


def test_title_no_text(page: Page):
    """Text not provided"""
    page.goto("http://localhost:8000/")
    page.fill("#title", "Note title")
    page.click("#addNote")
    expect(page.locator("#fieldText p")).not_to_have_class("is-hidden")


def test_text_no_title(page: Page):
    """Title not provided"""
    page.goto("http://localhost:8000/")
    page.fill("#text", "Lorem ipsum")
    page.click("#addNote")
    expect(page.locator("#fieldTitle p")).not_to_have_class("is-hidden")


@pytest.mark.parametrize("n", [1, 3, 8, 21, 55])
def test_addition(page: Page, n: int):
    """Adding notes"""
    page.goto("http://localhost:8000/")
    for _ in range(n):
        title = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
        page.fill("#title", title)
        text = " ".join(
            [
                "".join([random.choice(string.ascii_letters) for _ in range(random.randint(3, 10))])
                for _ in range(random.randint(10, 20))
            ]
        )
        page.fill("#text", text)
        page.click("#addNote")
    expect(page.locator(".note")).to_have_count(n)


@pytest.mark.parametrize("to_add, to_remove", [(1, 1), (2, 2), (2, 1), (8, 5), (13, 8)])
def test_removal(page: Page, to_add: int, to_remove: int):
    """Removing notes"""
    page.goto("http://localhost:8000/")
    for _ in range(to_add):
        page.fill("#title", "Lorem ipsum")
        page.fill("#text", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        page.click("#addNote")
    for _ in range(to_remove):
        page.locator(".deleteNote").all()[0].click()
    expect(page.locator(".note")).to_have_count(to_add - to_remove)


@pytest.mark.parametrize("n", [1, 3, 8, 21, 55])
def test_storage(page: Page, n: int):
    """Keeping notes"""
    page.goto("http://localhost:8000/")
    for _ in range(n):
        page.fill("#title", "Lorem ipsum")
        page.fill("#text", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        page.click("#addNote")
    page.reload()
    expect(page.locator(".note")).to_have_count(n)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
