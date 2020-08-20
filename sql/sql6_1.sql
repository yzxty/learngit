
# 导入数据
create database movieLens

drop table movie
# 建立movie表，并导入数据
create table movie (
movieId int primary key,
title varchar(250),
genres varchar(250))
load data LOCAL INFILE 'D:/python/venv/onlinelearning/MovieLens/ml-25m/movies.csv' into table movie 
FIELDS TERMINATED by ','
LINES TERMINATED by '\r\n'
IGNORE 1 LINES;

# 建立用户标签表
create table tag (
userId int ,
movieId int,
tag varchar(250),
timestamp int)
load data LOCAL INFILE 'D:/python/venv/onlinelearning/MovieLens/ml-25m/tags.csv' into table tag
FIELDS TERMINATED by ','
LINES TERMINATED by '\r\n'
IGNORE 1 LINES;


# 建立用户评价表
create table rating (
userId int ,
movieId int,
rating float,
timestamp int)
load data LOCAL INFILE 'D:/python/venv/onlinelearning/MovieLens/ml-25m/ratings.csv' into table rating 
FIELDS TERMINATED by ','
LINES TERMINATED by '\r\n'
IGNORE 1 LINES;



# 建立电影链接表
create table link(
movieId int,
imdbId int,
tmbdId int)
load data LOCAL INFILE 'D:/python/venv/onlinelearning/MovieLens/ml-25m/links.csv' into table link 
FIELDS TERMINATED by ','
LINES TERMINATED by '\r\n'
IGNORE 1 LINES;


#  一共有多少不同的用户
select count(distinct userID) from (
select userId from tag 
union 
select userId from rating ) as temp_user

# 一共有多少不同的电影
select count(distinct movieId) from movie

# 一共有多少不同的电影种类
select count(distinct genre) from (
SELECT  SUBSTRING_INDEX(SUBSTRING_INDEX(movie.genres,'|',helpTopic.help_topic_id+1),'|',-1) as genre FROM movie
left join mysql.help_topic helpTopic
on helpTopic.help_topic_id < (LENGTH(movie.genres)-LENGTH(REPLACE(movie.genres,'|',''))+1)) as temp_genre;


# 一共有多少电影没有外部链接
select count(distinct movieId) from movie
where movieId not in (select movieId from link);



# 2018年一共有多少人进行过电影评分
select count(distinct userId) from rating
where timestamp >= (select unix_timestamp('2018-01-01 00:00:00')) and timestamp < (select unix_timestamp('2019-01-01 00:00:00'));


# 2018年评分5分以上的电影及其对应的标签
select movie.movieId , movie.title , avg_rating , tags
from temp_rating 
LEFT JOIN movie on temp_rating.movieId = movie.movieId
LEFT JOIN 
(select movieId,GROUP_CONCAT(DISTINCT tag) as tags from tag
where timestamp >= (select unix_timestamp('2018-01-01 00:00:00'))  and  timestamp < (select unix_timestamp('2019-01-01 00:00:00')) 
group by movieId) as temp_tag
on temp_tag.movieId = temp_rating.movieId
