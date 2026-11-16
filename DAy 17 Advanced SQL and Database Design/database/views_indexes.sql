
-- DAY 17: VIEWS, INDEXES AND QUERY ANALYSIS
USE employee_task_management;

-- 1. Employee Workload View

CREATE OR REPLACE VIEW vw_employee_workload AS
SELECT
    e.employee_id,
    e.full_name,
    e.department,
    COUNT(t.task_id) AS total_tasks
FROM employees e
LEFT JOIN tasks t
    ON e.employee_id = t.employee_id
GROUP BY
    e.employee_id,
    e.full_name,
    e.department;


-- 2. Project Summary View

CREATE OR REPLACE VIEW vw_project_summary AS
SELECT
    p.project_id,
    p.project_name,
    COUNT(DISTINCT pm.employee_id) AS total_employees,
    COUNT(DISTINCT t.task_id) AS total_tasks
FROM projects p
LEFT JOIN project_members pm
    ON p.project_id = pm.project_id
LEFT JOIN tasks t
    ON p.project_id = t.project_id
GROUP BY
    p.project_id,
    p.project_name;


-- 3. Employee Project Details View

CREATE OR REPLACE VIEW vw_employee_projects AS
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


-- 4. Read Views

SELECT * FROM vw_employee_workload;
SELECT * FROM vw_project_summary;
SELECT * FROM vw_employee_projects;


-- 5. Useful Indexes
-- These indexes were created during practical work.
-- Do not execute CREATE INDEX again if they already exist.

-- CREATE INDEX idx_employees_department
-- ON employees(department);

-- CREATE INDEX idx_projects_status
-- ON projects(status);

-- CREATE INDEX idx_tasks_status_due_date
-- ON tasks(status, due_date);


-- 6. Verify Existing Indexes

SHOW INDEX FROM employees;
SHOW INDEX FROM projects;
SHOW INDEX FROM tasks;
SHOW INDEX FROM project_members;


-- 7. EXPLAIN: Employee Workload Query

EXPLAIN
SELECT
    e.employee_id,
    e.full_name,
    COUNT(t.task_id) AS total_tasks
FROM employees e
LEFT JOIN tasks t
    ON e.employee_id = t.employee_id
GROUP BY
    e.employee_id,
    e.full_name;


-- 8. EXPLAIN: Task Search Query

EXPLAIN
SELECT *
FROM tasks
WHERE status = 'Pending'
AND due_date >= '2026-11-01';
