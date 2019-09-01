from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)


# 返回并删除键名为list列表的最后一个元素
# 如果列表为空则会一直处于阻塞等待
# timeout:超时等待时间，0为一直等待
# 返回元组类型
print(redis.brpop('list',timeout=0))

# 将键名为list的列表尾元素删除
# 并将其添加到键名为list1的列表头部
# 返回该元素
print(redis.rpoplpush('list','list1'))
