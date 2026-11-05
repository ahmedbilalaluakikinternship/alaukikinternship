class InvalidEmployeeError(Exception):
    pass


def validate_employee(name, age, department):

    if not name.strip():
        raise InvalidEmployeeError("Employee name cannot be empty.")

    if not department.strip():
        raise InvalidEmployeeError("Department cannot be empty.")

    try:
        age = int(age)
    except ValueError:
        raise InvalidEmployeeError("Age must be a number.")

    if age < 18:
        raise InvalidEmployeeError("Employee age must be 18 or above.")

    return age