'''
#数据概括
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
     input = re.sub('\n+',' ',input).lower()
     input = re.sub('\[[0-9]*\]','',input)
     input = re.sub(' +',' ',input)
     input = bytes(input,'UTF-8')
     input = input.decode('ascii','ignore')
     cleanInput = []
     input = input.split(' ')
     for item in input:
          item = item.strip(string.punctuation)
          if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
               cleanInput.append(item)
     return cleanInput

def ngrams(input,n):
     input = cleanInput(input)
     output = {}
     for i in range(len(input)-n+1):
          ngramTemp = " ".join(input[i:i+n])
          if ngramTemp not in output:
               output[ngramTemp] = 0
          output[ngramTemp] += 1
     return output

content = str(urlopen(
     'http://pythonscraping.com/files/inaugurationSpeech.txt').read(),'utf-8')
ngrams = ngrams(content,2)
sortedNGrams = sorted(ngrams.items(),key = operator.itemgetter(1),reverse=True)
print(sortedNGrams[:20])
'''


'''
#文章生成器
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
     sum = 0
     for word,value in wordList.items():
          sum += value
     return sum

def retrieveRandomWord(wordList):
     randIndex = randint(1,wordListSum(wordList))
     for word,value in wordList.items():
          randIndex -= value
          if randIndex <= 0:
               return word

def buildWordDict(text):
     text = text.replace('\n',' ')
     text = text.replace('\"','')

     punctuation = [',', '.', ';',':']
     for symbol in punctuation:
          text = text.replace(symbol," "+symbol+" ")
          
     words = text.split(" ")
     words = [word for word in words if word !=""]

     wordDict = {}
     for i in range(1,len(words)):
          if words[i-1] not in wordDict:
               wordDict[words[i-1]] = {}
          if words[i] not in wordDict[words[i-1]]:
               wordDict[words[i-1]][words[i]] = 0
          wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]]+1
     return wordDict

text = str(urlopen(
     'http://pythonscraping.com/files/inaugurationSpeech.txt').read(),'utf-8')
wordDict = buildWordDict(text)

length = input('输入需要生成多少个数目单词文章:')
chain =""
currentWord = "I"
for i in range(0,int(length)):
     chain += currentWord + " "
     currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)
'''


'''
#统计
from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize('这里有些小黄书')
text = Text(tokens)
'''


'''
#打印NLTK内置书名
from nltk.book import *
from nltk import ngrams
fourgrams = ngrams(text6,4)
for fourgram in fourgrams:
     if fourgram[0] == 'coconut':
          print(fourgram)
'''

















