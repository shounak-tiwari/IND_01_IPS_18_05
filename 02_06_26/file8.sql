use Batch2DB;

create table if not exists product (
	proId int primary key auto_increment,
    proName varchar(50),
    proPrice decimal(10,2)
);

insert into product(proName,proPrice) 
values
('AC',12500),
('laptop',25500),
('watch',1500),
('phone',10000);

select * from product;

-- Transtraction 
start transaction;
insert into product(proName,proPrice)  values('mouse',290);

rollback;
commit;

start transaction;
delete from product where proId = 1;
select * from product;
rollback;
commit;

start transaction;
savepoint sp1;
select * from product;
rollback to sp1;
insert into product(proName,proPrice)  values('earphones',2090);



select * from product;
start transaction;
savepoint sp1;
insert into product(proName,proPrice) 
values 
('coffee',20);
rollback to sp1;

commit;

rollback;

