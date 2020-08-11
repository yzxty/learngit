# 1.查询同时存在1课程和2课程的情况
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 2.查询同时存在1课程和2课程的情况
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select studentId,name , avg(score) avgscore
from student_course
left join student on student.id=student_course.studentId
group by student_course.studentId,name
having avg(score)>=60 order by studentId

# 4.查询在student_course表中不存在成绩的学生信息的SQL语句
select *from student
where student.id not in (select studentId from student_course) 

# 5.查询所有有成绩的SQL
select *from student
where student.id in (select studentId from student_course) 

# 6.查询学过编号为1并且也学过编号为2的课程的同学的信息
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 7.检索1课程分数小于60，按分数降序排列的学生信息
select id,name,age,sex,courseId,score from student
left join student_course 
on student_course.studentId=student.id
where student_course.score<60
and student_course.courseId=1
ORDER  BY  score  DESC


# 8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select course.id,course.name ,avg(score) avgscore from course
left join student_course
on course.id=student_course.courseId
group by course.id,course.name
ORDER  BY  avgscore  DESC,id asc

# 9.查询课程名称为"数学"，且分数低于60的学生姓名和分数
select course.name,score,student.name from student_course
left join course
on student_course.courseId=course.id
left join student
on student_course.studentId=student.id
where course.name='数学' 
and score<60