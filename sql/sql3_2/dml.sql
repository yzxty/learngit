/*2.DML*/

-- 插入记录 --
insert into student values ('003','王五',21,'男');

-- 修改记录 --
update student set age=25 where id = '003';

-- 删除记录 --
delete from student where id = '003';

-- 查询记录 --
select * from student;
