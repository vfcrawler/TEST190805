from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['student']
collection = db['student']

# 指定sut1学号，姓名，年龄，性别
stu1 = {
    'id':'270101',
    'name':'Jordan',
    'age':20,
    'gener':'male'
}

# 指定sut2学号，姓名，年龄，性别
stu2 = {
    'id':'270102',
    'name':'Lucy',
    'age':28,
    'gener':'fmale'
}

result = collection.insert_many([stu1,stu2])
print(type(result))
print(type(result.inserted_ids))
print(result.inserted_ids)


