from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db.student

# 指定学号，姓名，年龄，性别
students = {
    'id':'270101',
    'name':'Jordan',
    'age':20,
    'gener':'male'
}

result = collection.insert(students)

print(result)



