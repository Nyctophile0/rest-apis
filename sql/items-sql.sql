SELECT * FROM item;

insert into item(id, name, price) values("fc8e6c4a1bdf468d970908ff6e566fef", "banana", 30)

create table item (id varchar(32),
name varchar(100),
price int,
primary key(id)
);

select * from item

insert into item (id, name, price) values("075355766ce046d3a62b999b24074a50","grapes", 45);

update item set name = "1 banana", price = 10 where id = "7929d6effab04ffb8631a2350253efdd"

delete from item where id="075355766ce046d3a62b999b24074a50"