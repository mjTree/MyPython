#coding:utf-8

import warnings
warnings.simplefilter("ignore")
import json
import jieba
import random
import itchat
from gensim import corpora, models, similarities


'''
function: 读取数据集文件
return: 返回问题列表和解答列表
'''
def loadFile(filepath):
    quesList = []
    answList = []
    
    with open(filepath,'rt',encoding='utf-8')as file_to_read:
        line = file_to_read.readline()
        while line:
            tmp = []
            line = json.loads(line)
            quesList.append(line['title'])
            for m in line['replies']:
                tmp.append(m['content'])
            answList.append(tmp)
            line = file_to_read.readline()
    return quesList,answList


'''
function: 将文本集转成字典和语料库
return: 返回字典和语料库
'''
def pretreat(texts):
    texts = [jieba.lcut(text) for text in texts]    # 做分词列表
    dictionary = corpora.Dictionary(texts)    # 建立文本集字典
    # 基于词典,将分词列表集转换成稀疏向量集(语料库)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return dictionary, corpus


'''
function: 通过预料库来训练TF-IDF模型
return: 返回模型
'''
def trainingModel(corpus):
    tfidf = models.TfidfModel(corpus)
    return tfidf


'''
function: 文本相似度计算
return: 最符合问题的位置下标
'''
def simCalc(tf_texts,tf_kw,num_features):
    index = similarities.SparseMatrixSimilarity(tf_texts, num_features)
    sim = index[tf_kw]
    #for e, s in enumerate(sim, 1):
    #   print('kw 与 text%d 相似度为：%.2f' % (e, s))
    result = list(sim)
    #print(a,max(a),a.index(max(a)))
    return result.index(max(result)) 



# 开始训练模型
texts,answer = loadFile('sample.txt')
dictionary, corpus = pretreat(texts)
tfidf = trainingModel(corpus)


'''
function: 开始夸用户
'''
def callUser(msg):
    kw_vector = dictionary.doc2bow(jieba.lcut(msg['Text']))  # 搜索词转稀疏向量
    # 用训练好的TF-IDF模型处理被检索文本和搜索词
    tf_texts = tfidf[corpus]
    tf_kw = tfidf[kw_vector]
    num_features = len(dictionary.token2id)
    loca = simCalc(tf_texts,tf_kw,num_features)
    num = min(random.randint(2,4),len(answer[loca]))
    for i in range(num):
        try:
            itchat.send(answer[loca][i],toUserName=msg['FromUserName'])
        except:
            itchat.send((msg['RemarkName']or msg['NickName'])+'给我发的：'+msg['Text']+' 报错啦')


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply = callUser(msg)

itchat.auto_login(hotReload=True)
itchat.run()




