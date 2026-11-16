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