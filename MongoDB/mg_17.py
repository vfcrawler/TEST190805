from pymongo import MongoClient, ASCENDING,DESCENDING

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

# name 升序
result = collection.find().sort('name',ASCENDING)
print([ret['name'] for ret in result])

# name 降序
result = collection.find().sort('name',DESCENDING)
print([ret['name'] for ret in result])



