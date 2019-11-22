#coding:utf-8

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "没爬到"


def parsePage(html):
    infoList = []
    try:
        titleList = re.findall(r'target=\"_blank\">.*?<', html)
        positionList1 = re.findall(r'\"district\".*?>', html)
        positionList2 = re.findall(r'\"bizcircle\".*?>', html)
        yearList = re.findall(r'/&nbsp.*?\n', html)
        tagList = re.findall(r'\"tagList\">\n                .*?/',html)
        priceList = re.findall(r'\"totalPrice\">.*?/', html)
        print(len(tagList))
        #print(priceList)
        for i in range(len(titleList)):
            # 楼盘名称
            title = titleList[i].split('>')[1][0:-1]
            # 楼盘价格
            price = priceList[i].split('n')[1][1:-2]
            # 楼盘位置
            positionInfo1 = positionList1[i].split('=')[1][1:-4]
            positionInfo2 = positionList2[i].split('=')[1][1:-4]
            position = positionInfo1 + '/' + positionInfo2
            # 建成时间
            year = yearList[i].split(';')[1][0:-1]
            # 附近地铁
            if len(tagList[i]) < 30:
                tag = '无地铁'
            else:
                tag = tagList[i].split('n')[1][1:-2]
            # 添加5个元素
            infoList.append([title, price, position, year, tag])
        return infoList
    except:
        print('爬取失败')
        return infoList


def main():
    for i in range(2):
        url = 'https://wh.lianjia.com/xiaoqu/jiangxia/pg'+ str(i+1) +'/'
        html = getHTMLText(url)
        #print(html[:100])
        
        infoList = parsePage(html[25000:84000])
        with open('house1.txt', 'a',errors='ignore') as f:
            for i in range(30):
                try:
                    f.write(str(infoList[i][0])+','+str(infoList[i][1])+','+str(infoList[i][2])+','+str(infoList[i][3])+','+str(infoList[i][4])+'\n')
                except:
                    print('爬取就是写错一个')
                    continue
    print('\n\n爬完了.....')


main()






