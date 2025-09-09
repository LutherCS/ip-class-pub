#!/usr/bin/env python3
"""
Testing simple project

@authors: Roman Yasinovskyy
@version: 2025.9
"""

import subprocess

import pytest
from playwright.sync_api import Page, expect


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "projects/hello"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.http_server.terminate()


def test_response(page: Page):
    """Test server response"""
    response = page.request.get("http://localhost:8000/index.html")
    expect(response).to_be_ok()


def test_title(page: Page):
    """Test page title"""
    page.goto("http://localhost:8000/index.html")
    expect(page).to_have_title("Hello, CS330")


def test_heading_location(page: Page):
    """Test the heading location"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("header > h1")).to_be_visible()


def test_heading_text(page: Page):
    """Test the heading text"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("header > h1")).to_have_text("Greetings!")


def test_heading_id(page: Page):
    """Test the heading id"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("header > h1")).to_have_id("greeting")


def test_greeeting_text(page: Page):
    """Test the heading text by id"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("#greeting")).to_have_text("Greetings!")


def test_paragraphs_by_tag(page: Page):
    """Test number of paragraphs"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("main >> p")).to_have_count(3)


def test_paragraphs_by_class(page: Page):
    """Test number of paragraphs with a class"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("p[class='paragraph']")).to_have_count(2)


def test_course(page: Page):
    """Test bolded text"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("p > strong")).to_have_text("CS330")


def test_prereqs(page: Page):
    """Test text with emphasis"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("p[class='paragraph'] > em")).to_have_count(3)


def test_bye_id(page: Page):
    """Test paragraph id"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("p[id='bye']")).to_be_visible()


def test_bye(page: Page):
    """Test paragraph attribute"""
    page.goto("http://localhost:8000/index.html")
    expect(page.locator("p[id='bye']")).to_have_css("color", "rgb(0, 255, 255)")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
