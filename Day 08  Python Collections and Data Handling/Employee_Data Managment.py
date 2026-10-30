
employees = []
tasks = []

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Add Task")
    print("7. Show Tasks")
    print("8. Update Task Status")
    print("9. Delete Task")
    print("10. Show Summary")
    print("11. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter ID: ")

        if any(emp["id"] == emp_id for emp in employees):
            print("Employee already exists.")
        else:
            name = input("Enter Name: ")
            position = input("Enter Position: ")

            employees.append({
                "id": emp_id,
                "name": name,
                "position": position
            })
            print("Employee added.")

    elif choice == "2":
        for emp in employees:
            print(emp)

        if not employees:
            print("No employees found.")

    elif choice == "3":
        emp_id = input("Enter ID: ")

        for emp in employees:
            if emp["id"] == emp_id:
                emp["name"] = input("Enter new name: ")
                emp["position"] = input("Enter new position: ")
                print("Employee updated.")
                break
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter ID: ")

        for emp in employees:
            if emp["id"] == emp_id:
                employees.remove(emp)
                print("Employee deleted.")
                break
        else:
            print("Employee not found.")

    elif choice == "5":
        emp_id = input("Enter ID: ")

        for emp in employees:
            if emp["id"] == emp_id:
                print("Employee Found:", emp)
                break
        else:
            print("Employee not found.")

    elif choice == "6":
        task_id = input("Enter Task ID: ")
        emp_id = input("Enter Employee ID: ")

        if not any(emp["id"] == emp_id for emp in employees):
            print("Employee not found.")
        elif any(task["id"] == task_id for task in tasks):
            print("Task already exists.")
        else:
            title = input("Enter Task Title: ")

            tasks.append({
                "id": task_id,
                "title": title,
                "employee_id": emp_id,
                "status": "Pending"
            })
            print("Task added.")

    elif choice == "7":
        for task in tasks:
            print(task)

        if not tasks:
            print("No tasks found.")

    elif choice == "8":
        task_id = input("Enter Task ID: ")

        for task in tasks:
            if task["id"] == task_id:
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")

                status = input("Choose status: ")

                if status == "1":
                    task["status"] = "Pending"
                elif status == "2":
                    task["status"] = "In Progress"
                elif status == "3":
                    task["status"] = "Completed"
                else:
                    print("Invalid choice.")
                    break

                print("Status updated.")
                break
        else:
            print("Task not found.")

    elif choice == "9":
        task_id = input("Enter Task ID: ")

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted.")
                break
        else:
            print("Task not found.")

    elif choice == "10":
        completed = sum(t["status"] == "Completed" for t in tasks)
        pending = sum(t["status"] == "Pending" for t in tasks)
        progress = sum(t["status"] == "In Progress" for t in tasks)

        print("\n===== System Summary =====")
        print("Total Employees:", len(employees))
        print("Total Tasks:", len(tasks))
        print("Pending:", pending)
        print("In Progress:", progress)
        print("Completed:", completed)

    elif choice == "11":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
