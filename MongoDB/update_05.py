from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

condition = {'age':{'$gt':20}}
result = collection.update_many(condition,{'$inc':{'age':1}})
print(type(result))
print(result)
print(result.matched_count,result.modified_count)

