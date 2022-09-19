#!/usr/bin/env python3
"""
`todo_list` testing

@authors: Roman Yasinovskyy
@version: 2022.9
"""

import subprocess
from time import sleep

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/todo_list"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    module.http_server.terminate()


def test_no_input(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    assert (
        page.query_selector("#feedbackMessage").inner_text()
        == "Fill out title and due date"
    )


def test_no_date(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.click("#addTaskBtn")
    assert (
        page.query_selector("#feedbackMessage").inner_text()
        == "Fill out title and due date"
    )


def test_no_title(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#dueDate", "2022-09-25")
    page.click("#addTaskBtn")
    assert (
        page.query_selector("#feedbackMessage").inner_text()
        == "Fill out title and due date"
    )


def test_no_selection(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2022-09-25")
    page.click("#addTaskBtn")
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    new_row = all_rows[-1]
    assert len(all_rows) == 1
    assert new_row.query_selector_all("td")[1].inner_text() == "Task title"
    assert new_row.query_selector_all("td")[2].inner_text() == "Aardvark"
    assert new_row.query_selector_all("td")[3].inner_text() == "Low"
    assert new_row.query_selector_all("td")[4].inner_text() == "2022-09-25"


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
def test_select_worker(page: Page, worker):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2022-09-25")
    page.select_option("#assignedTo", worker)
    page.click("#addTaskBtn")
    new_row = page.query_selector_all("table[id='taskList'] > tbody > tr")[-1]

    assert new_row.query_selector_all("td")[2].inner_text() == worker


@pytest.mark.parametrize("priority", ["Low", "Normal", "Important", "Critical"])
def test_select_priority(page: Page, priority):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2022-09-25")
    page.select_option("#priority", priority)
    page.click("#addTaskBtn")
    new_row = page.query_selector_all("table[id='taskList'] > tbody > tr")[-1]

    assert new_row.query_selector_all("td")[3].inner_text() == priority
    assert priority.lower() in new_row.get_attribute("class")


def test_remove_row(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2022-09-25")
    page.click("#addTaskBtn")
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    assert len(all_rows) == 1
    page.check("table[id='taskList'] > tbody > tr > td > input[type='checkbox']")
    sleep(3)
    all_rows = page.query_selector_all("table[id='taskList'] > tbody > tr")
    assert len(all_rows) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
