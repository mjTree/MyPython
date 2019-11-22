#coding:utf-8
#trees.py

"""
@CreateTime: 2017/12/11
@UpdateTime: 2017/12/11
@author: mjTree
"""

from math import log
import operator


"""
function : 创建一个数据集
return :  数据集、标签集
"""
def createDataSet():
    dataSet = [ [1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels


"""
function : 计算给定数据集的香农熵
parameter : dataSet 数据集
return : 
"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:     # 为所有可能分类创建字典
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob,2)    # 以2为底求对数
    return shannonEnt


"""
function : 按照给定特征来划分数据集
parameter : dataSet 待划分的数据集
parameter : axis 划分数据集的特征
parameter : value 需要返回特征的值
return : retDataSet 第axis轴为value值的数据集
"""
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:    # 将符合特征的数据抽取出来
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            #del(reducedFeatVec[axis])
            retDataSet.append(reducedFeatVec)
    return retDataSet


"""
function : 选择好的数据集划分方式
parameter : dataSet 待划分的数据集
return : bestFeature 最佳的轴
"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy    #计算信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


"""
function : 计算类型列表中,类型最多的类别
parameter : classList 剩余类别的类型数据
return : sortedClassCount[0][0] 最佳的轴
"""
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


"""
function : 通过递归用训练集来创建决策树
parameter : dataSet 训练集
parameter : labels 类别集
return : myTree 字典类型的树
"""
def createTree(dataSet,labels):    # 创建树的函数代码
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(calssList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


"""
function : 使用决策树的分类函数
parameter : inputTree 字典类型的树
parameter : featLabels
parameter : testVec 
return : classLabel 
"""
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel


'''
def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel
'''


"""
function : 使用pickle模块存储决策树
parameter : inputTree 字典类型的数
parameter : filename 要保存的文件名称
"""
def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

