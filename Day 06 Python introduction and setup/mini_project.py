# mini python project using core python concepts
print("Welcome to Employee Management System")
print("Please enter the following details to add a new employee")
print("-------------------------------------------------------------")
Employee_name = input("Enter your name: ")
Employee_id = int(input("Enter your employee id : "))
Employee_salary = float(input("Enter your salary: "))

print("---------------------------Your Details---------------------------------")

print("Employee Name : " + Employee_name)
print("Employee ID : " + str(Employee_id))
print("Employee Salary : " + str(Employee_salary))

print("-------------------------------------------------------------")
print("Thank you for your support, " + Employee_name + "! Your details have been added successfully.")