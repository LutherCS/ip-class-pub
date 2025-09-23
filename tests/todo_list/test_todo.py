#!/usr/bin/env python3
"""
`todo_list` testing

@authors: Roman Yasinovskyy
@version: 2025.9
"""

import subprocess

import pytest
from playwright.sync_api import Page, expect

expect.set_options(timeout=1_000)


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


def test_skip_input(page: Page):
    """Button clicked without any input"""
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    expect(page.locator("#taskTitleText > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskTitleText > p.help")).to_have_text("Task title is required")
    expect(page.locator("#taskDueDate > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskDueDate > p.help")).to_have_text("Task due date is required")


def test_skip_title(page: Page):
    """Title not chosen"""
    page.goto("http://localhost:8000/")
    page.fill("#dueDate", "2025-09-30")
    page.click("#addTaskBtn")
    expect(page.locator("#taskTitleText > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskTitleText > p.help")).to_have_text("Task title is required")


def test_skip_duedate(page: Page):
    """Date not chosen"""
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.click("#addTaskBtn")
    expect(page.locator("#taskDueDate > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskDueDate > p.help")).to_have_text("Task due date is required")


def test_skip_title_then_enter(page: Page):
    """Title is not entered and then entered"""
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    page.fill("#title", "Task title")
    page.click("#addTaskBtn")
    expect(page.locator("#taskTitleText > p.help")).to_have_class("help")
    expect(page.locator("#taskTitleText > p.help")).to_have_text("Task title is required")
    expect(page.locator("#taskDueDate > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskDueDate > p.help")).to_have_text("Task due date is required")


def test_skip_duedate_then_enter(page: Page):
    """Title is not entered and then entered"""
    page.goto("http://localhost:8000/")
    page.click("#addTaskBtn")
    page.fill("#dueDate", "2025-09-30")
    page.click("#addTaskBtn")
    expect(page.locator("#taskTitleText > p.help")).to_have_class("help is-danger")
    expect(page.locator("#taskTitleText > p.help")).to_have_text("Task title is required")
    expect(page.locator("#taskDueDate > p.help")).to_have_class("help")
    expect(page.locator("#taskDueDate > p.help")).to_have_text("Task due date is required")


def test_skip_selection(page: Page):
    """Default selection"""
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2025-09-30")
    page.click("#addTaskBtn")
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(1)
    expect(page.locator("tbody > tr > td:nth-child(2)")).to_have_text("Task title")
    expect(page.locator("tbody > tr > td:nth-child(3)")).to_have_text("Aardvark")
    expect(page.locator("tbody > tr > td:nth-child(4)")).to_have_text("Low")
    expect(page.locator("tbody > tr > td:nth-child(5)")).to_have_text("2025-09-30")


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
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2025-09-30")
    page.select_option("#assignedTo", worker)
    page.click("#addTaskBtn")
    expect(page.locator("tbody > tr > td:nth-child(3)")).to_have_text(worker)


@pytest.mark.parametrize("priority", ["Low", "Normal", "Important", "Critical"])
def test_select_priority(page: Page, priority: str):
    """Various priorities"""
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2025-09-30")
    page.select_option("#priority", priority)
    page.click("#addTaskBtn")
    expect(page.locator("tbody > tr")).to_have_class(priority.lower())
    expect(page.locator("tbody > tr > td:nth-child(4)")).to_have_text(priority)


def test_remove_row(page: Page):
    """Remove a task"""
    page.goto("http://localhost:8000/")
    page.fill("#title", "Task title")
    page.fill("#dueDate", "2025-09-30")
    page.click("#addTaskBtn")
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(1)
    page.click("table[id='taskList'] > tbody > tr > td > input[type='checkbox']")
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(1)
    page.wait_for_timeout(3000)
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(0)


def test_remove_all_rows(page: Page):
    """Remove a task"""
    page.goto("http://localhost:8000/")
    for _ in range(3):
        page.fill("#title", "Task title")
        page.fill("#dueDate", "2025-09-30")
        page.click("#addTaskBtn")
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(3)
    page.click("#removeAllTasks")
    page.wait_for_timeout(3000)
    expect(page.locator("table[id='taskList'] > tbody > tr")).to_have_count(0)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
