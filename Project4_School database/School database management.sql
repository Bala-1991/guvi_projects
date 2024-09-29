admin-- Create Database
CREATE DATABASE school_dbms;

-- Use the new Database
USE school_dbms;

-- Create Admin Table
CREATE TABLE admin (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Create Student Table
CREATE TABLE student (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK(age > 0 AND age < 120),
    sex ENUM('Male', 'Female', 'Other') NOT NULL,
    class VARCHAR(10) NOT NULL,
    fees DECIMAL(10,2) NOT NULL CHECK(fees >= 0),
    `rank` INT NOT NULL CHECK(`rank` > 0),
    english_mark INT NOT NULL CHECK(english_mark BETWEEN 0 AND 100),
    python_mark INT NOT NULL CHECK(python_mark BETWEEN 0 AND 100),
    math_mark INT NOT NULL CHECK(math_mark BETWEEN 0 AND 100),
    class_teacher VARCHAR(255) NOT NULL
);

-- Create Teacher Table
CREATE TABLE teacher (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK(age > 0 AND age < 120),
    sex ENUM('Male', 'Female', 'Other') NOT NULL,
    salary DECIMAL(10,2) NOT NULL CHECK(salary >= 0),
    class_teacher_class VARCHAR(255) NOT NULL
);

-- Create Principal Table
CREATE TABLE principal (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK(age > 0 AND age < 120),
    sex ENUM('Male', 'Female', 'Other') NOT NULL,
    salary DECIMAL(10,2) NOT NULL CHECK(salary >= 0)
);

-- Insert Default Admin User (For testing)
INSERT INTO admin (user_name, password) VALUES ('admin', 'admin123');
