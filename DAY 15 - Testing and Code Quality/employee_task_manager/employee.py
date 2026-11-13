class EmployeeManager:

    def __init__(self):
        self.employees = []
        self.next_id = 1

    def add_employee(self, name, salary):

        if not name.strip():
            raise ValueError("Employee name is required")

        if salary <= 0:
            raise ValueError("Salary must be positive")

        employee = {
            "id": self.next_id,
            "name": name,
            "salary": salary
        }

        self.employees.append(employee)
        self.next_id += 1

        return employee

    def get_employee(self, employee_id):

        for employee in self.employees:

            if employee["id"] == employee_id:
                return employee

        return None

    def delete_employee(self, employee_id):

        employee = self.get_employee(employee_id)

        if employee is None:
            return False

        self.employees.remove(employee)

        return True