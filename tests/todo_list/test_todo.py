#!/usr/bin/env python3
"""
`todo_list` testing

@authors: Roman Yasinovskyy
@version: 2023.9
"""

import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Set up"""
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/todo_list"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Tear down"""
    module.http_server.terminate()


def test_no_input(page: Page):
    """Button clicked without any input"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    assert (
        page.locator("#feedbackMessage").inner_text() == "Fill out title and due date"
    )


def test_no_date(page: Page):
    """Date not chosen"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.click("#addTaskBtn")
    assert (
        page.locator("#feedbackMessage").inner_text() == "Fill out title and due date"
    )


def test_no_title(page: Page):
    """Title not chosen"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#dueDate", "2023-09-26")
    page.click("#addTaskBtn")
    assert (
        page.locator("#feedbackMessage").inner_text() == "Fill out title and due date"
    )


def test_no_selection(page: Page):
    """Default selection"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2023-09-26")
    page.click("#addTaskBtn")
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    new_row = all_rows[-1]
    assert len(all_rows) == 1
    assert new_row.query_selector_all("td")[1].inner_text() == "Task title"
    assert new_row.query_selector_all("td")[2].inner_text() == "Aardvark"
    assert new_row.query_selector_all("td")[3].inner_text() == "Low"
    assert new_row.query_selector_all("td")[4].inner_text() == "2023-09-26"


@pytest.mark.parametrize(
    "worker",
    [
        "Aardvark",
        "Beaver",
        "Cheetah",
        "Dolphin",
        "Elephant",
        "Flamingo",
        "Giraffe",
        "Hippo",
    ],
)
def test_select_worker(page: Page, worker: str):
    """Various workers"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2023-09-26")
    page.select_option("#assignedTo", worker)
    page.click("#addTaskBtn")
    new_row = page.query_selector_all("table[id='taskList'] > tbody > tr")[-1]

    assert new_row.query_selector_all("td")[2].inner_text() == worker


@pytest.mark.parametrize("priority", ["Low", "Normal", "Important", "Critical"])
def test_select_priority(page: Page, priority: str):
    """Various priorities"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2023-09-26")
    page.select_option("#priority", priority)
    page.click("#addTaskBtn")
    new_row = page.query_selector_all("table[id='taskList'] > tbody > tr")[-1]

    assert new_row.query_selector_all("td")[3].inner_text() == priority
    assert new_row.get_attribute("class").index(priority.lower()) > -1


def test_remove_row(page: Page):
    """Remove a task"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2023-09-26")
    page.click("#addTaskBtn")
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    assert len(all_rows) == 1
    page.click("table[id='taskList'] > tbody > tr > td > input[type='checkbox']")
    page.wait_for_timeout(3000)
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    assert len(all_rows) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
