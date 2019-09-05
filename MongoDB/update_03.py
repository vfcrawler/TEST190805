from pymongo import MongoClient

client = MongoClient(host='mongodb://localhost:27017')
db = client['test']
collection = db['student']

condition = {'name':'Jordan'}
student = collection.find_one(condition)
student['age'] = 89

result = collection.update_one(condition,{'$set':student})
print(type(result))
print(result)
print(result.matched_count,result.modified_count)

