from redis import StrictRedis

redis = StrictRedis(host='localhost',
                    port=6379,
                    db=0,
                    password='wei8899')
# 设置name键的值
redis.set('name','Bob')
# 输出name键值的类型
print(type(redis.get('name')))
# 输出name键的值
print(redis.get('name'))


