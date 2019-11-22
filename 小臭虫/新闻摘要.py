# coding:utf-8

import itchat
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

#http://chromedriver.storage.googleapis.com/index.html

def getLinks(url):
    try:
        driver = webdriver.Chrome(r'C:\D\Python36\Scripts\chromedriver.exe')
        driver.get(url)
        pageSource = driver.page_source
        html_parse = BeautifulSoup(pageSource, 'lxml')
        html = html_parse.findAll("div",{"class":"item no-picture"})
    except:
        print('没网了')
    finally:
        driver.close()
        driver.quit()
        return html


def getNews(html):
    news = str(datetime.datetime.now().date()) + '早报:\n\n'
    for i in range(len(html)):
        news += str(i+1) + '、' +html[i].a.next + '\n' + html[i].a.attrs['href'] + '\n\n'
    return news


url = 'https://news.baidu.com/internet'
html = getLinks(url)
news = getNews(html)
print('信息采集成功')


itchat.login()
friends = itchat.get_friends(update=True)[0:]
users=itchat.search_friends('徐才权')
userName= users[0]['UserName']
itchat.send(news, toUserName=userName)
#groups  = itchat.get_chatrooms(update=True)

