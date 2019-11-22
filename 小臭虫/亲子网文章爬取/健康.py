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


def getLink(html):
    linkList1 = []
    try:
        linkList = re.findall(r'<a href=\"/article.*?\"', html)
        print(len(linkList))
        #print(linkList)
        for i in range(len(linkList)):
            link = 'http://www.enmuo.com' + linkList[i].split('=')[1][1:-1]
            linkList1.append(link)
        return linkList1
    except:
        return linkList1


def parsePage(html):
    textList = []
    infoList = []
    try:
        titleList = re.findall(r'<h1>.*?<', html)
        #pList = re.findall(r'<p>\r\n.*?。', html)
        pList = re.findall(r'<p>\r\n\t\u3000\u3000.*?。', html)
        # 文章标题
        title = titleList[0].split('>')[1][0:-1]
        infoList.append(title)
        for i in range(len(pList)):
            p = str(pList[i])[6:]
            textList.append(p)
        infoList.append(textList)
        return infoList
    except:
        print('爬取失败')
        return infoList


def main():
    classify = ['孕前检查','生男生女','生殖保健','不孕不育','怀孕测试','营养保健','怀孕检查',
                '流产避免','孕妇禁忌','性知识','饮食技巧','胎教知识','孕妇心理','胎儿发育',
                '胎教知识','胎动感知','应急措施','助产器械','孕期心理','婴儿健康','母婴交流',
                '准妈必知','月子饮食','产后恢复','新生儿喂养','日常护理','母婴交流','智力玩具'
                '早产儿','心理健康','妈妈健康','潜能激活','早教天地','疾病预防','婴儿食谱',
                '婴儿用品','孕妇心理','免疫接种','兴趣开发','婴儿护理','亲子活动'
                ]
    
    for i in classify:
        name = str(i) + '.txt'
        url = 'http://www.enmuo.com/search/1?q=' + str(i) +'&type=0'
        html = getHTMLText(url)
        #print(html)
        link = getLink(html)
        for j in range(len(link)):
            if j <= 10:
                html = getHTMLText(str(link[j]))
                infoList = parsePage(html)
                with open(name,'a',errors='ignore') as f:
                    f.write(str(infoList[0])+'\n')
                    for m in infoList[1]:
                        f.write('\n' + str(m))
                    f.write('\n\n\n\n\n')

main()

