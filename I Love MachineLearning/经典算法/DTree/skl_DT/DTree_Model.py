#coding:utf-8
#DTree_Model.py

from sklearn.feature_extraction import DictVectorizer
import csv, os
from sklearn import tree
from sklearn import preprocessing, metrics
from sklearn.externals.six import StringIO


"""
function: 读取csv文件,并将特性放入命令列表和类标签列表中
parameter: filename 数据集路径文件名
return: featureList 数据的特征值,labelList 类别标签
error: P2的sklearn和P3存在差异
solve: http://blog.csdn.net/qing101hua/article/details/77002444
"""
def loadDataset(filename):
    #allData = open(filename, 'rb')  #报错
    try:
        allData = open(filename, 'rt')
        reader = csv.reader(allData)
        headers = next(reader)
        #print(headers)     #展示首行信息
        featureList = []    #装特征值数据
        labelList = []      #装类别标签
        for row in reader:
            labelList.append(row[len(row)-1])   #读取每行最后一列的标签值
            rowDict = {}                        #读取该行的特征值
            for i in range(1, len(row)-1):
                rowDict[headers[i]] = row[i]
            featureList.append(rowDict)
        return featureList,labelList
    except:
        return 'error','error'



"""
function: 将特征值和类别标签转化成sklearn所需的0,1表示
parameter: featureList 数据的特征值
parameter: labelList 类别标签
return: dummyX 特征值转化结果
return: dummyY 类别标签转化结果
return: vec
"""
def valueConversion(featureList,labelList):
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    #print("dummyX: " + str(dummyX))    #展示转化成功的0,1
    #print(vec.get_feature_names())
    
    #print("labelList: " + str(labelList))
    lb = preprocessing.LabelBinarizer()
    dummyY = lb.fit_transform(labelList)
    #print("dummyY: " + str(dummyY))
    return dummyX,dummyY,vec



"""
function: 使用sklearn库的决策树对数据分类
parameter: dummyX 特征值
parameter: dummyY 类别标签
parameter: vec
return: clf 分类好的决策树
"""
def treesClassification(dummyX,dummyY):
    # 使用决策树进行分类
    # clf = tree.DecisionTreeClassifier()
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = clf.fit(dummyX, dummyY)
    #print("clf: " + str(clf))
    return clf



"""
function: 给分类好的数据创建一个pdf展示
parameter: vec
parameter: clf 决策树
"""
def createView(vec,clf):
    # 生成可视化模型<就是创建一个ResultsView.dot文件>
    with open("ResultsView.dot", 'w') as f:
        f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)
    # dot -Tpdf ResultsView.dot -o output.pdf
    try:
        print("如果主机无Graphviz则不能转化成pdf")
        cmd = "dot -Tpdf ResultsView.dot -o ResultsView.pdf"
        os.system(cmd)
    except:
        print("主机无Graphviz软件不能转化")



"""
function: 读取预测数据集的特征值
parameter: filename 数据集路径文件名
parameter: clf 决策树
return: predictedY 预测集预测的结果
error: 矩阵二维强转一维报错
solve: http://m.blog.csdn.net/justin18chan/article/details/78715495
"""
def forecastTest(filenameF,clf):
    '---读取预测集特征值---'
    forecastListData = open(filenameF, 'rt')
    reader = csv.reader(forecastListData)
    headers = next(reader)
    #print(headers)     #展示首行信息
    forecastList = []    #装特征值数据
    for row in reader:
        rowDict = {}    #读取该行的特征值
        for i in range(1, len(row)):
            rowDict[headers[i]] = row[i]
        forecastList.append(rowDict)
    
    '---转化预测集特征值---'
    vec = DictVectorizer()
    dummyXF = vec.fit_transform(forecastList).toarray()
    
    '---预测数据集---'
    predictedY = []     #存储预测集的预测结果
    for i in range(int(row[0])):
        #newRowX = dummyXF[int(i), :]
        #pred = clf.predict(newRowX)  #报错原因是二维强转一维
        pred = clf.predict(dummyXF[int(i), :].reshape(1,-1))
        predictedY.append(pred)
    return predictedY

