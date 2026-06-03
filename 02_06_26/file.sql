-- rdbms : sql (Structured Quary language) : 
-- used to interact with relational databases
-- ddl : CREATE ,ALTER, DROP,TRUNCATE,RENAME
-- REMOVE(DELETE) TABLE OR DATABASE 
-- TRUNCATE remove data from the table
-- dml : INSERT, UPDATE, DELETE , MERGE 
-- dql : SELECT 
-- dcl : GRANT , REVOKE
-- tcl : COMMIT , ROLLBACK, SAVEPOINT,SET TRANSACTION
-- Show databases
show databases;
-- Create database
CREATE DATABASE IF NOT EXISTS Employee;
-- select database where want to perform operations 
USE Employee;
-- Create table
CREATE TABLE IF NOT EXISTS Employee(
	EmpId INT,
    Name VARCHAR(50)
);

-- alter salary 
ALTER TABLE Employee 
Add Salary DECIMAL(10,2);

-- show table descriptions 
DESCRIBE Employee;

-- INSERT 
INSERT INTO Employee VALUES (1,"Akash Tiwari",100);

SET SQL_SAFE_UPDATES = 0 ; 
-- SET SQL_SAFE_UPDATES = 1;

-- Show the data of table 
SELECT * FROM Employee;

UPDATE Employee 
SET salary = 60000
WHERE EmpId = 1;

DELETE FROM Employee WHERE EmpId =1;
SELECT * FROM Employee;

-- create user 
CREATE USER 'user1'@'localhost'
IDENTIFIED BY 'password121212';

GRANT SELECT,INSERT ,DELETE,UPDATE  ON Employee.Employee 
TO 'user1'@'localhost';
