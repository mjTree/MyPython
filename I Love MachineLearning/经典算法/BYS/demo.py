# encoding: utf-8

"""
@version: python3.6
@author: misakalee
@contact: misakaleeaslxy@gmail.com
@file: demo.py
@time: 2018.01.24 18:39
"""
from mybayes import Fileoperation as fo
from mybayes import Bayes
filename = 'demo.csv'
dataset = fo.loadCsv(filename)#导入数据集
# 默认方式
print('##############默认方式##############')
summarizes,prediction,accuracy = Bayes.bayes(dataset,0.67)#返回
print('#######训练结果summarizes###########')
print(summarizes)
print("###################################")
print('#######预测结果prediction###########')
print(prediction)
print("###################################")
print('#######准确度accuracy###############')
print(accuracy)

# 自定义方式
print('##############自定义方式##############')
print('分割数据集')
trainSet,tsetSet = Bayes.splitDataset(dataset,0.5)
print('训练')
summarizes = Bayes.summarizeByClass(dataset)
print('预测')
###单例预测
input = [6,148,72,35,0,33.6,0.627,50]
result1 = Bayes.predict(summarizes,input)
print("input belong to {0}".format(result1))
result2 = Bayes.calculateClassProbabilities(summarizes,input)
print(result2)
result3 = Bayes.getPredictions(summarizes,dataset)
print(result3)
