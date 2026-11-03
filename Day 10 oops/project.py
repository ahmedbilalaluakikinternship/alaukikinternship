
class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)

class Manager:
    def __init__(self, name):
        self.name = name

    def assign_project(self, project):
        project.manager = self
        print("Project assigned to Manager:", self.name)


class Task:
    def __init__(self, task_id, title, employee):
        self.task_id = task_id
        self.title = title
        self.employee = employee
        self.status = "Pending"

    def update_status(self, status):
        self.status = status

    def show_details(self):
        print("Task ID:", self.task_id)
        print("Task:", self.title)
        print("Assigned Employee:", self.employee.name)
        print("Status:", self.status)


class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.manager = None
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def show_details(self):
        print("\nProject ID:", self.project_id)
        print("Project Name:", self.name)

        if self.manager:
            print("Manager:", self.manager.name)

        print("\nProject Tasks:")

        for task in self.tasks:
            task.show_details()

emp1 = Employee(101, "Ahmed", "Python Developer")
emp2 = Employee(102, "Bilal", "Frontend Developer")

manager1 = Manager("Bhumika Barethiya")

project1 = Project(1, "Employee Management System")


task1 = Task(1, "Create Login Page", emp2)
task2 = Task(2, "Develop Backend", emp1)


manager1.assign_project(project1)


project1.add_task(task1)
project1.add_task(task2)

task1.update_status("Completed")

print("\n===== EMPLOYEE DETAILS =====")
emp1.show_details()
print()
emp2.show_details()

print("\n===== PROJECT DETAILS =====")
project1.show_details()
