from bson import ObjectId
from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

condition = {"_id" : ObjectId("5d6f6e9d29172bba72856c51")}

result = collection.remove(condition)
print(type(result))
print(result)




