import pymysql

data = {
    'id':'20120002',
    'name':'Bob',
    'age':20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

sql = 'insert into {table} ({keys}) values ({values})'.format(table=table,
                                                              keys=keys,
                                                              values=values)
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
    result = cursor.execute(sql,tuple(data.values()))
    print(result)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
