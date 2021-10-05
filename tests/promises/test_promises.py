#!/usr/bin/env python3
"""Testing promises"""

import subprocess

import pytest
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
    page.wait_for_load_state("networkidle")
    all_numbers = page.query_selector_all("#number_info > div")
    assert [x.query_selector_all("div")[0].inner_text() for x in all_numbers] == [
        "329",
        "330",
        "331",
    ]


def test_batch_retrieval(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.check("#batch")
    page.click("#getInfo")
    page.wait_for_load_state("networkidle")
    all_numbers = page.query_selector_all("#number_info > div")
    assert [x.query_selector_all("div")[0].inner_text() for x in all_numbers] == [
        "329",
        "330",
        "331",
    ]


def test_request(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.click("#getInfo")
    page.wait_for_selector("#number_info > div")
    all_numbers = page.query_selector_all("#number_info > div")
    assert [x.query_selector_all("div")[0].inner_text() for x in all_numbers] == [
        "329",
    ]


def test_batch_request(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#number", "330")
    page.check("#batch")
    page.click("#getInfo")
    page.wait_for_selector("#number_info > div")
    all_numbers = page.query_selector_all("#number_info > div")
    assert [x.query_selector_all("div")[0].inner_text() for x in all_numbers] == [
        "329",
        "330",
        "331",
    ]


if __name__ == "__main__":
    pytest.main(["-v", __file__])
