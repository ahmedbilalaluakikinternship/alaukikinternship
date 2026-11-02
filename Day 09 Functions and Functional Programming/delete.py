employees=[]
tasks=[]


def delete_employees():
    emp_id = input("Enter ID: ")
    
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
        print("Employee deleted.")
        break
    else:
        print("Employee not found.")

def delete_Task():
    task_id = input("Enter Task ID: ")
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
        print("Task deleted.")
        break
    else:
        print("Task not found.")



delete_employees()
delete_Task()