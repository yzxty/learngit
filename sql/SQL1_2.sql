create database student_examination_sys

------------建立学生表并插入数据-------------
create table student (
id char(3) NOT NULL primary key,
name char(10) NOT NULL,
age int CHECK(age>0),
sex char(2) NOT NULL CHECK(sex='男'or sex='女')
)
insert into student values('001','张三',18,'男')
insert into student values('002','李四',20,'女')

------------建立考试科目表并插入数据------------
create table subject (
id char(4) NOT NULL primary key,
subject char(10) NOT NULL,
teacher char(10) NOT NULL,
description varchar(100)
)
insert into subject values('1001','语文','王老师','本次考试比较简单')
insert into subject values('1002','数学','刘老师','本次考试比较难')

------------建立考试科目表并插入数据------------
create table score (
id int NOT NULL,
student_id char(3) NOT NULL foreign key references student(id),
subject_id char(4) NOT NULL foreign key references subject(id),
score float NOT NULL
)
insert into score values(1,'001','1001','80')
insert into score values(2,'002','1002','60')
insert into score values(3,'001','1001','70')
insert into score values(4,'002','1002','60.5')

select * from student
select * from subject
select * from score
