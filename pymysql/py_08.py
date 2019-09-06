import pymysql
table = 'students'
condition = 'age>20'
sql = 'delete from {table} where {condition}'.format(table=table,
                                                    condition=condition)
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port = 3306,
    db='spiders'
)
cursor = db.cursor()
try:
    result =  cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()


