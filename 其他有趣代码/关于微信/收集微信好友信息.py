#coding:utf-8

import re
import itchat
import numpy as np
from os import path
import PIL.Image as Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


itchat.login()  #爬取自己好友相关信息,返回一个json文件
friends = itchat.get_friends(update=True)[0:]


#------------统计各性别人数------------#
male = female = other = 0  #初始化
#下标0是自己
for i in friends[1:]:
     sex = i['Sex']
     if sex == 1:
          male += 1
     elif sex == 2:
          female += 1
     else:
          other += 1
total = len(friends[1:])  #计算朋友总数


#------------打印个性别人数------------#
print('男性好友:%.2f%%'%(float(male)/total*100))
print('女性好友:%.2f%%'%(float(female)/total*100))
print('未知性别好友:%.2f%%'%(float(other)/total*100))


#---------------绘制饼图---------------#
'''
labels = 'Male','Female','Other'
sizes = [(float(male)/total*100),(float(female)/total*100),(float(other)/total*100)]
explode = (0,0.1,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#shadow表示是否带阴影，startangle表示起始角度
#plt.axis('equal')   #绘图变成正圆形
plt.show()
'''

#------------爬取其他信息------------#
def get_var(var):
     variable = []
     for i in friends:
          value = i[var]
          variable.append(value)
     return variable

NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
RemarkName = get_var('RemarkName')


data = {'真实姓名':RemarkName,'昵称':NickName,'性别':Sex,'省':Province,
        '城市':City,'个性签名':Signature}
frame = DataFrame(data)
frame.to_csv('data1.csv',index=True)


#------------重新处理个性签名------------#
siglist = []
for i in friends:
     signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
     rep = re.compile('1f\d+\w*|[<>/=]')
     signature = rep.sub('',signature)
     siglist.append(signature)
text = ''.join(siglist)

import jieba
wordlist = jieba.cut(text,cut_all=True)
word_space_split = ''.join(wordlist)

count = 0
with open('alice.txt', 'w') as f:
     for i in range(len(word_space_split)):
          if i%10 == 0:
               f.write(word_space_split[count:i]+'\n')
               count = i


#------------绘制词云图------------#
def drowWordCloud():
    d = path.dirname(__file__)
    # Read the whole text.
    text = open(path.join(d, 'alice.txt')).read()
    
    alice_coloring = np.array(Image.open(path.join(d, "alice_color1.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                   stopwords=stopwords, max_font_size=75, random_state=42,
                   font_path="simhei.ttf")
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    #plt.figure()
    plt.show()

drowWordCloud()



"""
import itchat
import math
import PIL.Image as Image
import os
# hotReload=True  # 使用这个属性，生成一个静态文件itchat.pkl，用于存储登陆的状态。
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
path = 'D:/zzz/image/'
for item in friends:
    # 可以打印item来看其中具体是什么内容，有什么字段
    img = itchat.get_head_img(userName=item['UserName'])
    with open(path + item['NickName'] + '.jpg', 'wb') as f:
        f.write(img)
# 获取好友昵称和签名
info = [(item['NickName'], item['Signature']) for item in friends]
# 获取文件夹中所有的图片
ls = os.listdir(path)
img_num = len(ls)
# 每张小图片宽
size = 60
#每行放几张
lines = 10
# 大图宽
width = 600
# 大图长
height = math.ceil(img_num/10)*60
# 画一个大图，用来放小头像
image = Image.new('RGBA', (width, height))
x = 0
y = 0
for i in range(0, len(ls)):
    img = Image.open(path + info[i][0] + '.jpg')
    img = img.resize((size, size), Image.ANTIALIAS)
    # 向指定位置放缩小后的图片
    image.paste(img, (x * size, y * size))
    x += 1
    if x == lines:
        x = 0
        y += 1
image.save(path + 'friends.jpg')
# 通过文件助手发给自己
itchat.send_image(path + 'friends.jpg', 'filehelper')
"""
