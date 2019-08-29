from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)
redis = StrictRedis(connection_pool=pool)

# 设置name键值
print('设置name1键值返回结果:',redis.set('name1','Bob1'))
print('设置name2键值返回结果:',redis.set('name2','Bob2'))
print('设置name3键值返回结果:',redis.set('name3','Bob3'))

# 判断键是否存在
print('判断name1键是否存在返回结果:',redis.exists('name1'))

# 判断键的类型
print('name1键的类型:',redis.type('name1'))

# 获取当前数据库所有符合规则的键
print('输出当前数据库中键名以n打头的键：',redis.keys('n*'))

# 获取随机一个键
print('获取随机一个键:',redis.randomkey())

# 将name1键 重命名为 name1_1
print('name1键 重命名为 name1_1返回结果:',
      redis.rename('name1','name1_1'))

# 获取当前数据库中键的数目
print('当前数据库中键的数目:',redis.dbsize())

# 设定name3键的过期时间
print('设定name3键的过期时间:',redis.expire('name3',20))

# 获取name3键的过期时间
print('获取name3键的过期时间:',redis.ttl('name3'))

# 获取name2键的过期时间
print('获取name2键的过期时间:',redis.ttl('name2'))

# 将键移到其他数据库
print('将键移到其他数据库:',redis.move('name1_1',2))

# 获取当前数据库所有键
print('获取当前数据库所有键:',redis.keys('*'))

# 删除name2键
print('删除name2键返回结果:',redis.delete('name2'))

# 删除当前数据库所有键
print('删除当前数据库所有键:',redis.flushdb())

# 删除所有数据库中的所有键
print('删除所有数据库的所有键:',redis.flushall())



