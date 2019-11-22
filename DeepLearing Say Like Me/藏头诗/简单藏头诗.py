#coding:utf-8

import pandas as pd
import numpy as np



poems = open(r'poems.txt',encoding='UTF-8').read()

lines = poems.split("\n")
sens_all = pd.DataFrame({"sen": lines})
sens_all["length"] = sens_all.sen.str.len()
l = np.asarray(sens_all.sen.str.split("。|，"))



'''
function: 将二维数据转换为一维数据
'''
def flat(li, re=[]):
    for i in range(0, len(li)):
        re.append(li[i][0])
        if len(li[i])>1:
            re.append(li[i][1])
    return re


df_all = pd.DataFrame({"sen":flat(l)})

df_all["tou"] = df_all.sen.str[0]   # 取头
df_all["wei"] = df_all.sen.str[-1]  # 取尾
#print df_all.head()


#区分五言与七言
df_5w = df_all.loc[df_all.sen.str.len()==5,]
df_7w = df_all.loc[df_all.sen.str.len()==7,]


#五言藏头
def Poet_Libai_5_tou():
    global l
    l = []
    user_line = input("请输入四个藏头字:\n")
    for i in range(len(user_line)):
        tf = df_5w.tou.str.contains(user_line[i])
        if tf.value_counts()[0]<len(tf):
            l.append(np.asarray(df_5w.loc[tf,"sen"])[0])
        else:
            l.append("----诗库暂无----")
    print("\n".join(l))


#五言藏尾
def Poet_Libai_5_wei():
    global l
    l = []
    user_line = input("请输入四个藏尾字:\n")
    for i in range(len(user_line)):
        tf = df_5w.wei.str.contains(user_line[i])
        if tf.value_counts()[0]<len(tf):
            l.append(np.asarray(df_5w.loc[tf,"sen"])[0])
        else:
            l.append("----诗库暂无----")
    print("\n".join(l))


#七言藏头
def Poet_Libai_7_tou():
    global l
    l = []
    user_line = input("请输入四个藏头字\n")
    for i in range(len(user_line)):
        tf = df_7w.tou.str.contains(user_line[i])
        if tf.value_counts()[0]<len(tf):
            l.append(np.asarray(df_7w.loc[tf,"sen"])[0])
        else:
            l.append("----诗库暂无----")
    print("\n".join(l))


#七言藏尾
def Poet_Libai_7_wei():
    global l
    l = []
    user_line = input("请输入四个藏尾字:\n")
    for i in range(len(user_line)):
        tf = df_7w.wei.str.contains(user_line[i])
        if tf.value_counts()[0]<len(tf):
            l.append(np.asarray(df_7w.loc[tf,"sen"])[0])
        else:
            l.append("----诗库暂无----")
    print("\n".join(l))


while True:
    Poet_Libai_5_tou();print('')
    Poet_Libai_5_wei();print('')
    Poet_Libai_7_tou();print('')
    Poet_Libai_7_wei();print('')
    
    flag = input('是否结束：<y/n>\n')
    if flag == 'n':
        continue
    else:
        break
        
    
