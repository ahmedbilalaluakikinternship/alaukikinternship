import pytest

from employee_task_manager.employee import EmployeeManager


@pytest.fixture
def employee_manager():
    return EmployeeManager()


def test_add_employee(employee_manager):

    employee = employee_manager.add_employee(
        "Ahmed",
        30000
    )

    assert employee["name"] == "Ahmed"
    assert employee["salary"] == 30000
    assert employee["id"] == 1


def test_get_employee(employee_manager):

    employee = employee_manager.add_employee(
        "Ahmed",
        30000
    )

    result = employee_manager.get_employee(employee["id"])

    assert result == employee


def test_delete_employee(employee_manager):

    employee = employee_manager.add_employee(
        "Ahmed",
        30000
    )

    result = employee_manager.delete_employee(employee["id"])

    assert result is True

    assert employee_manager.get_employee(employee["id"]) is None


def test_invalid_employee_name(employee_manager):

    with pytest.raises(ValueError):

        employee_manager.add_employee("", 30000)


def test_invalid_salary(employee_manager):

    with pytest.raises(ValueError):

        employee_manager.add_employee("Ahmed", -1000)