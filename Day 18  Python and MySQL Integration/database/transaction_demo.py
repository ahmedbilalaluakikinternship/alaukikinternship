
from database.db_connection import create_connection


def test_transaction():
    connection = create_connection()

    if connection:
        cursor = None

        try:
            cursor = connection.cursor()

            # Start transaction
            connection.start_transaction()

            cursor.execute("""
                UPDATE employees
                SET salary = 99999
                WHERE employee_id = 1
            """)

            print("Temporary salary update executed!")

            # Rollback transaction
            connection.rollback()

            print("Transaction Rolled Back Successfully!")

        except Exception as error:
            connection.rollback()
            print("Transaction Error:", error)

        finally:
            if cursor:
                cursor.close()

            connection.close()


if __name__ == "__main__":
    test_transaction()
