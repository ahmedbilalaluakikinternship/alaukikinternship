
-- DAY 17: SQL TRANSACTIONS
USE employee_task_management;

-- 1. START TRANSACTION
-- Update task status and save the change

START TRANSACTION;

UPDATE tasks
SET status = 'In Progress'
WHERE task_id = 1;

SELECT *
FROM tasks
WHERE task_id = 1;

-- Permanently save transaction
COMMIT;


-- 2. ROLLBACK
-- Update task and cancel the change

START TRANSACTION;

UPDATE tasks
SET status = 'Pending'
WHERE task_id = 1;

SELECT *
FROM tasks
WHERE task_id = 1;

-- Undo the update
ROLLBACK;


-- 3. Verify Final Task Status

SELECT *
FROM tasks
WHERE task_id = 1;
