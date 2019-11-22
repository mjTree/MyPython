#coding:utf-8

from pypinyin import pinyin


def findName(nameTest):
    length = len(nameTest);letter = ''
    name = pinyin(nameTest)
    for i in range(length):
        letter += name[i][0][0]
    if 'xzh' == letter:
        print('符合:', nameTest)

with open('name.txt', 'r') as f:
     for line in f:
         findName(line.strip('\n'))
