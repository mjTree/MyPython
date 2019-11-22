#coding:utf-8
#KNN_Model.py

import sys
import csv
import random
import math
import operator


"""
function: 对输入参数进行判断
parameter: fiename 文件路径
parameter: split 分割数据集比例
parameter: k 最近邻的K值
return: 输入的参数值
"""
def checkParam(filename, split, k):
    if filename == '':
        print('数据集不存在,请重新读取！！')
        #filename = 'KNN_0'
        sys.exit()
    if str(int(float(split))).isdigit() and (float(split)>0 and float(split)<1):
        split = float(split)
    else:
        print('输入有误,默认修改为0.7')
        split = '0.7'  #默认分割0.7
        split = float(split)
    if str(k).isdigit():
        k = int(k)
    else:
        k = '4'     #默认为4
        k = int(k)
    return filename,split,k



"""
function: 将数据库表的数据集分割
parameter: dataset 数据集
parameter: split 分割率
return: trainingSet 训练集 testSet 测试集
"""
def loadDatabase(dataset,split):
    trainingSet = []    #训练集
    testSet = []        #测试集
    for x in range(len(dataset)-1):
        for y in range(len(dataset[x])-1):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])
    return trainingSet,testSet


"""
function: 加载数据集文件
parameter: filename 数据集路径文件名
parameter: split 分割数据集来创建训练集和测试集
return: trainingSet 训练集
return: testSet 测试集
"""
def loadDataset(filename, split):
    trainingSet = []    #训练集
    testSet = []        #测试集
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        columns = next(lines)   #确定数据集列数
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(len(columns)-1):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
    return trainingSet,testSet


"""
function: 计算距离
parameter: instance1 事例1
parameter: instance2 事例2
parameter: length 事例的维度
return: euclideanDistance 返回euclidean的距离
"""
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)



"""
function: 获取测试集预测类别
parameter: trainingSet 训练集
parameter: testSet 测试集
parameter: k K值
return: predictions 测试集真实类别
"""
def operatorTestSet(trainingSet,testSet,k):
    predictions = []
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        #print('>预测-->' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    return predictions


"""
function: 获取最近的K个相邻数
parameter: trainingSet 训练集
parameter: testInstance 测试集中一个事例
parameter: k K值
return: neighbors K个最近的邻居
"""
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        #testinstance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        #distances.append(dist)
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


"""
function: 统计最近的K个邻居属于那些类别
parameter: neighbors K个最近的邻居
return: sortedVotes[0][0] 最相似的类别
"""
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


"""
function: 对分类结果进行检测
parameter: testSet 测试集
parameter: predictions 测试集真实类别
return: 最相似的类别
"""
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


"""
function: 绘制图形
parameter: trainingSet 训练集
parameter: testSet 测试集
return: scores 不同K值下的精度
"""
def dataView(trainingSet,testSet):
    scores = []
    parameter_values = list(range(1, 21))  # 计算K值从1-20之间的差异
    for n_neighbors in parameter_values:
        predictions = operatorTestSet(trainingSet,testSet,n_neighbors)
        accuracy = getAccuracy(testSet, predictions)
        scores.append(repr(accuracy))
    from matplotlib import pyplot as plt
    plt.plot(scores)
    plt.savefig('1.jpg')
    #plt.show()
    return scores


"""
function: 读取预测集文件
parameter: filename 文件路径
return: forecast 预测集
"""
def loadForecast(filename):
    forecastSet = []
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        columns = next(lines)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(len(columns)):
                dataset[x][y] = float(dataset[x][y])
            forecastSet.append(dataset[x])
    return forecastSet


"""
function: 预测数据集
parameter: trainingSet 训练集
parameter: forecastSet 预测集
parameter: k K值
return: PredictionSet 预测集分类的类别
"""
def forecastTest(trainingSet, forecastSet, k):
    PredictionSet = []
    for x in range(len(forecastSet)):
        sortedVotes = KNN_cls(trainingSet,forecastSet[x],k)
        PredictionSet.append(sortedVotes)
    return PredictionSet


"""
function: 用KNN分类器预测某行数据类别
parameter: trainingSet 训练集
parameter: testSet 测试集
return: scores 不同K值下的精度
"""
def KNN_cls(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    sortedVotes = getResponse(neighbors)
    return sortedVotes



"""
import numpy as np
from sklearn import neighbors   
      
knn = neighbors.KNeighborsClassifier() #取得knn分类器    
data = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]]) #data对应着打斗次数和接吻次数  
labels = np.array([1,1,1,2,2,2]) #labels则是对应Romance和Action  
knn.fit(data,labels) #导入数据进行训练   
print(knn.predict([18,90]))  
"""
