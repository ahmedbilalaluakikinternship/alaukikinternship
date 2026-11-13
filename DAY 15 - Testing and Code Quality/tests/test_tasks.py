
import pytest

from employee_task_manager.task import TaskManager


def test_add_task():
    manager = TaskManager()

    task = manager.add_task("Create Login Page", "Ahmed")

    assert task["title"] == "Create Login Page"
    assert task["assigned_to"] == "Ahmed"
    assert task["status"] == "Pending"


def test_get_task():
    manager = TaskManager()

    task = manager.add_task("Create Dashboard", "Ahmed")

    result = manager.get_task(task["id"])

    assert result == task


def test_update_status():
    manager = TaskManager()

    task = manager.add_task("Create API", "Ahmed")

    updated_task = manager.update_status(
        task["id"], "Completed"
    )

    assert updated_task["status"] == "Completed"


def test_empty_task_title():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task("", "Ahmed")


def test_empty_employee_name():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task("Create Login Page", "")


def test_invalid_status():
    manager = TaskManager()

    task = manager.add_task("Create API", "Ahmed")

    with pytest.raises(ValueError):
        manager.update_status(task["id"], "Cancelled")
