
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('./iris.csv')

# Sepal
setosa = iris.loc[iris['Name']=='Iris-setosa']
versicolor = iris.loc[iris['Name']=='Iris-versicolor']
virginica = iris.loc[iris['Name']=='Iris-virginica']

plt.scatter(setosa['SepalLength'], setosa['SepalWidth'], color='blue', label='Iris-setosa') #前50个样本
plt.scatter(versicolor['SepalLength'],versicolor['SepalWidth'], color='yellow', label='Iris-versicolor') #中间50个
plt.scatter(virginica['SepalLength'], virginica['SepalWidth'],color='red', label='Iris-Virginica') #后50个样本
plt.legend() #右上角
plt.xlabel('SepalLength')
plt.ylabel('SepalWidth')
plt.show()

# Sepal
plt.scatter(setosa['PetalLength'], setosa['PetalWidth'], color='blue', label='Iris-setosa') #前50个样本
plt.scatter(versicolor['PetalLength'],versicolor['PetalWidth'], color='yellow', label='Iris-versicolor') #中间50个
plt.scatter(virginica['PetalLength'], virginica['PetalWidth'],color='red', label='Iris-Virginica') #后50个样本
plt.legend() #右上角
plt.xlabel('PetalLength')
plt.ylabel('PetalWidth')
plt.show()




