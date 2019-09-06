import pymysql
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port = 3306,
    db='spiders'
)
cursor = db.cursor()
sql = 'select * from students where age>10'

try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
except:
    print('error')

