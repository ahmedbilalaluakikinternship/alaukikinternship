employees=[]
tasks=[]

def add_employee():
    emp_name=input("Pls Enter Employee Name:")
    emp_id=input("Enter Employee ID:")

    employees.append({
        "name":emp_name,
        "id":emp_id,

    })
    print("employee added")


def add_task():
    task_name=input("Enter Task Name:")
    task_id=input("Enter Task id:")

    tasks.append({
        "task_name":task_name,
        "task_id":task_id,
    })

    print("task added successfully")
def show_employees():
    for emp in employees:
        print("Name:", emp["name"])
        print("ID:", emp["id"])


def show_tasks():
    for task in tasks:
        print("Task Name:", task["task_name"])
        print("Task ID:", task["task_id"])




add_employee()
add_task()

print("\n===== Employee Records =====")
show_employees()

print("\n===== Task Records =====")
show_tasks()