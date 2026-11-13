
import unittest

from employee_task_manager.task import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task(
            "Create Login Page", "Ahmed"
        )

        self.assertEqual(
            task["title"], "Create Login Page"
        )

        self.assertEqual(
            task["assigned_to"], "Ahmed"
        )

        self.assertEqual(
            task["status"], "Pending"
        )

    def test_get_task(self):
        task = self.manager.add_task(
            "Create Dashboard", "Ahmed"
        )

        result = self.manager.get_task(task["id"])

        self.assertEqual(result, task)

    def test_update_status(self):
        task = self.manager.add_task(
            "Create API", "Ahmed"
        )

        updated = self.manager.update_status(
            task["id"], "Completed"
        )

        self.assertEqual(
            updated["status"], "Completed"
        )

    def test_empty_task_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("", "Ahmed")


if __name__ == "__main__":
    unittest.main()
