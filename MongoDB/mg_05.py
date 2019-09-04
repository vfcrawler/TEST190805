from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')

# 指定test数据库
db = client['test']

# 指定集合方式1
collection = db['student']

# 指定集合方式2
collection = db.student

print(collection)





