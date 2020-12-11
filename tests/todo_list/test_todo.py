#!/usr/bin/env python3
"""Testing todo_list"""

import subprocess
from time import sleep

import pytest
from playwright.sync_api import Page


def setup_module(module):
    module.http_server = subprocess.Popen(
        ["python3", "-m", "http.server", "--directory", "exercises/todo_list"]
    )
    try:
        module.http_server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass
    # module.pid = http_server.pid
    # sleep(1)


def teardown_module(module):
    # subprocess.Popen(["kill", "-9", f"{module.pid}"])
    module.http_server.terminate()


def test_no_input(page: Page):
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    assert (
        page.querySelector("#feedbackMessage").innerText()
        == "Fill out title and due date"
    )


def test_no_date(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.click("#addTaskBtn")
    assert (
        page.querySelector("#feedbackMessage").innerText()
        == "Fill out title and due date"
    )


def test_no_title(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#dueDate", "2020-12-20")
    page.click("#addTaskBtn")
    assert (
        page.querySelector("#feedbackMessage").innerText()
        == "Fill out title and due date"
    )


def test_no_selection(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2020-12-20")
    page.click("#addTaskBtn")
    allRows = page.querySelectorAll("table[id='taskList'] > tbody > tr")
    newRow = allRows[-1]
    assert len(allRows) == 1
    assert newRow.querySelectorAll("td")[1].innerText() == "Task title"
    assert newRow.querySelectorAll("td")[2].innerText() == "Aardvark"
    assert newRow.querySelectorAll("td")[3].innerText() == "Low"
    assert newRow.querySelectorAll("td")[4].innerText() == "2020-12-20"


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
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2020-12-20")
    page.selectOption("#assignedTo", worker)
    page.click("#addTaskBtn")
    newRow = page.querySelectorAll("table[id='taskList'] > tbody > tr")[-1]

    assert newRow.querySelectorAll("td")[2].innerText() == worker


@pytest.mark.parametrize("priority", ["Low", "Normal", "Important", "Critical"])
def test_select_priority(page: Page, priority):
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2020-12-20")
    page.selectOption("#priority", priority)
    page.click("#addTaskBtn")
    newRow = page.querySelectorAll("table[id='taskList'] > tbody > tr")[-1]

    assert newRow.querySelectorAll("td")[3].innerText() == priority
    assert priority.lower() in newRow.getAttribute("class")


def test_remove_row(page: Page):
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2020-12-20")
    page.click("#addTaskBtn")
    allRows = page.querySelectorAll("table[id='taskList'] > tbody > tr")
    assert len(allRows) == 1
    page.check("table[id='taskList'] > tbody > tr > td > input[type='checkbox']")
    sleep(3)
    allRows = page.querySelectorAll("table[id='taskList'] > tbody > tr")
    assert len(allRows) == 0
