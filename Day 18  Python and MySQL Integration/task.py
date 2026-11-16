
from database.db_connection import create_connection


# CREATE TASK
def add_task(
    task_title,
    description,
    employee_id,
    project_id,
    priority="Medium",
    status="Pending",
    due_date=None
):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO tasks
            (task_title, description, employee_id,
             project_id, priority, status, due_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            task_title,
            description,
            employee_id,
            project_id,
            priority,
            status,
            due_date
        )

        cursor.execute(query, values)
        connection.commit()

        print("Task Added Successfully!")
        print("Task ID:", cursor.lastrowid)

    except Exception as error:
        connection.rollback()
        print("Error Adding Task:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# READ ALL TASKS
def get_all_tasks():

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            SELECT task_id, task_title, description,
                   employee_id, project_id,
                   priority, status, due_date
            FROM tasks
            ORDER BY task_id
        """

        cursor.execute(query)
        tasks = cursor.fetchall()

        print("\n========== ALL TASKS ==========")

        if not tasks:
            print("No Tasks Found!")

        for task in tasks:
            print(task)

    except Exception as error:
        print("Error Fetching Tasks:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# READ TASK BY ID
def get_task_by_id(task_id):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM tasks WHERE task_id = %s"

        cursor.execute(query, (task_id,))
        task = cursor.fetchone()

        if task:
            print("\nTask Details:")
            print(task)
        else:
            print("Task Not Found!")

    except Exception as error:
        print("Error Fetching Task:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# UPDATE TASK STATUS
def update_task_status(task_id, status):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE tasks
            SET status = %s
            WHERE task_id = %s
        """

        cursor.execute(query, (status, task_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Task Status Updated Successfully!")
        else:
            print("Task Not Found!")

    except Exception as error:
        connection.rollback()
        print("Error Updating Task:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()


# DELETE TASK
def delete_task(task_id):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = "DELETE FROM tasks WHERE task_id = %s"

        cursor.execute(query, (task_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Task Deleted Successfully!")
        else:
            print("Task Not Found!")

    except Exception as error:
        connection.rollback()
        print("Error Deleting Task:", error)

    finally:
        if cursor:
            cursor.close()
        connection.close()
