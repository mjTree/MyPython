#coding:utf-8
#testKNN.py

import KNN_Module as knnn


path = 'Data\\Ionosphere\\test.data' #input('请输入数据集路径：')
# path在此输入: Data\\Ionosphere\\ionosphere.data

X,y = knnn.downloadData(path)

avg_scores,all_scores,parameter_values = knnn.knnCategoricalData(X,y)

knnn.dataView(avg_scores,all_scores,parameter_values)


