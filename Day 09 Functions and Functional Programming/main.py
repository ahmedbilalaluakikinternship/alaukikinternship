import employee
import task
import delete

while True:
    print("\n=====Employee & Task Management System =====")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Add Task")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        employee.add_employee()

    elif choice == "2":
        employee.show_employees()

    elif choice == "3":
        task.add_task()

    elif choice == "4":
        task.show_tasks()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice.")