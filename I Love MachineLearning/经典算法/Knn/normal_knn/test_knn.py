import threading
import KNN_Model as knn


filename = input("请输入数据集路径:\n")     # irisdata.txt
split1 = input("请输入数据集分割率:")
k1 = input("请输入最近邻K值:")

filename,split,k = knn.checkParam(filename, split1, k1)   #检测参数

trainingSet,testSet = knn.loadDataset(filename, split)  #加载数据集

print('训练集有: ' + repr(len(trainingSet)) + '个')
print('测试集有: ' + repr(len(testSet)) + '个')

predictions = knn.operatorTestSet(trainingSet,testSet,k)    #KNN分类训练集类别

accuracy = knn.getAccuracy(testSet, predictions)    #计算分类器的精度

print('预测精度: ' + repr(accuracy) + '%')


#scores = knn.dataView(trainingSet,testSet)
class ThreadDrow(threading.Thread):
    def run(self):
        scores = knn.dataView(trainingSet,testSet)
        #from matplotlib import pyplot as plt
        #plt.plot(scores)
        #plt.show()

t = ThreadDrow()
t.start()


'----------分类预测集----------'
filename1 = input("请输入预测集：\n")      # forecast.txt
forecastSet = knn.loadForecast(filename1)

PredictionSet = knn.forecastTest(trainingSet,forecastSet,k)
print(PredictionSet)

