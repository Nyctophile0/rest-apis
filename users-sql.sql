create table users (
id int auto_increment,
username varchar(50),
password varchar(50) not null,
primary key(id)
)

alter table users modify id int, drop primary key, add primary key(username)
ALTER TABLE users ADD INDEX id (id), MODIFY id int auto_increment;
ALTER TABLE users AUTO_INCREMENT = 5;
alter table users modify column password varchar(100)

select * from users
delete from users where username="user"
insert into users (username, password) values("user6", "pass5")