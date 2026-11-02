tasks = []

def add_task():
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Name: ")

    tasks.append({
        "id": task_id,
        "title": title,
        "status": "Pending"
    })

    print("Task added.")

def show_tasks():
    for task in tasks:
        print(task)