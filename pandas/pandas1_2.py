#读取rates.csv文件，完成：
# 将每1分做为一档，电影的评分共分为5档，(0:1], (1,2], (2, 3], (3, 4], (4, 5], 通过pandas包求出每个评分档共有多少部电影
# # 添加一个comment列，对平均分4分以上的电影标‘推荐’，其他标‘不推荐’，输出到一个comment.csv中

import pandas as pd

#读取数据
data = pd.read_csv('ratings.csv')

#计算不同档的电影有多少部
for i in range(0, 5):
    number=data.loc[(data["rating"] <= i+1) & (data["rating"] > i)].movieId.count()
    print("评分在[%d,%d]的电影有：%d部" %(i,i+1,number))

#增加comment列，对平均分4分以上的电影标‘推荐’，其他标‘不推荐’
#按电影id，计算评价分
data2=data.groupby(['movieId'],as_index=False)['rating'].agg({'avg_rating':'mean'})
data2.loc[:,"comment"] = data2.avg_rating.apply(lambda x: '不推荐' if x<=4 else '推荐')

#保存数据
data2.to_csv('comments.csv',index=False)



