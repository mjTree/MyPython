#coding:utf-8

import re
import datetime
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "没爬到"


def getLink(html):
    linkList1 = []
    try:
        linkList = re.findall(r'\/\/zhaoshang.tmall.com.*?\"', html)
        #print(len(linkList))
        for i in range(len(linkList)):
            link = 'http:' + str(linkList[i])[0:-1]
            linkList1.append(link)
        return linkList1
    except:
        return linkList1


def getGoods(html):
    sthList1 = []
    try:
        sthList = re.findall(r'\/\/detail.tmall.com\/item.htm.*?\"', html)
        print(len(sthList))
        for i in range(len(sthList)):
            sth = 'http:' + str(sthList[i])[0:-1]
            sthList1.append(sth)
        return sthList1
    except:
        print('爬取失败')
        return sthList1


def main():
    classfy = ['洗澡','手办','遥控']
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #现在
    for goods in classfy:
        name = str(goods) + '.txt'
        url = '''
                https://list.tmall.com/search_product.htm?q=''' + goods + '''&type=
                p&vmarket=&spm=0.0.a2227oh.d100&from=..pc_1_searchbutton
              '''
        html = getHTMLText(url)
        goodsLink = getGoods(html)  #获得某件商品的部分链接
        for License in goodsLink:
            html1 = getHTMLText(License)
            listLink = getLink(str(html1))
            with open(name,'a',errors='ignore') as f:
                for m in listLink:
                    f.write('\n' + str(m))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) #现在


main()



