from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

# 统计符合某个条件的数据条数
result = collection.find({'name':{'$regex':'^J.*'}}).count()

print(type(result))
print(result)

