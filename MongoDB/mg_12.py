from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

result = collection.find({'age':20})

# 返回生成器类型Cursor
print(type(result))

for e in result:
    print(e)




