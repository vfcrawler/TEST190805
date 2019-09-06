import pymysql


db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    port = 3306,
    db = 'spiders'
)
cursor = db.cursor()
sql = 'insert into students (id,name,age) values (%s,%s,%s)'

try:
    result = cursor.execute(sql, ('20120001', 'Bob', 20))
    print(result)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
