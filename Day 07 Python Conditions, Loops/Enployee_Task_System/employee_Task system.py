
employees = []
tasks = []

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Add Task")
    print("4. Show Tasks")
    print("5. Change Task Status")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter job position: ")

        employee = {
            "id": emp_id,
            "name": name,
            "position": position
        }

        employees.append(employee)
        print("Employee added.")

    elif choice == "2":
        if not employees:
            print("No employee records found.")
        else:
            for emp in employees:
                print("\nEmployee ID:", emp["id"])
                print("Name:", emp["name"])
                print("Position:", emp["position"])

    elif choice == "3":
        if not employees:
            print("Add an employee before creating a task.")
            continue

        emp_id = input("Enter employee ID: ")
        found = False

        for emp in employees:
            if emp["id"] == emp_id:
                found = True
                break

        if found:
            task_id = input("Enter task ID: ")
            title = input("Enter task name: ")

            task = {
                "id": task_id,
                "title": title,
                "employee_id": emp_id,
                "status": "Pending"
            }

            tasks.append(task)
            print("Task added.")
        else:
            print("Employee ID not found.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print("\nTask ID:", task["id"])
                print("Task:", task["title"])
                print("Assigned Employee:", task["employee_id"])
                print("Status:", task["status"])

    elif choice == "5":
        task_id = input("Enter task ID: ")
        found = False

        for task in tasks:
            if task["id"] == task_id:
                found = True
                print("1. Pending")
                print("2. Completed")

                status = input("Choose status: ")

                if status == "1":
                    task["status"] = "Pending"
                    print("Status changed to Pending.")
                elif status == "2":
                    task["status"] = "Completed"
                    print("Task completed.")
                else:
                    print("Invalid option.")

                break

        if not found:
            print("Task ID not found.")

    elif choice == "6":
        print("Application closed.")
        break

    else:
        print("Please select a valid option.")
