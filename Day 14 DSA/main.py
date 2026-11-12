from employee_manager import EmployeeManager
from task_manager import TaskManager


employee_manager = EmployeeManager()
task_manager = TaskManager()


def run_application():

    while True:

        print("\n===== OPTIMIZED EMPLOYEE & TASK SYSTEM =====")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Search Employee by ID")
        print("4. Search Employee by Name")
        print("5. Filter Employees by Department")
        print("6. Sort Employees by Name")
        print("7. Sort Employees by Age")
        print("8. Add Task")
        print("9. Show Tasks")
        print("10. Search Task by ID")
        print("11. Search Task by Title")
        print("12. Filter Tasks by Status")
        print("13. Update Task Status")
        print("14. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")

            employee_manager.add_employee(
                emp_id, name, age, department
            )

        elif choice == "2":
            employee_manager.show_employees()

        elif choice == "3":

            emp_id = input("Enter Employee ID: ")
            employee = employee_manager.search_employee(emp_id)

            if employee:
                employee_manager.show_employees([employee])
            else:
                print("Employee not found.")

        elif choice == "4":

            name = input("Enter Employee Name: ")
            result = employee_manager.search_by_name(name)
            employee_manager.show_employees(result)

        elif choice == "5":

            department = input("Enter Department: ")
            result = employee_manager.filter_by_department(department)
            employee_manager.show_employees(result)

        elif choice == "6":
            employee_manager.show_employees(
                employee_manager.sort_by_name()
            )

        elif choice == "7":
            employee_manager.show_employees(
                employee_manager.sort_by_age()
            )

        elif choice == "8":

            task_id = input("Enter Task ID: ")
            title = input("Enter Task Title: ")
            emp_id = input("Enter Assigned Employee ID: ")

            if employee_manager.search_employee(emp_id):
                task_manager.add_task(task_id, title, emp_id)
            else:
                print("Employee not found. Add employee first.")

        elif choice == "9":
            task_manager.show_tasks()

        elif choice == "10":

            task_id = input("Enter Task ID: ")
            task = task_manager.search_task(task_id)

            if task:
                task_manager.show_tasks([task])
            else:
                print("Task not found.")

        elif choice == "11":

            title = input("Enter Task Title: ")
            result = task_manager.search_by_title(title)
            task_manager.show_tasks(result)

        elif choice == "12":

            status = input("Enter Status: ")
            result = task_manager.filter_by_status(status)
            task_manager.show_tasks(result)

        elif choice == "13":

            task_id = input("Enter Task ID: ")
            status = input("Enter New Status: ")

            task_manager.update_status(task_id, status)

        elif choice == "14":
            print("Application closed.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    run_application()