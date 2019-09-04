from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379'

pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

print(redis.flushall())
