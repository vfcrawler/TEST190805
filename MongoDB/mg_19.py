from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

result = collection.find().skip(2).limit(3)
print([ret['name'] for ret in result])
