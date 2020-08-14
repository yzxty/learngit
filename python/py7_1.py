import pandas as pd
import time, datetime

# 读取数据
tags = pd.read_csv('D:/python/venv/onlinelearning/MovieLens/ml-25m/tags.csv')#获取用户对电影的tag
ratings = pd.read_csv('D:/python/venv/onlinelearning/MovieLens/ml-25m/ratings.csv')#获取用户对电影的评价
movies = pd.read_csv('D:/python/venv/onlinelearning/MovieLens/ml-25m/movies.csv')#获取电影信息
links = pd.read_csv('D:/python/venv/onlinelearning/MovieLens/ml-25m/links.csv')#获取电影链接信息


# 1、 一共有多少不同的用户
tags_user = tags['userId']
ratings_user = ratings['userId']
temp_user = tags_user.append(ratings_user)#拼接两份用户id
print('用户数：',len(temp_user.drop_duplicates()))#输出去重后的长度

# 2、一共有多少不同的电影
movieId = movies['movieId']
print('电影数：',len(movieId.drop_duplicates()))#防止重复ID

# 3、一共有多少不同的电影种类
genres_arg = movies['genres']
temp_genres=genres_arg.str.split("|").tolist()
genres=list(set([i for j in temp_genres for i in j ]))
print('电影种类数：',len(genres))


# 4、一共有多少电影没有外部链接
movie_link=pd.merge(movies, links, how='left',on='movieId')
movie_link_has=movie_link[movie_link['imdbId'].notna()]

print('电影无链接数：',len(movie_link)-len(movie_link_has))


# 5、2018年一共有多少人进行过电影评分
# 获取18年的时间戳范围
star_time=time.strptime("2018-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
end_time=time.strptime("2019-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
star_ts=int(time.mktime(star_time))
end_ts=int(time.mktime(end_time))
user2018=ratings.loc[(ratings["timestamp"] < end_ts) & (ratings["timestamp"] >= star_ts)]

print('2018年评分人数：',len(user2018.drop_duplicates(['userId'])))
