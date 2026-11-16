
import mysql.connector


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bilal@4311",
            database="employee_task_management"
        )

        if connection.is_connected():
            print("MySQL Database Connected Successfully!")

        return connection

    except mysql.connector.Error as error:
        print("Database Connection Error:", error)
        return None


# Main execution block
if __name__ == "__main__":

    connection = create_connection()

    if connection:
        connection.close()
        print("Database Connection Closed Successfully!")

def fetch_employees():
    connection = create_connection()

    if connection:
        cursor = None

        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM employees")

            employees = cursor.fetchall()

            print("\nEmployee Records:")

            for employee in employees:
                print(employee)

        except mysql.connector.Error as error:
            print("Query Execution Error:", error)

        finally:
            if cursor:
                cursor.close()

            connection.close()


if __name__ == "__main__":
    fetch_employees()
