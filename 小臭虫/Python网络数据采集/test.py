'''
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
     try:
          html = urlopen(url)
     except (HTTPError,URLError) as e:
          return None
     try:
          bsObj = BeautifulSoup(html.read())
          title = bsObj.body.h1
     except AttributeError as e:
          return None
     return title
title = getTitle('https://zhidao.baidu.com/question/1175659466422508059.html')
if title == None:
     print('找不到')
else:
     print(title)
'''
'''
from urllib.request import urlopen
from bs4  import BeautifulSoup
html = 'http://www.pythonscraping.com/pages/warandpeace.html'
bsObj = BeautifulSoup(html)
#nameList=bsObj.findall("span",{"class":"green"})
nameList = bsObj.findall(text="the prince")
for name in nameList:
     #print(name.get_text())
     print(len(nameList))
'''

'''
#通过随机数爬取连接
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
     html = urlopen("http://en.wikipedia.org"+articleUrl)
     bsObj = BeautifulSoup(html)
     return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links)>0:
     newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
     print(newArticle)
     links = getLinks(newArticle)
'''

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
     html = urlopen(siteUrl)
     bsObj = BeautifulSoup(html)
     internalLinks = getInternalLinks(bsObj,splitAddress(sisteUrl)[0])
     externalLinks = getInternalLinks(bsObj,splitAddress(sisteUrl)[0])
     for link in externalLinks:
          if link not in allExtLinks:
               allExLinks.add(link)
               print(link)
     for link in internalLinks:
          if link not in allIntLinks:
               print('获取链接是:'+link)
               allIntLinks.add(link)
               getAllExternalLinks(link)










