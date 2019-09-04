from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

result = collection.find_one({'_id':ObjectId('5d6f6c0242e3c9bdef62739d')})

print(type(result))

print(result)






