#!/usr/bin/env python3
"""
Test the user interface

@authors: Roman Yasinovskyy
@version: 2025.12
"""

import os
import subprocess

import pytest
from playwright.sync_api import Playwright, expect, sync_playwright

expect.set_options(timeout=1_000)


@pytest.fixture(scope="module", autouse=True)
def server():
    """Create the server fixture"""
    os.chdir("exercises/authorization")
    server = subprocess.Popen(["flask", "run"])
    try:
        server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass
    yield
    server.terminate()


def test_main(playwright: Playwright):
    """Test main page"""
    browser = playwright.firefox.launch()
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.route(
        "https://cdn.jsdelivr.net/**",
        lambda route: route.abort(),
    )
    page.goto("https://panda.luther.edu:5000/")
    page.locator("a#loginBtn").click()
    expect(page.get_by_text("Sign in with Google")).to_be_visible()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        test_main(playwright)
