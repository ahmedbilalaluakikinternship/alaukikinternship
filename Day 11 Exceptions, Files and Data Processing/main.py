import json
from employees import (
    add_employee,
    show_employees,
    export_csv,
    import_csv,
    export_json,
    import_json,
    create_backup,
    restore_backup
)

from validation import InvalidEmployeeError


while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Export Employees to CSV")
    print("4. Import Employees from CSV")
    print("5. Export Employees to JSON")
    print("6. Import Employees from JSON")
    print("7. Create Backup")
    print("8. Restore Backup")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":

            employee = {
                "emp_id": input("Enter Employee ID: "),
                "name": input("Enter Employee Name: "),
                "age": input("Enter Employee Age: "),
                "joining_date": input("Enter Joining Date (DD-MM-YYYY): ")
            }

            add_employee(employee)

        elif choice == "2":
            show_employees()

        elif choice == "3":
            export_csv()

        elif choice == "4":
            import_csv()

        elif choice == "5":
            export_json()

        elif choice == "6":
            import_json()

        elif choice == "7":
            create_backup()

        elif choice == "8":
            restore_backup()

        elif choice == "9":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please try again.")

    except (InvalidEmployeeError, ValueError, FileNotFoundError,
            json.JSONDecodeError, OSError) as error:
        print("Error:", error)
