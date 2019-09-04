from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

# 向键名为grade的有序集合中添加Bob(分数为100),
# 添加Mike(分数为90),返回添加的元素个数
# 传入参数为字典类型,{'元素名称':分数.....}
print(redis.zadd('grade',{'Bob':100,'Mike':90}))

# 删除键名为grade的有序集合中的Mike元素
# 返回删除的元素个数
print(redis.zrem('grade','Mike'))

# 修改键名为grade的有序集合中的Bob元素对应的分数减2
# 返回修改后元素的分数
print(redis.zincrby('grade',-2,'Bob'))

redis.zadd('grade',{'Tom':120,'Limy':140,'Jack':97})

# 返回键名grade的有序集合中Limy元素的排名
# 从小到大排序(排名从0开始)
print(redis.zrank('grade','Limy'))

# 返回键名grade的有序集合中Limy元素的排名
# 从大到小排序(排名从0开始)
print(redis.zrevrank('grade','Limy'))

# 返回键名为grade的有序集合中,分数排名从1至4的元素
# 其排序是按照分数从小到大
print(redis.zrange('grade',0,3))

# 返回键名为grade的有序集合中,分数排名从1至4的元素
# 其排序是按照分数从大到小
print(redis.zrevrange('grade',0,3))

# 返回键名为grade的有序集合中,其分数值处于110-190的元素
# 其结果是按照从小到大的排序方式
print(redis.zrangebyscore('grade',110,190))

# 返回键名为grade的有序集合中,其分数值处于190-110的元素
# 其结果是按照从大到小的排序方式
print(redis.zrevrangebyscore('grade',190,110))

# 返回键名grade在给定区间90-190之间的元素个数
print(redis.zcount('grade',90,190))

# 返回键名grade的所有元素的个数
print(redis.zcard('grade'))

# 删除键名为grade的有序集合中其分数排名为给定区间的元素
# 排名是按从小到大的顺序
# 返回删除的元素的个数
print(redis.zremrangebyrank('grade',0,3))

# 删除键名为grade的有序集合中其分数为给定区间的元素
# 分数是按从小到大的顺序
# 返回删除的元素的个数
print(redis.zremrangebyscore('grade',90,190))


















