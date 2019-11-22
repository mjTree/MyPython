#coding=utf-8
'''
@描述：通过连接池直接调用mysql
@作者：mjTree
@版本：V1.0
@创建时间：2017-12-06 晚上20:58
'''
from DB_connetion_pool import getPTConnection, PTConnectionPool


"""
function: 从mysql数据库中读取相应表的信息
return: dataset 数据集
# http://blog.csdn.net/cyh1111/article/details/53337895
"""
def TestMySQL():
    #申请资源  
    with getPTConnection() as db:
        # SQL 查询语句;
        tables = input('输入你要提供的表名：')
        sql = 'select * from ' + tables
        try:
            # 获取所有记录列表
            db.cursor.execute(sql)
            results = db.cursor.fetchall()
            dataset = []
            temp = []
            for row in results:
                for column in range(len(row)):
                    temp.append(row[column].decode())
                dataset.append(temp)
                temp = []
            return dataset
        except:
            print("出错:无法获取数据,请检查数据库")

