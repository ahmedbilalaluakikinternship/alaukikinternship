employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")

    employees.append({
        "id": emp_id,
        "name": name
    })

    print("Employee added.")

def show_employees():
    for emp in employees:
        print(emp)