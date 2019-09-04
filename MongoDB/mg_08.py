from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

# 指定sut1学号，姓名，年龄，性别
stu1 = {
    'id':'270101',
    'name':'Jordan',
    'age':20,
    'gener':'male'
}

result = collection.insert_one(stu1)

# 返回InsertOneResult类型
print(type(result))
print(result.inserted_id)


