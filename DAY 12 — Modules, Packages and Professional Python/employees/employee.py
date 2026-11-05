import json
import uuid

from config import EMPLOYEE_FILE
from employees.validation import validate_employee
from utils.logger import logger


def load_employees():

    if not EMPLOYEE_FILE.exists():
        return []

    with open(EMPLOYEE_FILE, "r") as file:
        return json.load(file)


def save_employees(employees):

    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file, indent=4)


def add_employee(name, age, department):

    age = validate_employee(name, age, department)

    employees = load_employees()

    employee = {
        "id": str(uuid.uuid4()),
        "name": name.strip(),
        "age": age,
        "department": department.strip()
    }

    employees.append(employee)

    save_employees(employees)

    logger.info("Employee added: %s", employee["name"])

    print("Employee added successfully!")


def show_employees():

    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    print("\n===== EMPLOYEE DETAILS =====")

    for emp in employees:
        print("--------------------------")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Department:", emp["department"])