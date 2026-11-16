USE employee_task_management;

SELECT
    e.employee_id,
    e.full_name,
    p.project_name,
    pm.role,
    pm.assigned_date
FROM employees e
INNER JOIN project_members pm
    ON e.employee_id = pm.employee_id
INNER JOIN projects p
    ON pm.project_id = p.project_id;
    
SELECT
    e.full_name,
    p.project_name
FROM employees e
LEFT JOIN project_members pm
    ON e.employee_id = pm.employee_id
LEFT JOIN projects p
    ON pm.project_id = p.project_id;
    
SELECT
    p.project_name,
    e.full_name
FROM employees e
RIGHT JOIN project_members pm
    ON e.employee_id = pm.employee_id
RIGHT JOIN projects p
    ON pm.project_id = p.project_id;
