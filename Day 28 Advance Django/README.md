# Day 28 — Advanced ORM and Database Optimization

## Objective
To understand advanced Django ORM techniques and database optimization methods to improve application performance, reduce unnecessary database queries, and handle database operations efficiently.

## Topics Covered

- `select_related()` and `prefetch_related()`
- Q and F expressions
- `annotate()` and `aggregate()`
- Database transactions and atomic operations
- Bulk operations
- N+1 query problem
- Database indexing and query optimization
- Query profiling and EXPLAIN plans

## Practical Tasks

- Optimize dashboard database queries using Django ORM.
- Identify and fix N+1 query problems.
- Use `select_related()` and `prefetch_related()` to reduce unnecessary queries.
- Implement transactional task assignment using `transaction.atomic()`.
- Perform bulk database operations where appropriate.
- Compare query performance before and after optimization.
- Analyze SQL queries and execution plans.

## Project Work

Improve database efficiency in the Main Django Project by:

- Optimizing employee, project, and task dashboard queries.
- Reducing unnecessary database queries.
- Applying suitable ORM optimization techniques.
- Implementing safe and reliable database transactions.
- Improving query performance through indexing and profiling.
- Reviewing database operations to make the application more efficient.

## Project Development Structure

All practical implementations and database optimization work will be performed in the existing **Main Django Project**.

The Day 28 folder will contain daily learning documentation and related notes.

## Technologies Used

- Python
- Django
- Django ORM
- SQLite / MySQL
- SQL
- VS Code