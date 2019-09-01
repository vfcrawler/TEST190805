from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

# 向键名为list的列表尾添加1、2、3;返回列表大小
print(redis.rpush('list',1,2,3,4,5))

# 向键名为list的列表头部添加0;返回列表大小
print(redis.lpush('list',0))

# 返回键名为list的列表长度
print(redis.llen('list'))

# 返回起始索引范围为1-3对应的列表
print(redis.lrange('list',1,3))

# 保留键名为list的索引为1-3的元素,返回True|False
print(redis.ltrim('list',1,3))

# 返回键名为list列表索引为1的元素,返回True|False
print(redis.lindex('list',1))

# 将键名为list的列表中索引为1的位置赋值5
print(redis.lset('list',1,5))

# 将键名为list的列表删除2个3,返回实际删除的个数
print(redis.lrem('list',2,0))

# 返回并删除键名为list的列表的第一个元素
print(redis.lpop('list'))

# 返回并删除键名为list的列表的最后一个元素
print(redis.rpop('list'))

# 返回并删除键名为list列表的首个元素
# 如果列表为空则会一直处于阻塞等待
# timeout:超时等待时间，0为一直等待
# 返回元组类型
print(redis.blpop('list',timeout=0))

# 返回并删除键名为list列表的最后一个元素
# 如果列表为空则会一直处于阻塞等待
# timeout:超时等待时间，0为一直等待
# 返回元组类型
print(redis.brpop('list',timeout=0))

# 将键名为list的列表尾元素删除
# 并将其添加到键名为list1的列表头部
# 返回该元素
print(redis.rpoplpush('list','list1'))






















