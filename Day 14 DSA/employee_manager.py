class EmployeeManager:

    def __init__(self):
        self.employees = []
        self.employee_index = {}

    def add_employee(self, employee_id, name, age, department):

        if employee_id in self.employee_index:
            print("Employee ID already exists.")
            return

        employee = {
            "id": employee_id,
            "name": name,
            "age": age,
            "department": department
        }

        self.employees.append(employee)
        self.employee_index[employee_id] = employee

        print("Employee added successfully!")

    def search_employee(self, employee_id):
        return self.employee_index.get(employee_id)

    def search_by_name(self, name):
        return [
            emp for emp in self.employees
            if name.casefold() in emp["name"].casefold()
        ]

    def filter_by_department(self, department):
        return [
            emp for emp in self.employees
            if emp["department"].casefold() == department.casefold()
        ]

    def sort_by_name(self):
        return sorted(
            self.employees,
            key=lambda emp: emp["name"].casefold()
        )

    def sort_by_age(self):
        return sorted(
            self.employees,
            key=lambda emp: emp["age"]
        )

    def show_employees(self, employees=None):

        records = self.employees if employees is None else employees

        if not records:
            print("No employees found.")
            return

        for emp in records:
            print("-------------------------")
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Department:", emp["department"])