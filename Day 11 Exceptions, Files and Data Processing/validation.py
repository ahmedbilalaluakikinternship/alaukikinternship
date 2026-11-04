
from datetime import datetime


class InvalidEmployeeError(Exception):
    pass


def validate_employee(employee):

    if not employee["name"].strip():
        raise InvalidEmployeeError("Employee name cannot be empty.")

    if not employee["emp_id"].strip():
        raise InvalidEmployeeError("Employee ID cannot be empty.")

    try:
        age = int(employee["age"])
    except ValueError:
        raise InvalidEmployeeError("Age must be a number.")

    if age < 18:
        raise InvalidEmployeeError("Employee age must be 18 or above.")

    try:
        datetime.strptime(employee["joining_date"], "%d-%m-%Y")
    except ValueError:
        raise InvalidEmployeeError("Joining date must be DD-MM-YYYY.")

    return True
