import requests
import os
import re

def getHTMLText(url):
     try:
          url = '''https://image.baidu.com/search/index?tn=baiduimage&ipn=
               r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=11
               1111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&he
               ight=&face=0&istype=2&ie=utf-8&word='''+ url
          r = requests.get(url,timeout=30)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          return r.text
     except:
          print("爬取网页失败辣")
          return ""

def parsePage(ilt, html):
    try:
         p = r'URL":"([^"]*\.jpg)".*?,'
         imglist = re.findall(p,html)
         for i in imglist:
              if str(i).split(':')[1][0] != '\\':
                   ilt.append(i)
    except:
         print("爬取图片连接出错辣")

def pictureSave(ilt):
     j = 1
     n = 0
     n = input('请输入默认一次爬取多少张图片:')
     for i in ilt:
          url = i
          root = "D://zzzzz//"
          path = root + url.split('/')[-1]
          try:
               if not os.path.exists(root):
                    os.mkdir(root)
               if not os.path.exists(path):
                    r = requests.get(url)
                    with open(path,'wb') as f:
                         f.write(r.content)
                         f.close()
                         print('第{}张图片保存成功'.format(j))
                         j=j+1
                         #print("文件保存成功")
               else:
                    print("第{}张图片已存在".format(j))
          except:
               print("爬取图片失败")
          if(j%int(n)==0):
               print('\n已经爬取{}张照片'.format(n))
               ch = input('是否继续爬取(Y/N):')
               if(ch=='Y'or ch=='y'):
                    n = int(n)+int(j)
                    continue
               elif ch=='N'or ch=='n':
                    print('爬取结束')
                    return
               else:
                    exit

def main():
     url = input('请输入要爬取的关键字:')
     infoList = []
     #pic = getHTMLText(url)
     html = getHTMLText(url)
     parsePage(infoList,html)
     print(len(infoList))
     for i in range(len(infoList)):
          if (len(infoList[i])>=90) and (len(infoList[i]) != len(infoList[i+1])):
               print(infoList[i])
     #pictureSave(infoList)
     
main()
