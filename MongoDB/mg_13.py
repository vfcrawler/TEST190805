from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

result = collection.find({'age':{'$gt':20}})

print(type(result))

for e in result:
    print(e)
