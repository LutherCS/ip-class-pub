#!/usr/bin/env python3
"""Testing promises"""

import subprocess

from playwright.sync_api import Page


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/promises"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.http_server.terminate()


def test_retrieval(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.click("#getInfo")
    page.waitForLoadState("networkidle")
    allNumbers = page.querySelectorAll("#number_info > div")
    assert [x.querySelectorAll("div")[0].innerText() for x in allNumbers] == [
        "329",
        "330",
        "331",
    ]


def test_batch_retrieval(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.check("#batch")
    page.click("#getInfo")
    page.waitForLoadState("networkidle")
    allNumbers = page.querySelectorAll("#number_info > div")
    assert [x.querySelectorAll("div")[0].innerText() for x in allNumbers] == [
        "329",
        "330",
        "331",
    ]


def test_request(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.click("#getInfo")
    page.waitForResponse("http://numbersapi.com/*")
    allNumbers = page.querySelectorAll("#number_info > div")
    assert [x.querySelectorAll("div")[0].innerText() for x in allNumbers] == [
        "329",
    ]


def test_batch_request(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.check("#batch")
    page.click("#getInfo")
    page.waitForResponse("http://numbersapi.com/*")
    allNumbers = page.querySelectorAll("#number_info > div")
    assert [x.querySelectorAll("div")[0].innerText() for x in allNumbers] == [
        "329",
        "330",
        "331",
    ]
