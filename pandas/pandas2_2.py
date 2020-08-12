import pandas as pd

#导入数据
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
tags = pd.read_csv('tags.csv')

#计算平均分
avg_ratings=ratings.groupby(['movieId'],as_index=False)['rating'].agg({'avg_rating':'mean'})#ID,平均分
#计算tag字符串
temp_data=pd.merge(tags, movies, how='left',on='movieId')
all_tags=temp_data.groupby('movieId')['tag'].apply(lambda x:x.str.cat(sep='|')).reset_index()#ID,tag串

#多表依据movieId连接
result_temp=pd.merge(movies, avg_ratings, how='left',on='movieId')
result_temp=pd.merge(result_temp, all_tags, how='left',on='movieId')

#去除多余的列，得到电影ID、电影名称、平均分、所有tag（注：数据集没有主演）
result_data=result_temp.drop(['genres'],axis=1)
pd.options.display.max_columns =None
print(result_data)
