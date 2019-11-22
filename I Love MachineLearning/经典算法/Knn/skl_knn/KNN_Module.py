#coding:utf-8
#KNN_Module.py

"""
@CreateTime: 2017/12/8
@UpdateTime: 2017/12/9
@author: mjTree
@needModel: csv, sys, numpy, sklearn, matplotlib
"""

import sys    # py自带的标准库
import csv
import numpy as np


"""
function : 加载用户提供的数据集
parameter : path 用户提供数据集路径,字符串
return : X 存储数据集,矩阵
return : y 存储每行数据集类别值,矩阵
"""
def downloadData(path):
    data_filename = path
    
    # 已知数据集大小,建立一个初始化矩阵保存数据集的数据
    '''
    X = np.zeros((351, 34), dtype='float')
    y = np.zeros((351,), dtype='bool')
    
    with open(data_filename, 'r') as input_file:
        reader = csv.reader(input_file)
        for i, row in enumerate(reader):
            data = [float(datum) for datum in row[:-1]]
            print(data)
            X[i] = data
            y[i] = row[-1] == 'g'
    return X,y
    '''
    data = []
    labels = []
    with open(data_filename, 'r') as input_file:
        reader = csv.reader(input_file)
        for i, row in enumerate(reader):    # i表示行数
            data.append([float(datum) for datum in row[:-1]])
            labels.append(row[-1])
    
    X = np.array(data)
    labels = np.array(labels)
    y = np.zeros(labels.shape)
    y[labels=='g']=1;y[labels=='b']=0    # 标签转化为0,1
    return X,y
    

"""
function : 通过KNN算法对数据进行分类
parameter : X 存储数据集,矩阵
parameter : y 存储每行数据集的类别值,矩阵
return : avg_scores 保存所有的近邻得分,列表
return : all_scores 保存近邻得分的平均值,列表
return : parameter_values 
"""
def knnCategoricalData(X,y):
    from sklearn.cross_validation import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)  # 拆分训练数据和测试数据
    print("训练数据集中有{}样本".format(X_train.shape[0]))
    print("测试数据集中有{}样本".format(X_test.shape[0]))
    print("每个示例都有{}特性".format(X_train.shape[1]))

    from sklearn.neighbors import KNeighborsClassifier    # 导入K近邻分类器类
    estimator = KNeighborsClassifier()    # 通过sklearn进行参数默认
    estimator.fit(X_train, y_train)       # 用训练数据进行训练

    
    '''用测试集测试算法'''
    y_predicted = estimator.predict(X_test)
    accuracy = np.mean(y_test == y_predicted) * 100
    print('精度是{0:.1f}%'.format(accuracy))

    
    '''用scikit-learn交叉检验'''
    from sklearn.cross_validation import cross_val_score
    scores = cross_val_score(estimator, X, y, scoring='accuracy')
    average_accuracy = np.mean(scores) * 100
    print('平均精度是{0:.1f}%'.format(average_accuracy))

    avg_scores = []
    all_scores = []
    parameter_values = list(range(1, 21))  # 计算K值从1-20之间的差异
    for n_neighbors in parameter_values:
        estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
        scores = cross_val_score(estimator, X, y, scoring='accuracy')
        avg_scores.append(np.mean(scores))  # 保存n_neighbors值的得分和平均分
        all_scores.append(scores)
    return avg_scores,all_scores,parameter_values


"""
function : 通过KNN算法对数据进行分类
parameter : avg_scores
parameter : all_scores
parameter : parameter_values
return : 无
"""
def dataView(avg_scores,all_scores,parameter_values):
    #绘制图形
    from matplotlib import pyplot as plt
        
    plt.figure(figsize=(8,5))
    plt.plot(parameter_values, avg_scores, '-o', linewidth=2, markersize=10)
    plt.show()
    # plt.axis([0, max(parameter_values), 0, 1.0])
    '''
    for parameter, scores in zip(parameter_values, all_scores):
        n_scores = len(scores)
        plt.plot([parameter] * n_scores, scores, '-o')
    plt.show()

    plt.plot(parameter_values, all_scores, 'bx')
    plt.show()
    '''

"""
function : 通过主函数测试该模块功能
parameter : 无
return : 无
"""
'''
def main():
    path = input('请输入数据集路径：')
    # D:\zzz\data_analysis\代码\knn\Data\Ionosphere\ionosphere.data
    X,y = downloadData(path)
    avg_scores,all_scores,parameter_values = knnCategoricalData(X,y)
    dataView(avg_scores,all_scores,parameter_values)
'''

"""
function : 调用mian函数
parameter : 无
return : 无
"""
#main()






