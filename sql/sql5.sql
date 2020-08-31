-- 建立数据库，并导入数据
create table  student  
( id     varchar(5)  not null,
name   varchar(10),
age    int ,
sex    varchar(1)
);
insert into student(id,name,age,sex)
values( '001','张三',18,'男'),('002','李四',20,'女');

create table  subject  
( id           int  not null,
subject      varchar(10),
teacher      varchar(10),
description  varchar(20)
);
insert into subject(id,subject,teacher,description)
values( 1001,'语文','王老师','本次考试比较简单'),(1002,'数学','刘老师','本次考试比较难');

create table  score  
( id           int  not null,
  student_id   varchar(5),
  subject_id   int,
  score        float
);
insert into score(id,student_id,subject_id,score)
values( 1,'001',1001,80),(2,'002',1001,75),(3,'001',1002,70),(4,'002',1002,60.5);



/**请编写一个MySQL存储过程`calc_student_stat`计算统计数据并输出到一个新表`student_stat`中。其中需要统计的数据有：

1. avg_score: 该科目平均分
2. score: 学生在该科目下的得分
3. total_score: 学生总分
4. score_rate: 该科目得分占总分的比例

除了上述统计字段，`student_stat`表还包含字段：`name` `teacher` `subject`.   **/
create procedure calc_student_stat()
BEGIN

 DROP TEMPORARY TABLE IF EXISTS temp_table ;
 CREATE TEMPORARY TABLE temp_table  as
 SELECT t1.student_id, t1.subject_id , t1.score, avg_score, total_score,t1.score/t3.total_score score_rate 
 FROM score  as  t1
 LEFT JOIN (SELECT subject_id,avg(score) avg_score
              FROM score 
            GROUP BY subject_id)   as t2	 
 ON t1.subject_id	=	t2.subject_id
 LEFT JOIN (SELECT student_id,sum(score) total_score 
              FROM score 
            GROUP BY student_id)  as  t3 
 ON t1.student_id	=	t3.student_id;

 DROP TABLE IF EXISTS student_stat;
 CREATE TABLE student_stat as
 SELECT t2.name,t3.subject,t3.teacher,score,total_score,avg_score,score_rate
 FROM temp_table  as  t1
 LEFT JOIN student  as t2
 ON t1.student_id	= t2.id
 LEFT JOIN subject  as t3
 ON t1.subject_id = t3.id;
END;

CALL calc_student_stat() ;
select * from student_stat












