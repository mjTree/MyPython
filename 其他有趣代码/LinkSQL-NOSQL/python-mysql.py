import pymysql

#连接数据库函数
def connDB(name,mima,shujuku):
    try:
        conn=pymysql.connect(host='localhost',user=name,passwd=mima,db=shujuku,port=3306,charset='utf8')
        #conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='imooc',port=3306,charset='utf8')
        cur=conn.cursor()#获取一个游标
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

def main():
    name = input('请输入用户名<一般为root>：')
    mima = input('请输入连接数据库密码：')
    shujuku = input('请输入要连接的数据库名称：')
   
    link = input("是否连接mysql数据库? (Y/N)\n")
    if(link == 'N'or link == 'n'):
        print("自动退出程序")
        exit
    elif(link == 'Y' or link == 'y'):
        while(1):
            conn,cur = connDB(name,mima,shujuku)
            exeSQL(conn,cur)
            exeExit(conn,cur)
            c = input("是否继续进行操作? (Y/N):\n")
            if(c == 'Y' or c == 'y'):
                continue
            elif(c =='N' or c == 'n'):
                print('关闭与数据的连接')
                print("程序结束")
                break
            else:
                print("不知道你想干啥")
    else:
        print("不知道你想干啥")
main()
