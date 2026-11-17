# Database Setup and Backup Procedures

## 1. Database Information

- Database: MySQL
- Database Name: employee_task_management
- Host: localhost
- Username: root

## 2. Database Setup

1. Install MySQL Server.
2. Open MySQL Workbench.
3. Connect to the local MySQL server.
4. Create the database:

```sql
CREATE DATABASE employee_task_management;
```

5. Select the database:

```sql
USE employee_task_management;
```

6. Run the required table creation SQL queries.

## 3. Database Backup

Use the following command to create a database backup:

```bash
mysqldump -u root -p employee_task_management > backup.sql
```

Enter the MySQL password when prompted.

## 4. Database Restore

First, create the database if it does not exist:

```sql
CREATE DATABASE employee_task_management;
```

Restore the backup using:

```bash
mysql -u root -p employee_task_management < backup.sql
```

## 5. Security Practices

- Never upload database passwords to GitHub.
- Store credentials in a `.env` file.
- Add `.env` to `.gitignore`.
- Keep database backups private.
- Use `.env.example` to share sample configuration.

## 6. Conclusion

Database setup, backup, restore, and basic security procedures are documented for the Employee & Task Management System.