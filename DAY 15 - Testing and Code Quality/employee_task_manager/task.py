
class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, assigned_to):
        if not title:
            raise ValueError("Task title cannot be empty")

        if not assigned_to:
            raise ValueError("Employee name is required")

        task = {
            "id": self.next_id,
            "title": title,
            "assigned_to": assigned_to,
            "status": "Pending"
        }

        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task

        return None

    def update_status(self, task_id, status):
        valid_statuses = ["Pending", "In Progress", "Completed"]

        if status not in valid_statuses:
            raise ValueError("Invalid task status")

        task = self.get_task(task_id)

        if task is None:
            raise ValueError("Task not found")

        task["status"] = status
        return task
