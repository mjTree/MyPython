import csv
import sys
import numpy as np


#读取数据集
data_filename = "Data\\Ionosphere\\ionosphere.data"
#print(data_filename)

# Size taken from the dataset and is known
X = np.zeros((351, 34), dtype='float')
y = np.zeros((351,), dtype='bool')

with open(data_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
        data = [float(datum) for datum in row[:-1]]
        X[i] = data
        y[i] = row[-1] == 'g'


#创建训练集和测试集
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)
print("There are {} samples in the training dataset".format(X_train.shape[0]))
print("训练数据集中有{}样本".format(X_train.shape[0]))
print("测试数据集中有{}样本".format(X_test.shape[0]))
print("每个示例都有{}特性".format(X_train.shape[1]))

from sklearn.neighbors import KNeighborsClassifier    #导入K近邻分类器类
estimator = KNeighborsClassifier()    #参数默认

estimator.fit(X_train, y_train)    #用训练数据进行训练

# 用测试集测试算法
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("精度是{0:.1f}%".format(accuracy))


# scikit-learn交叉检验
from sklearn.cross_validation import cross_val_score

scores = cross_val_score(estimator, X, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("平均精度是{0:.1f}%".format(average_accuracy))

avg_scores = []
all_scores = []
parameter_values = list(range(1, 21))  # Including20
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator, X, y, scoring='accuracy')
    #保存n_neighbors值的得分和平均分
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)


#绘制图形
from matplotlib import pyplot as plt
plt.figure(figsize=(32,20))
plt.plot(parameter_values, avg_scores, '-o', linewidth=5, markersize=24)
plt.show()
#plt.axis([0, max(parameter_values), 0, 1.0])

for parameter, scores in zip(parameter_values, all_scores):
    n_scores = len(scores)
    plt.plot([parameter] * n_scores, scores, '-o')
plt.show()

plt.plot(parameter_values, all_scores, 'bx')
plt.show()


from collections import defaultdict

all_scores = defaultdict(list)
parameter_values = list(range(1, 21))  # Including 20
for n_neighbors in parameter_values:
    for i in range(100):
        estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
        scores = cross_val_score(estimator, X, y, scoring='accuracy', cv=10)
        all_scores[n_neighbors].append(scores)
for parameter in parameter_values:
    scores = all_scores[parameter]
    n_scores = len(scores)
    plt.plot([parameter] * n_scores, scores, '-o')
plt.show()

plt.plot(parameter_values, avg_scores, '-o')
plt.show()


#进行特征规范化
from sklearn.preprocessing import MinMaxScaler

X_transformed = MinMaxScaler().fit_transform(X)
estimator = KNeighborsClassifier()
transformed_scores = cross_val_score(estimator, X_transformed, y, scoring='accuracy')
print("平均精度为{0:.1f}%".format(np.mean(transformed_scores) * 100))
