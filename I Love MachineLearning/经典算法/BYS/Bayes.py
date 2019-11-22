# encoding: utf-8

"""
@version: python3.6
@author: misakalee
@contact: misakaleeaslxy@gmail.com
@file: Bayes.py
@time: 2018.01.24 19:06
"""
"""
bayes为主函数,
输入：
dataset：列表形式的数据集，最后一列为类别信息。
splitRatio：0~1之间两位小数，默认为0.67，当splitRatio=1时全为训练集。splitRatio=0时报错，输入0~1之间的数。
返回：
summarizes：训练结果，字典。
prediction：预测结果，二维列表，最后一列为预测的分类结果，前面为属性。
accuracy：有测试集时的准确度。

summarizeByClass为训练函数，
输入：
dataset：列表形式的数据集，最后一列为类别信息。
返回：
summarizes：训练结果，字典。

calculateClassProbabilities，predict均为预测函数，
输入：（两函数相同）
summaries：为summarizeByClass所返回的训练结果
inputVector：列表，为想要分类的数据，不包含类别信息
返回：
calculateClassProbabilities返回probabilities：返回该输入属于各个类别的概率
predict返回bestLabel：为该输入最可能属于的类别，即可能性最大的类别

getPredictions为多重预测函数，
输入：
summaries：为summarizeByClass所返回的训练结果
testSet：二维列表，为想知道类别的数据，也可以在最后一列包含类别信息作为测试
返回：
predictions：为各数据所归属类别的列表，顺序与输入列表一致

splitDataset为数据集分割函数，
输入：
dataset：列表形式数据集
solitRation：0~1之间两位小数，当splitRatio=1时全为训练集。splitRatio=0时报错，输入0~1之间的数。
返回：
trainSet：训练集
copy：测试集
"""
import random
import math
    #分割数据集
def splitDataset(dataset,splitRatio):
    if splitRatio<=0 or splitRatio>1:
        return print('Please give a number 0~1(such as 0.67) to split the data')
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))#随机选择项加入train并从copy删除
    return [trainSet,copy]   #trainSet为训练集，copy为测试集

    #以类别分割数据集
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):#最后一项为类别
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries

def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities

def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def bayes(dataset, splitRatio=0.67):
    if splitRatio<=0 or splitRatio>1:
        print('Please give a number 0~1(such as 0.67) to split the data')
        return None,None,None
    trainSet,testSet = splitDataset(dataset,splitRatio) #分割数据集
    summarizes = summarizeByClass(trainSet)#训练
    predictions = getPredictions(summarizes,testSet)#预测
    accuracy = getAccuracy(testSet,predictions)#计算准确度
    prediction = testSet
    for i in range(len(testSet)):
        prediction[i][-1] = predictions[i]
    return summarizes,prediction,accuracy

