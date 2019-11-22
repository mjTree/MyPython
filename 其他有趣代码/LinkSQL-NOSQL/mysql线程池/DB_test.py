#coding=utf-8
'''
@描述：通过连接池直接调用mysql
@作者：mjTree
@版本：V1.0
@创建时间：2017-12-06 晚上20:58
'''
from DB_connetion_pool import getPTConnection, PTConnectionPool

def TestMySQL():
    #申请资源  
    with getPTConnection() as db:
        # SQL 查询语句;
        sql = 'select * from users'
        try:
            # 获取所有记录列表
            db.cursor.execute(sql)
            results = db.cursor.fetchall()
            for row in results:
                userId = row[0]
                name = row[1].decode()
                nickname = row[2].decode()
                hobby = row[6].decode()
                # 打印结果
                print("userId=%d \t 姓名=%s \t 昵称=%s \t 兴趣=%s" %\
                     ( userId, name, nickname, hobby ) )
        except:
            print("Error: unable to fecth data")

TestMySQL()

#http://blog.csdn.net/cyh1111/article/details/53337895
