import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier

X,y=datasets.load_iris(return_X_y=True) 
target_names=datasets.load_iris().target_names 
feature_names=datasets.load_iris().feature_names 
print('target name:',target_names)
print('feature names:',feature_names)

#决策树
feature_train, feature_test, target_train, target_test = train_test_split(X,y,test_size=0.30, random_state=42)
dt_model = DecisionTreeClassifier(
    max_depth=3, # 深度
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0,
    max_leaf_nodes=None,
    min_impurity_decrease=0
)  # 决策树的参数
dt_model.fit(feature_train, target_train)  # 使用训练集训练模型
predict_results = dt_model.predict(feature_test)  # 使用模型对测试集进行预测
scores = dt_model.score(feature_test, target_test)
print('scores:',scores)

#test
test = [[6.0,1.0,3.0,2.0]]
test_result = dt_model.predict(test)
if (test_result == 0):
    print("is setosa")
elif(test_result == 1):
    print("is versicolor")
else:
    print("is virginca")

#可视化
tree.plot_tree(dt_model)
plt.show()
plt.savefig('D:\python\venv\onlinelearning\sklearn1.jpg')
