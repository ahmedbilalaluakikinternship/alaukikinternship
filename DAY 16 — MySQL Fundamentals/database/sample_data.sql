
USE employee_task_management_db;


-- 1. INSERT EMPLOYEES

INSERT INTO employees
(full_name, email, phone, department, salary, joining_date, status)
VALUES
('Ahmed Bilal', 'ahmed@gmail.com', '9876543210', 'IT', 25000, '2026-10-26', 'Active'),
('Rahul Sharma', 'rahul@gmail.com', '9876543211', 'HR', 30000, '2026-09-15', 'Active'),
('Priya Verma', 'priya@gmail.com', '9876543212', 'Development', 35000, '2026-08-10', 'Active'),
('Aman Khan', 'aman@gmail.com', '9876543213', 'Testing', 28000, '2026-07-20', 'Active'),
('Neha Jain', 'neha@gmail.com', '9876543214', 'Design', 32000, '2026-06-05', 'Inactive');


-- 2. INSERT PROJECTS

INSERT INTO projects
(project_name, description, start_date, end_date, budget, status)
VALUES
('Employee Management System', 'Manage employees and tasks', '2026-10-26', '2027-01-26', 100000, 'In Progress'),
('E-Commerce Website', 'Online shopping platform', '2026-11-01', '2027-02-01', 150000, 'Pending'),
('Portfolio Website', 'Personal portfolio development', '2026-10-15', '2026-12-15', 50000, 'In Progress');


-- 3. INSERT TASKS

INSERT INTO tasks
(task_title, description, employee_id, project_id, priority, status, due_date)
VALUES
('Create Login Page', 'Develop login interface', 1, 1, 'High', 'Completed', '2026-11-20'),
('Create Dashboard', 'Develop employee dashboard', 1, 1, 'High', 'In Progress', '2026-11-25'),
('Design Homepage', 'Create website homepage', 5, 2, 'Medium', 'Pending', '2026-12-01'),
('Develop Employee Module', 'Create employee module', 3, 1, 'High', 'In Progress', '2026-12-05'),
('Test Login Functionality', 'Perform login testing', 4, 1, 'Medium', 'Pending', '2026-11-28'),
('Create HR Report', 'Generate HR report', 2, 1, 'Low', 'Pending', '2026-12-10');


-- VERIFY SAMPLE DATA

SELECT * FROM employees;
SELECT * FROM projects;
SELECT * FROM tasks;
