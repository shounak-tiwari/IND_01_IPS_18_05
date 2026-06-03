use Batch2DB;
create table if not exists product (
	proId int primary key auto_increment,
    proName varchar(50),
    proPrice decimal(10,2)
);
insert into product(proName,proPrice) values('Remote',125);
-- admin 
-- create user 
create user Cat
identified by 'password1234';
create user 'Cat'@'localhost'
identified by 'password12345';
-- give the pre... 
grant select on product to Cat; 
SHOW GRANTS FOR 'Cat'@'%';
revoke select on product from Cat;