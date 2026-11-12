class TaskManager:

    def __init__(self):
        self.tasks = []
        self.task_index = {}

    def add_task(self, task_id, title, employee_id, status="Pending"):

        if task_id in self.task_index:
            print("Task ID already exists.")
            return

        task = {
            "id": task_id,
            "title": title,
            "employee_id": employee_id,
            "status": status
        }

        self.tasks.append(task)
        self.task_index[task_id] = task

        print("Task added successfully!")

    def search_task(self, task_id):
        return self.task_index.get(task_id)

    def filter_by_status(self, status):
        return [
            task for task in self.tasks
            if task["status"].casefold() == status.casefold()
        ]

    def search_by_title(self, title):
        return [
            task for task in self.tasks
            if title.casefold() in task["title"].casefold()
        ]

    def update_status(self, task_id, status):

        task = self.search_task(task_id)

        if task is None:
            print("Task not found.")
            return

        valid_statuses = ["Pending", "In Progress", "Completed"]

        if status not in valid_statuses:
            print("Invalid status.")
            return

        task["status"] = status

        print("Task status updated successfully!")

    def show_tasks(self, tasks=None):

        records = self.tasks if tasks is None else tasks

        if not records:
            print("No tasks found.")
            return

        for task in records:
            print("-------------------------")
            print("Task ID:", task["id"])
            print("Title:", task["title"])
            print("Employee ID:", task["employee_id"])
            print("Status:", task["status"])