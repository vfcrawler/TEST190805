from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

# 获取test数据库
db = client.test




