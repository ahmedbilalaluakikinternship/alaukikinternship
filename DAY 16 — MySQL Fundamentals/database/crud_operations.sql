
USE employee_task_management_db;


-- ==================================
-- CREATE (INSERT)
-- ==================================

INSERT INTO employees
(full_name, email, phone, department, salary, joining_date)
VALUES
('Rohit Patel', 'rohit@gmail.com', '9876543215',
 'Development', 27000, '2026-11-13');


-- ==================================
-- READ (SELECT)
-- ==================================

-- Display all employees
SELECT * FROM employees;

-- Display selected columns
SELECT full_name, email, salary FROM employees;

-- Find employees by department
SELECT * FROM employees
WHERE department = 'Development';

-- Sort employees by salary
SELECT * FROM employees
ORDER BY salary DESC;

-- Display top 3 highest-paid employees
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 3;


-- ==================================
-- UPDATE
-- ==================================

-- Update employee salary
UPDATE employees
SET salary = 30000
WHERE employee_id = 1;

-- Update employee department
UPDATE employees
SET department = 'Python Development'
WHERE employee_id = 1;


-- ==================================
-- DELETE
-- ==================================

-- Delete employee with ID 6
-- Only if the employee has no assigned tasks

DELETE FROM employees
WHERE employee_id = 6;


-- ==================================
-- PROJECT CRUD
-- ==================================

-- Create
INSERT INTO projects
(project_name, description, start_date, budget, status)
VALUES
('AI Chatbot', 'Customer support chatbot',
 '2026-11-13', 75000, 'Pending');

-- Read
SELECT * FROM projects;

-- Update
UPDATE projects
SET status = 'In Progress'
WHERE project_id = 2;

-- Delete only if no tasks reference this project
DELETE FROM projects
WHERE project_id = 3;


-- ==================================
-- TASK CRUD
-- ==================================

-- Create
INSERT INTO tasks
(task_title, description, employee_id, project_id,
 priority, status, due_date)
VALUES
('Create Registration Page', 'Develop registration form',
 1, 1, 'High', 'Pending', '2026-12-15');

-- Read
SELECT * FROM tasks;

-- Update
UPDATE tasks
SET status = 'Completed'
WHERE task_id = 2;

-- Delete
DELETE FROM tasks
WHERE task_id = 6;
