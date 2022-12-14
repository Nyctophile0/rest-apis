create table users (
id int auto_increment,
username varchar(50),
password varchar(50) not null,
primary key(id)
)

select * from users

insert into users (username, password) values("user1", "pass1")