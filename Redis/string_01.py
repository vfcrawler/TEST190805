from redis import StrictRedis,ConnectionPool

url = 'redis://:wei8899@localhost:6379/0'
pool = ConnectionPool.from_url(url=url)

redis = StrictRedis(connection_pool=pool)

# 给name键赋值为Bob
print('给name键赋值为Bob:',redis.set('name','Bob'))
print('给nickname键赋值为Bob_nick:',redis.set('nickname','Bob_nick'))

# 返回name键的value值
print('返回name键的value值:',redis.get('name'))

# 赋值name键为Mike，并得到上次的value
print('赋值name键为Mike，并得到上次的value:',
      redis.getset('name','Mike'))

# 返回name键和nickname键的value(列表类型)
print('返回name键和nickname键的value:',
      redis.mget(['name','nickname']))

# 如果不存在newname这个键不存在
# 则设置为James
print('如果不存在newname这个键不存在,则设置为James:',
      redis.setnx('newname','James'))

# 将name键的值设为James，有效期为1秒
print('将name键的值设为James，有效期为1秒:',
      redis.setex('name',1,'James'))

# 设置name为hello字符串，
# 并在index为6的位置补world
redis.set('name','hello')
print('设置name为hello字符串,并在index为6的位置补world:',
      redis.setrange('name',6,'world'))

# 将name1设置为Durant,name2设置为James
print('将name1设置为Durant,name2设置为James:',
      redis.mset({'name1':'Durant','name2':'James'}))

# 在name3和name4键都不存在的情况下才设置二者的值
print('在name3和name4键都不存在的情况下才设置二者的值:',
      redis.msetnx({'name3':'Smith','name4':'Curry'}))

# age键对应的值增1，如不存在，则会创建并设置1
# 返回修改后的值
print('age键对应的值增1，如不存在，则会创建并设置1:',
      redis.incr('age',amount=1))

# age键对应的值减1，如不存在，则会创建并设置-1
# 返回修改后的值
print('age键对应的值减1，如不存在，则会创建并设置-1:',
      redis.decr('age',amount=1))

# 向键名为nickname的值追加OK
# 返回修改后字符串的长度
print('向键名为nickname的值追加OK:',
      redis.append('nickname','OK'))

# 返回键名为name的字符串，
# 并截取索引1-4的字符
print('返回键名为name的字符串,并截取索引1-4的字符:',
      redis.substr('name',1,4))

# 返回键名为name的字符串，
# 并截取索引1-4的字符
print('返回键名为name的字符串,并截取索引1-4的字符:',
      redis.getrange('name',1,4))


