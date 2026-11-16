
-- DAY 17: SUBQUERIES AND CTE
USE employee_task_management;

-- 1. Subquery
-- Employees earning above average salary

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- 2. Subquery
-- Employees who have at least one task

SELECT *
FROM employees
WHERE employee_id IN (
    SELECT employee_id
    FROM tasks
);


-- 3. CTE
-- Employee-wise task count

WITH employee_task_counts AS (
    SELECT
        employee_id,
        COUNT(*) AS total_tasks
    FROM tasks
    GROUP BY employee_id
)
SELECT
    e.employee_id,
    e.full_name,
    COALESCE(c.total_tasks, 0) AS total_tasks
FROM employees e
LEFT JOIN employee_task_counts c
    ON e.employee_id = c.employee_id;


-- 4. CTE
-- Project-wise task count

WITH project_task_counts AS (
    SELECT
        project_id,
        COUNT(*) AS total_tasks
    FROM tasks
    GROUP BY project_id
)
SELECT
    p.project_id,
    p.project_name,
    COALESCE(pt.total_tasks, 0) AS total_tasks
FROM projects p
LEFT JOIN project_task_counts pt
    ON p.project_id = pt.project_id;
