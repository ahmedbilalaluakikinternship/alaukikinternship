
import csv
import json
import shutil
from pathlib import Path

from validation import validate_employee


# Project folders
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backup"

CSV_FILE = DATA_DIR / "employees.csv"
JSON_FILE = DATA_DIR / "employees.json"
BACKUP_FILE = BACKUP_DIR / "employees_backup.json"

# Automatically create folders
DATA_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)


# Load employees from JSON
def load_employees():

    if JSON_FILE.exists() and JSON_FILE.stat().st_size > 0:

        with open(JSON_FILE, "r") as file:
            return json.load(file)

    return []


# Save employees to JSON
def save_employees(employees):

    with open(JSON_FILE, "w") as file:
        json.dump(employees, file, indent=4)


# Add employee
def add_employee(employee):

    validate_employee(employee)

    employees = load_employees()

    for emp in employees:
        if emp["emp_id"] == employee["emp_id"]:
            raise ValueError("Employee ID already exists.")

    employees.append(employee)

    save_employees(employees)

    print("Employee added successfully!")


# Show employees
def show_employees():

    employees = load_employees()

    if not employees:
        print("No employee records found.")
        return

    for emp in employees:
        print("\n--------------------")
        print("ID:", emp["emp_id"])
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Joining Date:", emp["joining_date"])


# Export employees to CSV
def export_csv():

    employees = load_employees()

    fields = ["emp_id", "name", "age", "joining_date"]

    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(employees)

    print("CSV export successful!")


# Import employees from CSV
def import_csv():

    employees = load_employees()
    existing_ids = {emp["emp_id"] for emp in employees}
    count = 0

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            validate_employee(row)

            if row["emp_id"] not in existing_ids:
                employees.append(row)
                existing_ids.add(row["emp_id"])
                count += 1

    save_employees(employees)

    print(count, "employees imported from CSV.")


# Export employees to JSON
def export_json():

    employees = load_employees()

    with open(JSON_FILE, "w") as file:
        json.dump(employees, file, indent=4)

    print("JSON export successful!")


# Import employees from JSON
def import_json():

    with open(JSON_FILE, "r") as file:
        imported_data = json.load(file)

    if not isinstance(imported_data, list):
        raise ValueError("JSON must contain a list of employees.")

    employees = load_employees()
    existing_ids = {emp["emp_id"] for emp in employees}
    count = 0

    for emp in imported_data:
        validate_employee(emp)

        if emp["emp_id"] not in existing_ids:
            employees.append(emp)
            existing_ids.add(emp["emp_id"])
            count += 1

    save_employees(employees)

    print(count, "employees imported from JSON.")


# Create backup
def create_backup():

    if not JSON_FILE.exists():
        raise FileNotFoundError("No employee data available to backup.")

    shutil.copy2(JSON_FILE, BACKUP_FILE)

    print("Backup created successfully!")


# Restore backup
def restore_backup():

    if not BACKUP_FILE.exists():
        raise FileNotFoundError("Backup file not found.")

    shutil.copy2(BACKUP_FILE, JSON_FILE)

    print("Backup restored successfully!")
