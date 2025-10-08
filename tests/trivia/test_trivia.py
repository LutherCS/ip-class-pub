#!/usr/bin/env python3
"""
`trivia` testing

@authors: Roman Yasinovskyy
@version: 2025.10
"""

import json
import pathlib
import random
import subprocess

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)


def setup_module(module):
    """Set up"""
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/trivia"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Tear down"""
    module.http_server.terminate()


@pytest.fixture(name="test_json")
def test_json():
    def _test_json(category: str, number: int = 3):
        with open(
            pathlib.Path(__file__).parent / pathlib.Path("testQuestions.json"), "r"
        ) as f:
            data = json.loads(f.read())
        if category:
            data["results"] = [
                question
                for question in data["results"]
                if question["category"] == category
            ]
        data["results"] = data["results"][:number]
        return data

    return _test_json


def test_no_input(page: Page):
    """Button clicked without any input"""
    page.goto("http://localhost:8000/")
    page.click("#getQuestionsBtn")

    expect(page.locator("#numberInputField > p.help")).to_have_class("help is-warning")
    expect(page.locator("#numberInputField > p.help")).to_have_text(
        "This field is required"
    )


@pytest.mark.parametrize("number", random.choices(range(11, 99), k=5))
def test_wrong_input(page: Page, number: int):
    """Button clicked with a number out of 1..10 range"""
    page.goto("http://localhost:8000/")
    page.fill("#numberInput", f"{number}")
    page.click("#getQuestionsBtn")

    expect(page.locator("#numberInputField > p.help")).to_have_class("help is-warning")
    expect(page.locator("#numberInputField > p.help")).to_have_text(
        "Enter a number between 1 and 10"
    )


@pytest.mark.parametrize(
    "category", ["Science: Computers", "Mythology", "Geography", "History"]
)
@pytest.mark.parametrize("number", [1, 2, 3])
def test_numbers(page: Page, test_json, category: str, number: int):
    """Only the chosen number of questions must be retrieved"""
    page.route("*/**/bulma.min.css", lambda route: route.abort())
    page.route(
        "https://opentdb.com/api.php*",
        lambda route: route.fulfill(json=test_json(category, number)),
    )
    page.goto("http://localhost:8000/")
    page.select_option("#categorySelect", category)
    page.fill("#numberInput", str(number))
    page.click("#getQuestionsBtn")

    expect(page.locator("#questionsDiv > .card")).to_have_count(number)
    expect(
        page.locator("#questionsDiv > .card > footer > p:nth-child(1)")
    ).to_have_text([category] * number)


@pytest.mark.parametrize(
    "category", ["Science: Computers", "Mythology", "Geography", "History"]
)
def test_categories(page: Page, test_json, category: str):
    """Only questions in the selected category must be retrieved"""
    page.route("*/**/bulma.min.css", lambda route: route.abort())
    page.route(
        "https://opentdb.com/api.php*",
        lambda route: route.fulfill(json=test_json(category)),
    )
    page.goto("http://localhost:8000/")
    page.select_option("#categorySelect", category)
    page.fill("#numberInput", "3")
    page.click("#getQuestionsBtn")

    expect(page.locator("#questionsDiv > .card")).to_have_count(3)
    expect(
        page.locator("#questionsDiv > .card > footer > p:nth-child(1)")
    ).to_have_text([category] * 3)


@pytest.mark.parametrize(
    "category", ["Science: Computers", "Mythology", "Geography", "History"]
)
def test_difficulty(page: Page, test_json, category: str):
    """Questions of various levels of difficulty must be retrieved"""
    page.route("*/**/bulma.min.css", lambda route: route.abort())
    page.route(
        "https://opentdb.com/api.php*",
        lambda route: route.fulfill(json=test_json(category)),
    )
    page.goto("http://localhost:8000/")
    page.select_option("#categorySelect", category)
    page.fill("#numberInput", "3")
    page.click("#getQuestionsBtn")

    expect(page.locator("#questionsDiv > .easy")).to_have_count(1)
    expect(page.locator("#questionsDiv > .medium")).to_have_count(1)
    expect(page.locator("#questionsDiv > .hard")).to_have_count(1)
    expect(
        page.locator("#questionsDiv > .card > footer > p:nth-child(2)")
    ).to_have_text(["Easy", "Medium", "Hard"])


@pytest.mark.parametrize(
    "category", ["Science: Computers", "Mythology", "Geography", "History"]
)
def test_answers(page: Page, test_json, category: str):
    """Category selection"""
    page.route("*/**/bulma.min.css", lambda route: route.abort())
    page.route(
        "https://opentdb.com/api.php*",
        lambda route: route.fulfill(json=test_json(category)),
    )
    page.goto("http://localhost:8000/")
    page.select_option("#categorySelect", category)
    page.fill("#numberInput", "3")
    page.click("#getQuestionsBtn")

    expect(
        page.locator("#questionsDiv > .card > footer > p:nth-child(3) > button")
    ).to_have_count(3)
    for button in page.locator(
        "#questionsDiv > .card > footer > p:nth-child(3) > button"
    ).all():
        button.click()
    expect(
        page.locator(
            "#questionsDiv > .card > div.card-content > ol > li.correct_answer"
        )
    ).to_have_count(3)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
