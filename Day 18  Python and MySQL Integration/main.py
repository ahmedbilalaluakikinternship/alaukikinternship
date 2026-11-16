
from employee import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

from task import (
    add_task,
    get_all_tasks,
    get_task_by_id,
    update_task_status,
    delete_task
)


def employee_menu():

    while True:

        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. View Employee By ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Back to Main Menu")

        choice = input("Enter Choice: ")

        try:

            if choice == "1":

                full_name = input("Enter Full Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                department = input("Enter Department: ")
                salary = float(input("Enter Salary: "))
                joining_date = input("Joining Date (YYYY-MM-DD): ")

                add_employee(
                    full_name,
                    email,
                    phone,
                    department,
                    salary,
                    joining_date
                )

            elif choice == "2":
                get_all_employees()

            elif choice == "3":

                employee_id = int(input("Enter Employee ID: "))
                get_employee_by_id(employee_id)

            elif choice == "4":

                employee_id = int(input("Enter Employee ID: "))
                department = input("Enter New Department: ")
                salary = float(input("Enter New Salary: "))

                update_employee(
                    employee_id,
                    department,
                    salary
                )

            elif choice == "5":

                employee_id = int(input("Enter Employee ID: "))

                confirm = input(
                    "Are you sure you want to delete? (yes/no): "
                )

                if confirm.lower() == "yes":
                    delete_employee(employee_id)

            elif choice == "6":
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please enter valid input!")


def task_menu():

    while True:

        print("\n========== TASK MANAGEMENT ==========")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Task By ID")
        print("4. Update Task Status")
        print("5. Delete Task")
        print("6. Back to Main Menu")

        choice = input("Enter Choice: ")

        try:

            if choice == "1":

                task_title = input("Enter Task Title: ")
                description = input("Enter Description: ")
                employee_id = int(input("Enter Employee ID: "))
                project_id = int(input("Enter Project ID: "))
                priority = input("Enter Priority: ")
                status = input("Enter Status: ")
                due_date = input("Due Date (YYYY-MM-DD): ")

                add_task(
                    task_title,
                    description,
                    employee_id,
                    project_id,
                    priority,
                    status,
                    due_date
                )

            elif choice == "2":
                get_all_tasks()

            elif choice == "3":

                task_id = int(input("Enter Task ID: "))
                get_task_by_id(task_id)

            elif choice == "4":

                task_id = int(input("Enter Task ID: "))
                status = input("Enter New Status: ")

                update_task_status(task_id, status)

            elif choice == "5":

                task_id = int(input("Enter Task ID: "))

                confirm = input(
                    "Are you sure you want to delete? (yes/no): "
                )

                if confirm.lower() == "yes":
                    delete_task(task_id)

            elif choice == "6":
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please enter valid input!")


def main():

    while True:

        print("\n========================================")
        print(" EMPLOYEE & TASK MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Employee Management")
        print("2. Task Management")
        print("3. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            employee_menu()

        elif choice == "2":
            task_menu()

        elif choice == "3":
            print("Thank You for Using the System!")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
    