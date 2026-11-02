employees=[]

def add_employee():
    name=input("Enter Employee name:")
    emp_id=input("Enter Employee ID:")

    employees.append({"name":name,
                      "emp_id":emp_id
                      })
    print("Employee Added")

add_employee()


