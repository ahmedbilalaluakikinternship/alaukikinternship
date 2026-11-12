from models import Employee, Task
from decorators import log_activity
from generators import process_tasks
from context_manager import TaskProcessingManager


employees = []
tasks = []


@log_activity
def add_employee(name: str, department: str) -> None:

    employee = Employee(name, department)

    employees.append(employee)

    print("Employee added successfully!")
    print("Employee ID:", employee.employee_id)


@log_activity
def add_task(title: str, employee_id: str) -> None:

    employee = next(
        (emp for emp in employees if emp.employee_id == employee_id),
        None
    )

    if employee is None:
        print("Employee not found!")
        return

    task = Task(title, employee)

    tasks.append(task)

    print("Task added successfully!")
    print("Task ID:", task.task_id)


def show_employees() -> None:

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(
            employee.employee_id,
            employee.name,
            employee.department
        )


def show_tasks() -> None:

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            task.task_id,
            task.title,
            task.assigned_to.name,
            task.status
        )


@log_activity
def update_task_status(task_id: str, status: str) -> None:

    for task in tasks:

        if task.task_id == task_id:

            match status:

                case "Pending":
                    task.status = "Pending"

                case "In Progress":
                    task.status = "In Progress"

                case "Completed":
                    task.status = "Completed"

                case _:
                    print("Invalid status!")
                    return

            print("Task status updated successfully!")
            return

    print("Task not found!")


def process_all_tasks() -> None:

    with TaskProcessingManager():

        for task in process_tasks(tasks):

            print("\nProcessing:", task.title)
            print("Assigned To:", task.assigned_to.name)
            print("Current Status:", task.status)


def run_application() -> None:

    while True:

        print("\n===== ADVANCED EMPLOYEE & TASK SYSTEM =====")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Add Task")
        print("4. Show Tasks")
        print("5. Update Task Status")
        print("6. Process All Tasks")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter employee name: ")
            department = input("Enter department: ")

            add_employee(name, department)

        elif choice == "2":
            show_employees()

        elif choice == "3":

            title = input("Enter task title: ")
            employee_id = input("Enter employee ID: ")

            add_task(title, employee_id)

        elif choice == "4":
            show_tasks()

        elif choice == "5":

            task_id = input("Enter task ID: ")
            status = input(
                "Enter status (Pending/In Progress/Completed): "
            )

            update_task_status(task_id, status)

        elif choice == "6":
            process_all_tasks()

        elif choice == "7":
            print("Application closed.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    run_application()