from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

# 统计所有的数据条数
result = collection.count()

print(type(result))
print(result)


