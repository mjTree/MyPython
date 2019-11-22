#coding:utf-8

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.admin
db.authenticate('admin', '123456')


my_db = client.mydb
#my_db = client['mydb']
collection = my_db.myset
#collection = my_db['myset']


'''
# 添加一条信息
collection.insert({"name":"zhangsan","age":18})
# 添加多条信息
mylist = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]
x = collection.insert_many(mylist)
'''


'''
# 删除信息
myquery = {"name":"薛志豪"}
collection.delete_one(myquery)
collection.delete_many(myquery)
for i in collection.find():
    print(i)

# 删除集合
collection.drop()
'''


'''
# 查看第一条信息
x = collection.find_one()
print(x)
# 查看所有信息
for i in collection.find():
    print(i)
# 条件查询数据
for i in collection.find({},{"order_id":1}):
    print(i)
'''


'''
# 修改数据
myquery = {"name":"zhangsan"}
newvalues = {"$set":{"name":"薛志豪"}}
collection.update_one(myquery, newvalues)
#collection.update_many(myquery, newvalues)
for i in collection.find():
    print(i)
'''







