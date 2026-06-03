-- RENAME 
-- SAVEPOINT,
-- SET TRANSACTION

-- database create
CREATE DATABASE if not exists IPSEmployee;

-- select database 
use IPSEmployee;

-- data table create 
create table if not exists employees(
	EmpId int primary key,
    EmpName varchar(50)
);
-- table information or descriptions 
describe employees;

-- insert value in a table 
INSERT INTO employees(EmpId,EmpName) VALUES 
(5,'Gargree'),
(6,'Jaya'),
(7,'Lakshya'),
(8,'Pranjal');

-- DROP TABLE TABLENAME;
drop table employees;
truncate employees;
select * from employees;

-- primary key :  it is constraints of cols which is use 
-- when we want unique and not null , in a table only 
-- one primary key is valid 
-- DUPLICATE
INSERT INTO employees(EmpId,EmpName)
VALUES
(5,'Gargi'),
(1,'Akash'),
(2,'Ayush')
on duplicate key update
EmpName = values(EmpName);
select * from employees;


-- COMMIT 
start transaction;
insert into employees values (10,'Madhur');
commit;
rollback;
select * from employees;
delete from employees where EmpId = 2;

-- SAVEPOINT 
start transaction;
insert into employees values (11,'Karan');
savepoint sp1;
insert into employees values (12,'Arjun');

rollback to sp1;
select * from employees;