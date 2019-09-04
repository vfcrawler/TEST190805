from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)
redis = StrictRedis(connection_pool=pool)

redis.flushall()

# 向键名为price的散列表添加映射关系,cake的值为5
# 返回添加至price散列表中的元素个数
print(redis.hset('price','cake',5))

# 如果book映射关系不存在
# 则向键名为price的散列表中添加映射关系,book的值为6
# 返回添加至price散列表的元素个数
print(redis.hsetnx('price','book',6))

# 返回键名为price的散列表中,键值为book的值
print(redis.hget('price','book'))

# 批量返回键名为price的散列表中，键值为book,cake的值
print(redis.hmget('price',['book','cake']))

# 向键名为price的散列表中，批量添加映射
# 返回是否添加成功
print(redis.hmset('price',{'book1':'67','cake1':123}))

# 将键名为price的散列表中的book1的值加1
# 返回book1键修改后的值
print(redis.hincrby('price','book1',1))

# 判断键名为price的散列表中是否存在book键
print(redis.hexists('price','book'))

# 删除键名为price的散列表中book键、cake键
# 返回删除的个数
print(redis.hdel('price','book','cake'))

# 返回键名为price的散列表中映射的个数
print(redis.hlen('price'))

# 获取键名为price的散列表中所有映射的的键名
print(redis.hkeys('price'))










