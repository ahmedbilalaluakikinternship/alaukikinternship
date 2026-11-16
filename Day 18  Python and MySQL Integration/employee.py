
from database.db_connection import create_connection


# CREATE EMPLOYEE
def add_employee(
    full_name,
    email,
    phone,
    department,
    salary,
    joining_date,
    status="Active"
):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            INSERT INTO employees
            (full_name, email, phone, department,
             salary, joining_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            full_name,
            email,
            phone,
            department,
            salary,
            joining_date,
            status
        )

        cursor.execute(query, values)
        connection.commit()

        print("Employee Added Successfully!")
        print("Employee ID:", cursor.lastrowid)

    except Exception as error:

        connection.rollback()
        print("Error Adding Employee:", error)

    finally:

        if cursor:
            cursor.close()

        connection.close()


# READ ALL EMPLOYEES
def get_all_employees():

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            SELECT * FROM employees
            ORDER BY employee_id
        """

        cursor.execute(query)

        employees = cursor.fetchall()

        print("\n========== ALL EMPLOYEES ==========")

        if not employees:
            print("No Employees Found!")

        for employee in employees:
            print(employee)

    except Exception as error:

        print("Error Fetching Employees:", error)

    finally:

        if cursor:
            cursor.close()

        connection.close()


# READ EMPLOYEE BY ID
def get_employee_by_id(employee_id):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            SELECT * FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Details:")
            print(employee)
        else:
            print("Employee Not Found!")

    except Exception as error:

        print("Error Fetching Employee:", error)

    finally:

        if cursor:
            cursor.close()

        connection.close()


# UPDATE EMPLOYEE
def update_employee(employee_id, department, salary):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            UPDATE employees
            SET department = %s,
                salary = %s
            WHERE employee_id = %s
        """

        values = (department, salary, employee_id)

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee Updated Successfully!")
        else:
            print("Employee Not Found!")

    except Exception as error:

        connection.rollback()
        print("Error Updating Employee:", error)

    finally:

        if cursor:
            cursor.close()

        connection.close()


# DELETE EMPLOYEE
def delete_employee(employee_id):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            DELETE FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee Deleted Successfully!")
        else:
            print("Employee Not Found!")

    except Exception as error:

        connection.rollback()
        print("Error Deleting Employee:", error)
        print("Check whether this employee is assigned to any tasks or projects.")

    finally:

        if cursor:
            cursor.close()

        connection.close()
