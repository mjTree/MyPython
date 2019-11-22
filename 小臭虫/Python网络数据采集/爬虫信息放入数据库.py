import requests
from bs4 import BeautifulSoup
import bs4
import pymysql

#--------------------------------------------------------------------
#--------------------------------------------------------------------
#连接数据库函数
def connDB(name,mima,shujuku):
    try:
        conn=pymysql.connect(host='localhost',user=name,passwd=mima,db=shujuku,port=3306,charset='utf8')
        #conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='imooc',port=3306,charset='utf8')
        cur=conn.cursor()#获取一个游标
        print(host)
        print('连接成功')
        return(conn,cur)
    except Exception:
        print("你的数据库服务器可能没有启动呀!!!!")

#可执行update,insert,delete语句
def exeSQL(conn,cur):
    try:
        sql = input("请输入一条sql语句:\n")
        sta = cur.execute(sql)
        data=cur.fetchall()
        print("耶,sql语句操作成功辣\n")
        if(sql[0] in ['S','s']):
            for d in data :
                #注意int类型需要使用str函数转义
                print("Sname:"+str(d[0])+"\tSno:"+d[1])
    except Exception:
        print("sql语句可能存在语法错误啦! ^_^")

def exeExit(conn,cur):
    cur.close()  #关闭游标
    conn.commit()#向数据库中提交未解决的事务,对不支持事务的数据库不进行操作
    conn.close() #释放数据库资源

#--------------------------------------------------------------------
#--------------------------------------------------------------------

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬虫累了,休息一下重新开始")
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num,conn,cur):

    try:
        sql = 'insert into info values("1","北大","98")'
        sta = cur.execute(sql)
        data=cur.fetchall()
        print("耶,sql语句操作成功辣\n")
        exeExit(conn,cur)
    except Exception:
        print("sql语句可能存在语法错误啦! ^_^")


    '''
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    #print(tplt.format("排名","学校名称","总分",chr(12288)))
    #print(tplt.format("0","湖北大学","你猜",chr(12288)))
    for i in range(num):
        u = ulist[i]
        try:
            sql = 'insert into info values("1","北大","98")'
            sta = cur.execute(sql)
            data=cur.fetchall()
            print("耶,sql语句操作成功辣\n")
            exeExit(conn,cur)
        except Exception:
            print("sql语句可能存在语法错误啦! ^_^")'''
          

def main():
    '''
    name = input('请输入用户名<一般为root>：')
    mima = input('请输入连接数据库密码：')
    shujuku = input('请输入要连接的数据库名称：')
    '''
    name = 'root'
    mima = '123456'
    shujuku = 'imooc'
    conn,cur = connDB(name,mima,shujuku)
    
    uinfo =[]
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    #printUnivList(uinfo,20,conn,cur) #只列出20个学校

    printUnivList(uinfo,1,conn,cur)

main()
