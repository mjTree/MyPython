#!/usr/bin/env Python
# coding=utf-8


# 婴儿车
# //detail.tmall.com/item.htm?id=563202644446&ns=1&abbucket=0
# //item.taobao.com/item.htm?id=545597442857&ns=1&abbucket=0#detail

# 宝宝奶粉
# //detail.tmall.com/item.htm?id=523784609093&ns=1&abbucket=0

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


def getDescribe(url):
    describeList = []
    url = 'https:' + url
    html = getHTMLText(url)
    #dlt = re.findall(r'<li title=\".*?<',html)
    dlt = re.findall(r'<li title=\".*?\"',html)
    for i in range(len(dlt)):
        try:
            #describe = dlt[i].split('>')[1][0:-1]
            describe = dlt[i].split('=')[1][0:-1]
            describeList.append(describe)
        except:
            continue
    return describeList


def parsePage(ilt, html):
    describeList = []
    try:
        Ilt = re.findall(r'\"pic_url\"\:\".*?\"',html)
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        dlt = re.findall(r'\"detail_url\"\:\".*?\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            image = eval(Ilt[i].split(':')[1])
            describe = eval(dlt[i].split(':')[1])
            describeList = getDescribe(describe)
            ilt.append([price , title, image, str(describeList)[1:-1]])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:10}\t{:10}\t{:50}"
    print(tplt.format("序号", "价格", "商品名称","图片链接","详情"))
    count = 0
    for g in ilt:
        count = count + 1
        
        with open('data1.txt','a',errors='ignore') as f:
            price = 'http:' + str(g[2])
            f.write(str(count)+'\t'+str(g[0])+'\t'+str(g[1])+'\t'+price+'\t'+str(g[3])+'\n')
        #print(tplt.format(count, g[0], g[1], price, g[3]))
    print(count)

def main():
    goods = input("请输入爬取的商品名称:")
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(15*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()



'''

a = """'证书编号：2017012201995535', '证书状态：有效', '产品名称：儿童推车/儿童推车',
    '3C规格型号：X7(七款)', '产地:&nbsp;&#20013;&#22269;&#22823;&#38470;', '厂商型号:
    &nbsp;X7(&#19971;&#27454;)', '童车车轮类型:&nbsp;&#22825;&#28982;&#27233;&#33014;'
    , '车架材质:&nbsp;&#38109;&#38209;&#21512;&#37329;', '车篮面料:&nbsp;&#33707;&#201
    95;&#23572;', '颜色分类:&nbsp;&#28145;&#28784;&#33394;(&#23569;&#37327;&#29616;&#3
    6135;&#65292;&#21363;&#23558;&#39044;&#21806;&#65289;&nbsp;&#31881;+&#28784;&#33394
    ;&#65288;&#23569;&#37327;&#29616;&#36135;&#65292;&#21363;&#23558;&#39044;&#21806;&#
    65289;&nbsp;&#22696;&#32511;&#33394;&#65288;&#29616;&#36135;&#65289;&nbsp;&#37202;&#
    32418;&#33394;&#65288;&#23569;&#37327;&#29616;&#36135;&#65289;&nbsp;&#31881;&#32418
    ;&#33394;&#65288;&#23569;&#37327;&#29616;&#36135;&#65289;', '推车价格:&nbsp;1001&#2
    0803;-3000&#20803;', '适用年龄:&nbsp;&#26032;&#29983;&nbsp;1&#20010;&#26376;&nbsp;2&
    #20010;&#26376;&nbsp;3&#20010;&#26376;&nbsp;4&#20010;&#26376;&nbsp;5&#20010;&#26376;
    &nbsp;6&#20010;&#26376;&nbsp;7&#20010;&#26376;&nbsp;8&#20010;&#26376;&nbsp;9&#20010;
    &#26376;&nbsp;10&#20010;&#26376;&nbsp;11&#20010;&#26376;&nbsp;12&#20010;&#26376;&nbs
    p;13&#20010;&#26376;&nbsp;14&#20010;&#26376;&nbsp;15&#20010;&#26376;&nbsp;16&#20010;
    &#26376;&nbsp;17&#20010;&#26376;&nbsp;18&#20010;&#26376;&nbsp;19&#20010;&#26376;&nbsp
    ;20&#20010;&#26376;&nbsp;21&#20010;&#26376;&nbsp;22&#20010;&#26376;&nbsp;23&#20010;&#
    26376;&nbsp;2&#23681;&nbsp;25&#20010;&#26376;&nbsp;26&#20010;&#26376;&nbsp;27&#20010;
    &#26376;&nbsp;28&#20010;&#26376;&nbsp;29&#20010;&#26376;&nbsp;30&#20010;&#26376;&nbsp
    ;31&#20010;&#26376;&nbsp;32&#20010;&#26376;&nbsp;33&#20010;&#26376;&nbsp;34&#20010;&#
    26376;&nbsp;35&#20010;&#26376;&nbsp;3&#23681;&nbsp;4&#23681;&nbsp;5&#23681;', '承重
    :&nbsp;25kg'"""

#print(a.encode('unicode-escape').decode('gb2312'))
print(a.encode('utf-8').decode('utf-8'))

'''
