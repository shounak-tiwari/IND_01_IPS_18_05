-- mysql : soft for managing relational database 
-- sql : Structured quary language

-- fundamental quary of RDBMS 

-- create database 
show databases;

-- creating database 
create database Batch2DB;

-- select database or use database 
use Batch2DB;

-- creating tables into database 
-- create table tableName (
-- 	colsName datatype constraints
-- )
create table Student(
    EnrollmentNumber varchar(50) primary key,
    StudentName varchar(50) not null,
    Contact bigint
);
-- Describe the table
desc Student;

-- insert the data into data table 
insert into Student(EnrollmentNumber,StudentName,Contact) 
values
('0808cs241300','MySql',1234),
('0808cs241301','NoSql',1234),
('0808cs241302','PostgreSql',1234),
('0808cs241303','PLSQL',1234),
('0808cs241304','Oracle',1234),
('0808cs241305','MySql Developer',1234);

-- data print or select the data from table 
select * from Student;

-- data defination language : 
-- ddl : CREATE ,ALTER, DROP,TRUNCATE,RENAME
-- dml : INSERT, UPDATE, DELETE , MERGE 
-- dql : SELECT 
-- dcl : GRANT , REVOKE
-- tcl : COMMIT , ROLLBACK, SAVEPOINT,SET TRANSACTION
alter table Student 
Add Percetange DECIMAL(10,2);
-- TRUNCATE : remove the data from table 
truncate table Student;
select * from Student;
-- remove table 
drop table Student;
-- remove database 
drop database if exists Batch2DB;
