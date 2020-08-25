import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import linear_model
import matplotlib.pyplot as plt

#数据
data_df = pd.DataFrame(datasets.load_boston()['data'],columns=datasets.load_boston()['feature_names'])
target_df = pd.DataFrame(datasets.load_boston()['target'],columns=['y'])
df=data_df.join(target_df)

x=df.loc[:,['RM','DIS','LSTAT','PTRATIO']]

plt.scatter(x['RM'],target_df,c = 'r',marker = 'o')
plt.show()
plt.scatter(x['DIS'],y_df,c = 'g',marker = 'o')
plt.show()
plt.scatter(x['LSTAT'],y_df,c = 'b',marker = 'o')
plt.show()
plt.scatter(x['PTRATIO'],y_df,c = 'y',marker = 'o')
plt.show()

xx = np.array(x)
reg = linear_model.LinearRegression()
model = reg.fit(xx, target_df)
print('系数：',model.coef_)
print('截距：',model.intercept_)

model.predict([[8, 2, 12, 22]])
model_RM = reg.fit(x[['RM']], target_df)
print('系数：',model_RM.coef_)
print('截距：',model_RM.intercept_)

