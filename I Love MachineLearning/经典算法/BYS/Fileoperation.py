# encoding: utf-8

"""
@version: python3.6
@author: misakalee
@contact: misakaleeaslxy@gmail.com
@file: Fileoperation.py
@time: 2018.01.21 20:38
"""
"""
如果文件在当前目录，则输入文件名
如果文件不在当前目录，则输入绝对路径
以列表形式返回数据集
"""

import csv #import file

def loadCsv(filename):
    with open(filename,'r') as f:
        dataset = list(csv.reader(f))
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]# 将数据转化为float方便计算
        return dataset
