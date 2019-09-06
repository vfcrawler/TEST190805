import pymysql

data={
    'id':'20120004',
    'name':'Bob4',
    'age':20
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

sql = 'insert into {table} ({keys}) values({values}) on duplicate key update '.format(
    table=table,
    keys=keys,
    values=values)
update = ','.join(['{key}=%s'.format(key=e) for e in data])
sql += update

print(sql)


db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    db='spiders'
)
cursor = db.cursor()
try:
    result = cursor.execute(sql,tuple(data.values())*2)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()

