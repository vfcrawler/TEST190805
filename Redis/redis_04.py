from redis import StrictRedis,ConnectionPool

# 使用Redis TCP连接
url = 'redis://:wei8899@localhost:6379/0'

pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

redis.set('name','Bob')
print(redis.get('name'))



