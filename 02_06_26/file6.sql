-- dml : INSERT, UPDATE, DELETE , MERGE 
-- manupulate data 
--  avg , sum , max , min 

create database Batch2Db;
use batch2db;
create table employee(
	EmpId int primary key,
    Name varchar(50) ,
    Salary decimal(10,2)
);
insert into employee(EmpId,Name,Salary)
values 
(101,'Rahul',50000),
(102,'Arpit',45000),
(103,'AsimSir','150000'),
(104,'Himanshu',35000);

update employee
set Salary = 55000
where EmpId =101;

select * from employee;

delete from employee 
where EmpId = 101;

create table NewEmployee(
	EmpId int primary key,
    Name varchar(50) ,
    Salary decimal(10,2)
);
insert into NewEmployee(EmpId,Name,Salary)
values 
(101,'Rahul',60000),
(102,'Arpit',65000),
(103,'AsimSir','170000'),
(104,'Himanshu',55000);


insert into NewEmployee(EmpId,Name,Salary)
values 
(111,'Aditya',60000),
(112,'Ayush',65000),
(113,'Sumit','170000'),
(114,'Kuch',55000);




-- MERGE INTO Employee E 
-- USING NewEmployee N 
-- on (E.EmpId=N.EmpId)
-- WHEN MATCHED THEN
-- 	update set E.Salary = N.salary 
-- WHEN NOT MATCHED THEN
-- 	INSERT(EmpId,Name,Salary)
--     Values(N.EmpId,N.Name,N.Salary);


-- duplicate in place of merge