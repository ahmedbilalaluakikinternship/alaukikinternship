import argparse

from config import APP_NAME, APP_VERSION

from employees.employee import add_employee, show_employees

from tasks.task import (
    add_task,
    show_tasks,
    update_task_status
)

from utils.backup import create_backup, restore_backup

from utils.logger import logger

from employees.validation import InvalidEmployeeError


def run_menu():

    while True:

        print(f"\n===== {APP_NAME} =====")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Add Task")
        print("4. Show Tasks")
        print("5. Update Task Status")
        print("6. Create Backup")
        print("7. Restore Backup")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":

                name = input("Enter Employee Name: ")
                age = input("Enter Employee Age: ")
                department = input("Enter Department: ")

                add_employee(name, age, department)

            elif choice == "2":
                show_employees()

            elif choice == "3":

                title = input("Enter Task Title: ")
                employee_id = input("Enter Employee ID: ")

                add_task(title, employee_id)

            elif choice == "4":
                show_tasks()

            elif choice == "5":

                task_id = input("Enter Task ID: ")
                status = input(
                    "Enter Status (Pending/In Progress/Completed): "
                )

                update_task_status(task_id, status)

            elif choice == "6":
                create_backup()

            elif choice == "7":
                restore_backup()

            elif choice == "8":
                print("Application closed.")
                break

            else:
                print("Invalid choice.")

        except (InvalidEmployeeError, ValueError, OSError) as error:
            logger.error("Application error: %s", error)
            print("Error:", error)


def main():

    parser = argparse.ArgumentParser(
        description=APP_NAME
    )

    parser.add_argument(
        "--version",
        action="version",
        version=APP_VERSION
    )

    parser.add_argument(
        "--action",
        choices=["add-employee", "show-employees"],
        help="Select an employee operation"
    )

    parser.add_argument("--name", help="Employee name")
    parser.add_argument("--age", help="Employee age")
    parser.add_argument("--department", help="Employee department")

    args = parser.parse_args()

    try:

        if args.action == "add-employee":

            if not args.name or not args.age or not args.department:
                parser.error(
                    "add-employee requires --name, --age and --department"
                )

            add_employee(args.name, args.age, args.department)

        elif args.action == "show-employees":
            show_employees()

        else:
            run_menu()

    except (InvalidEmployeeError, ValueError, OSError) as error:
        logger.error("CLI error: %s", error)
        print("Error:", error)


if __name__ == "__main__":
    main()