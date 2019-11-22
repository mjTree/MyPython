'''
#采集网络上一张图片
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")
'''

'''
#自己做一个csv表格
import csv
csvFile = open("D:/Python36/WorkSpace/test.csv",'w+')
try:
     writer = csv.writer(csvFile)
     writer.writerow(('number','number plus 2','number times 2'))
     for i in range(10):
          writer.writerow((i,i+2,i*2))
finally:
     csvFile.close()
'''


'''
#从网上获取数据写入csv中
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("D:/Python36/WorkSpace/editors.csv",'wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
try:
     for row in rows:
          csvRow = []
          for cell in row.findAll(['td','th']):
               csvRow.append(cell.get_text())
          writer.writerow(csvRow)
finally:
     csvFile.close()
'''


'''
#一个简单的连接数据库查询
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='123456',
                       db='imooc',port=3306,charset='utf8')
cur = conn.cursor()
print('数据库连接成功')
cur.execute('select * from pages where id=1')

print(cur.fetchone())
cur.close()
conn.commit()
conn.close()
'''



#爬虫随机爬取的数据存入数据库中
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='123456',
                       db='imooc',port=3306,charset='utf8')
cur = conn.cursor()
print('数据库连接成功')

random.seed(datetime.datetime.now())

def store(title,content):
     cur.execute('insert into studentinfo(title,content)values(\"%s\",\"%s\")',(title,content))
     #cur.execute('insert into studentinfo(Id,Deperment,Major,Grade,Class,Num,Name,Sex)values(\"%s\",\"%s\,\"%s\,\"%s\,\"%s\,\"%s\,\"%s\,\"%s\")',(Id,Deperment,Major,Grade,Class,Num,Name,Sex))
     cur.connection.commit()

def getLinks(articleUrl):
     html = urlopen("http://en.wikipedia.org"+articleUrl)
     bsObj = BeautifulSoup(html)
     title = bsObj.find('h1').get_text()
     content = bsObj.find('div',{"id":"mw-content-text"}).find('p').get_text()
     store(title,content)
     return bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

def main():
     links = getLinks('/wiki/Kevin_Bacon')
     try:
          while len(links)>0:
               newArticle = links[random.randint(0,len(links)-1)].attrs['href']
               print(newArticle)
               links = getLinks(newArticle)
     finally:
          cur.close
          conn.commit()
          conn.close()
main()



'''
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject,body):
     msg = MIMEText(body)
     msg['Subject'] = subject
     msg['From'] = 'christmas_alerts@pythonscraping.com'
     msg['To'] = "ryan@pythonscraping.com"

     s = smtplib.SMTP('localhost')
     s.send_message(msg)
     s.quit()

bsObj = BeautifulSoup(urlopen('http://isitchristmas.com/'))
while(bsObj.find('a',{'id':'answer'}).attrs['title']=='NO'):
     print('今天不是圣诞节')
     time.sleep(3600*24)
     bsObj = BeautifulSoup(urlopen('http://isitchristmas.com/'))
sendMail("今天是圣诞节","According to http://isitchristmas.com,it is Christmas!")
'''





