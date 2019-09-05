from pymongo import MongoClient

client = MongoClient(host='mongodb://127.0.0.1:27017')
db = client['test']
collection = db['student']

result = collection.find({'name':{'$regex':'^J.*'}})
print(type(result))
for e in result:
    print(e)




