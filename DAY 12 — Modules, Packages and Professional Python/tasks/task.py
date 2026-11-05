import json
import uuid

from enum import Enum

from config import TASK_FILE
from employees.employee import load_employees
from utils.logger import logger


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


def load_tasks():

    if not TASK_FILE.exists():
        return []

    with open(TASK_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):

    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title, employee_id):

    employees = load_employees()

    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        print("Employee not found.")
        return

    tasks = load_tasks()

    task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "employee_id": employee_id,
        "employee_name": employee["name"],
        "status": TaskStatus.PENDING.value
    }

    tasks.append(task)

    save_tasks(tasks)

    logger.info("Task added: %s", title)

    print("Task added successfully!")


def show_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n===== TASK DETAILS =====")

    for task in tasks:
        print("--------------------------")
        print("Task ID:", task["id"])
        print("Title:", task["title"])
        print("Assigned To:", task["employee_name"])
        print("Status:", task["status"])


def update_task_status(task_id, status):

    valid_statuses = [item.value for item in TaskStatus]

    if status not in valid_statuses:
        print("Invalid task status.")
        print("Available statuses:", valid_statuses)
        return

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)

            logger.info("Task status updated: %s", task_id)

            print("Task status updated successfully!")
            return

    print("Task not found.")