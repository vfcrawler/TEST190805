from redis import StrictRedis,ConnectionPool

pool = ConnectionPool(host='localhost',port=6379,db=0,password='wei8899')
redis = StrictRedis(connection_pool=pool)

redis.set('name','Bob')
print(type(redis.get('name')))
print(redis.get('name'))
