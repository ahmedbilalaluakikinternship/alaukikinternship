
-- ==========================================
-- DAY 17: FINAL DATABASE SCHEMA
-- Employee & Task Management System
-- ==========================================

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS employee_task_management;

USE employee_task_management;


-- 2. Employees Table
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


-- 3. Projects Table
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


-- 4. Tasks Table
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


-- 5. Project Members Table
-- Many-to-Many Relationship

CREATE TABLE IF NOT EXISTS project_members (
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    assigned_date DATE NOT NULL,
    role VARCHAR(50) DEFAULT 'Member',

    PRIMARY KEY (employee_id, project_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);


-- 6. Verify Database Tables

SHOW TABLES;

DESC employees;
DESC projects;
DESC tasks;
DESC project_members;
