'''
@描述：数据库连接池管理模块
@作者：mjTree
@版本：V1.0
@创建时间：2017-12-06 晚上20:58
'''

import pymysql
from DBUtils.PooledDB import PooledDB
import DB_config as Config



'''
function: 创建和关闭mysql数据库连接池
'''   
class PTConnectionPool(object):
    __pool = None
    """
    function: 创建连接池
    return: self.__pool.connection() 连接池指针
    """
    def __getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql, mincached=Config.DB_MIN_CACHED , maxcached=Config.DB_MAX_CACHED, 
                                   maxshared=Config.DB_MAX_SHARED, maxconnections=Config.DB_MAX_CONNECYIONS, 
                                   blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE, 
                                   setsession=Config.DB_SET_SESSION,
                                   host=Config.DB_TEST_HOST , port=Config.DB_TEST_PORT , 
                                   user=Config.DB_TEST_USER , passwd=Config.DB_TEST_PASSWORD ,
                                   db=Config.DB_TEST_DBNAME , use_unicode=False, charset=Config.DB_CHARSET);
        return self.__pool.connection()

    """
    function: 创建con和cursor连接数据库
    return: self 连接数据库指针
    """
    def __enter__(self):
        self.conn = self.__getConn()
        self.cursor = self.conn.cursor()
        print("mysql数据库创建con和cursor")
        return self
    
    """
    function: 释放连接池的资源
    """
    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()
        print("mysql连接池释放con和cursor")

'''
function: 获取mysql数据库的连接
'''  
def getPTConnection():
    return PTConnectionPool()
