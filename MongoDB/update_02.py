from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

condition = {'name':'Jordan'}
student = collection.find_one(condition)
student['age'] = 28

result = collection.update(condition,{'$set':student})
print(result)
