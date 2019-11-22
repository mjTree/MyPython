import SVM_Model as svm
import pylab as pl
import numpy as np

filename = input("请输入数据集路径：\n")    # irisdata.txt
split = input("请输入数据集分割率：")
function = input('<1:多项式核函数 2:线性核函数 3：径向基核函数>\n选择核函数对应数字：')

filename,split,function = svm.checkParam(filename,split,function)

trainingSet,testSet,trainingLabel,testLabel = svm.loadDataset(filename,split)

print('训练集有: ' + repr(len(trainingSet)) + '个')
print('测试集有: ' + repr(len(testSet)) + '个')

# 转化类标签表示方式
trainingLabel = svm.valueConversion(trainingLabel)
testLabel = svm.valueConversion(testLabel)

clf = svm.svmClassification(trainingSet,trainingLabel,function)    #通过训练集得到svm分类器

accuracy = svm.getAccuracy(testSet,testLabel,clf)   #用测试集对分类器做测试
print('预测精度: ' + repr(accuracy) + '%')

