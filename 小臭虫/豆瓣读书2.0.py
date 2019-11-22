# coding:utf-8

import re
import requests
#from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        return r.text
    except:
        return "没爬到"

def getBookLink(html):
    bookID = re.findall(r'<a href=\"https:\/\/book.douban.com\/subject\/.*?\/\" title', html)
    for i in range(len(bookID)):
        bookID[i] = bookID[i].split('"')[1].split('e')[1][3:-1]
        getBookInfo(bookID[i])


def getBookInfo(bookID):
    url = 'https://book.douban.com/subject/'+bookID+'/'
    bookInfo = getHTMLText(url)
    try:
        # 作者名
        partInfo = bookInfo[4000:7000]
        bookWriter = re.findall(r'\"name\": \".*?\"',partInfo)[0].split(':')[1][2:-1]
        # 书名、出版社、出版年、定价、ISBN、评分、图片
        partInfo = bookInfo[10000:16000]
        bookPicture = re.findall(r'<img src=\"https:\/\/img3.doubanio.com\/view\/subject\/l\/public\/.*?\"', partInfo)[0].split('=')[1][1:-1]
        bookName = re.findall(r'<span property=\"v:itemreviewed\">.*?<', partInfo)[0].split('>')[1][:-1]
        bookPress = re.findall(r'<span class=\"pl\">出版社:<\/span>.*?<', partInfo)[0].split('>')[2][1:-1]
        bookYear = re.findall(r'<span class=\"pl\">出版年:<\/span>.*?<', partInfo)[0].split('>')[2][1:-1]
        bookPrice = re.findall(r'<span class=\"pl\">定价:<\/span>.*?<', partInfo)[0].split('>')[2][1:-1]
        bookISBN = re.findall(r'<span class=\"pl\">ISBN:<\/span>.*?<', partInfo)[0].split('>')[2][1:-1]
        bookScore = re.findall(r'<strong class=\"ll rating_num \" property=\"v:average\">.*?<', partInfo)[0].split('>')[1][1:-2]
        # 内容简介
        partInfo = bookInfo[22000:24000]
        bookCon = re.findall(r'<p>.*?<\/p>', partInfo)
        bookConStr = ''
        for i in range(len(bookCon)):
            bookConStr += bookCon[i][3:-4]
        # 作者简介
        partInfo = bookInfo[25000:26000]
        authorInt = re.findall(r'<p>.*?<\/p>', partInfo)
        authorIntStr = ''
        for i in range(len(authorInt)):
            authorIntStr += authorInt[i][3:-4]
    except:
        return
    
    file = open('bookInfo.txt','a',encoding='gb18030')
    file.write(bookWriter+'#'+bookPicture+'#'+bookName+'#'+bookPress+'#'+bookYear+'#'+bookPrice+'#'+bookISBN+'#'+bookScore+'#'+bookConStr+'#'+authorIntStr+'\n')
    


def main():
    goods = input("请输入爬取的书籍类型:")
    page = input('请输入要爬取几张网页信息:')
    for i in range(0, int(page)*20, 20):
        url = 'https://book.douban.com/tag/'+goods+'?start='+ str(i) +'&type=T'
        html = getHTMLText(url)
        getBookLink(html)
    

main()
