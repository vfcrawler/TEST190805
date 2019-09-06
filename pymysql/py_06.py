import pymysql

sql = 'update students set age=%s where name=%s'
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
    result = cursor.execute(sql,(25,'Bob'))
    print(result)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
