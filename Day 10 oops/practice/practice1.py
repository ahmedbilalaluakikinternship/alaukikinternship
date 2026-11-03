class Employee:
    name="bilal"
    age="22"
    Id="1008"
    department="IT"

    def showdetails(self):
        print("=====Employee Details====")
        print("Emolyee name:",self.name)
        print("Employee age:",self.age)
        print("Employee Id:",self.Id)
        print("Employee Departmen:",self.department)

class Manager(Employee):
    ManagerName="Bhumika Barethiya"
    EmployeeName=Employee.name
    EmployeeAge=Employee.age
    EmployeeId=Employee.Id
    EmployeeDepartment=Employee.department
    def Emp_Data(self):
        print("--------Employee data By Manager-------")

class project(Manager):
    def Assign_project(self):
        print("project assign to Manager:",self.ManagerName)


class task(Employee):
    taskName="Build Frontend Module"
    taskId="122"
    TaskAssign_to=Employee.name
    TaskStatus="Pending"

    def Taskdetails(self):
        print("====Task Data =====")
        print("Task name:",self.taskName)
        print("Task Id:",self.taskId)
        print("Task Assign to:",self.TaskAssign_to)
        print("Task status:",self.TaskStatus)




m= Manager()
m.Emp_Data()

e = Employee()
e.showdetails()

p= project()
p.Assign_project()


t=task()
t.Taskdetails()

