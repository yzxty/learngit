# 1.��ѯͬʱ����1�γ̺�2�γ̵����
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 2.��ѯͬʱ����1�γ̺�2�γ̵����
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 3.��ѯƽ���ɼ����ڵ���60�ֵ�ͬѧ��ѧ����ź�ѧ��������ƽ���ɼ�
select studentId,name , avg(score) avgscore
from student_course
left join student on student.id=student_course.studentId
group by student_course.studentId,name
having avg(score)>=60 order by studentId

# 4.��ѯ��student_course���в����ڳɼ���ѧ����Ϣ��SQL���
select *from student
where student.id not in (select studentId from student_course) 

# 5.��ѯ�����гɼ���SQL
select *from student
where student.id in (select studentId from student_course) 

# 6.��ѯѧ�����Ϊ1����Ҳѧ�����Ϊ2�Ŀγ̵�ͬѧ����Ϣ
select * from student 
where student.id in (
select t1.studentId from student_course t1
left join student_course t2 
on t1.studentId=t2.studentId 
where  t1.courseId=1
and t2.courseId=2)

# 7.����1�γ̷���С��60���������������е�ѧ����Ϣ
select id,name,age,sex,courseId,score from student
left join student_course 
on student_course.studentId=student.id
where student_course.score<60
and student_course.courseId=1
ORDER  BY  score  DESC


# 8.��ѯÿ�ſγ̵�ƽ���ɼ��������ƽ���ɼ��������У�ƽ���ɼ���ͬʱ�����γ̱����������
select course.id,course.name ,avg(score) avgscore from course
left join student_course
on course.id=student_course.courseId
group by course.id,course.name
ORDER  BY  avgscore  DESC,id asc

# 9.��ѯ�γ�����Ϊ"��ѧ"���ҷ�������60��ѧ�������ͷ���
select course.name,score,student.name from student_course
left join course
on student_course.courseId=course.id
left join student
on student_course.studentId=student.id
where course.name='��ѧ' 
and score<60