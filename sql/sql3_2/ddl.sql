/*1. DDL*/
/************数据库级别*************/

-- 显示所有数据库 --
show databases;

-- 进入某个数据库 --
use student_examination_sys;

-- 创建一个数据库 --
create database test1;

-- 创建指定字符集的数据库 --
create database test2 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;

-- 显示数据库的创建信息 --
show create database test2;

-- 修改数据库的编码 --
alter database test2 character set utf8;

-- 删除一个数据库 --
drop database test1;

/**************表级别*************/
-- 修改表名 --
alter table student rename to stu;

-- 修改字段的数据类型 --
alter table stu modify column name char(10);

-- 修改字段名 --
ALTER TABLE stu CHANGE name stu_name varchar(12);

-- 添加字段 --
alter table   stu add teacher varchar(12);

-- 删除字段 --
alter table stu drop teacher;

-----修改表的存储引擎---
alter table stu engine=innodb;

-- 删除表的外键约束 --
alter table score drop foreign key stu_id;

-- 删除一张表 --
drop table stu;
