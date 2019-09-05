from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

condition = {'name':'Jordan'}
result = collection.delete_one(condition)
print(type(result))
print(result)
print(result.deleted_count)

