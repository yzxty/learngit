import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#数据
df=pd.DataFrame(datasets.load_iris()['data'],columns=datasets.load_iris()['feature_names'])
df.head()

#聚类
k_model = KMeans(n_clusters=3).fit(df)
pre = k_model.predict(df)
center = k_model.cluster_centers_
print('聚类结果：',pre)
print('中心点：',center)
df['cluster_3'] = pre

# 可视化
colors_list = ['red', 'blue', 'green']
labels_list = ['setosa', 'versicolor', 'virginica']
df = df
dfarray = df.values
for i in range(3):
    plt.scatter(dfarray[pre==i,0], dfarray[pre== i,1], s=100,c=colors_list[i],label = labels_list[i])
plt.legend(loc=2)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.savefig('D:\python\venv\onlinelearning\sklearn2.png')
plt.show()
