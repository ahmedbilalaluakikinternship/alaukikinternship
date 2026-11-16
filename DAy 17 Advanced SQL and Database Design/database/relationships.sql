
-- DAY 17: DATABASE RELATIONSHIPS
USE employee_task_management;

-- Relationship 1:
-- One Employee can have Multiple Tasks

SELECT
    e.employee_id,
    e.full_name,
    t.task_title
FROM employees e
INNER JOIN tasks t
    ON e.employee_id = t.employee_id;


-- Relationship 2:
-- One Project can have Multiple Tasks

SELECT
    p.project_id,
    p.project_name,
    t.task_title
FROM projects p
INNER JOIN tasks t
    ON p.project_id = t.project_id;


-- Relationship 3:
-- Many-to-Many Employees and Projects

SELECT
    e.full_name,
    p.project_name,
    pm.role,
    pm.assigned_date
FROM employees e
INNER JOIN project_members pm
    ON e.employee_id = pm.employee_id
INNER JOIN projects p
    ON pm.project_id = p.project_id;


-- Verify Project Members
SELECT * FROM project_members;
