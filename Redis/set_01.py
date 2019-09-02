from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

# 删除所有数据库中的所有键,返回是否删除成功
print(redis.flushall())

# 向键名为Tags集合添加Book、Tea和Coffee这三个内容
# 返回插入的数据个数
print(redis.sadd('Tags','Book','Tea','Coffee'))

# 从键名Tags的集合中删除Book
# 返回删除的数据个数
print(redis.srem('Tags','Book'))

# 从键名Tags的集合中随机删除一个元素
# 返回删除的元素
print(redis.spop('Tags'))

# 将Coffee内容从键名为Tags的集合中移动到键名为Tags2的集合中
# 返回是否移动成功
print(redis.smove('Tags','Tags2','Coffee'))

# 返回键名为name的集合中元素的个数
print(redis.scard('name'))

# 判断Book内容是否为键名为name的元素
print(redis.sismember('Tags','Book'))

redis.sadd('Tags','Book','Tea','Coffee')
redis.sadd('Tags1','Book','Tea','Coffee')

# 返回键名Tags集合和键名为Tags1集合的交集
print(redis.sinter('Tags','Tags1'))

# 取键名Tags集合和键名Tags1集合的交集
# 保存至键名为inttag的集合中,
# 返回插入键名为inttag集合的数据个数
print(redis.sinterstore('inttag',['Tags','Tags1']))

# 返回键名Tags的集合和键名Tags1的集合的并集
print(redis.sunion('Tags','Tags1'))

# 取键名Tags集合和键名Tags1集合的并集
# 保存至键名为inttag的集合中,
# 返回插入键名为inttag集合的数据个数
print(redis.sunionstore('inttag',['Tags','Tags1']))

# 返回键名为Tags集合和键名为Tags1的集合的差集
print(redis.sdiff('Tags','Tags1'))


# 取键名Tags集合和键名Tags1集合的差集
# 保存至键名为inttag的集合中,
# 返回插入键名为inttag集合的数据个数
print(redis.sdiffstore('inttag',['Tags','Tags1']))

# 返回tags键名的所有元素
print(redis.smembers('Tags'))


# 返回键名为Tags的集合中随机的一个元素
print(redis.srandmember('Tags'))











