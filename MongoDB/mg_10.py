from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

result = collection.find_one({'name':'Lucy'})

print(type(result))

print(result)