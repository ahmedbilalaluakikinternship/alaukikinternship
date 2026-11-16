
CREATE DATABASE IF NOT EXISTS employee_task_management_db;

USE employee_task_management_db;


-- 1. EMPLOYEES TABLE

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) UNIQUE,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) CHECK (salary >= 0),
    joining_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Active'
);


-- 2. PROJECTS TABLE

CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(12,2) CHECK (budget >= 0),
    status VARCHAR(20) DEFAULT 'Pending',

    CHECK (end_date IS NULL OR end_date >= start_date)
);


-- 3. TASKS TABLE

CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_title VARCHAR(150) NOT NULL,
    description TEXT,
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    priority VARCHAR(20) DEFAULT 'Medium',
    status VARCHAR(20) DEFAULT 'Pending',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id),

    CHECK (priority IN ('Low', 'Medium', 'High')),

    CHECK (status IN ('Pending', 'In Progress', 'Completed'))
);




SHOW TABLES;

DESC employees;
DESC projects;
DESC tasks;
