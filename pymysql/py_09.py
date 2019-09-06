import pymysql

sql= 'select * from students where age>=20'

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    db='spiders'
)

cursor = db.cursor()

try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)
    one = cursor.fetchone()
    print('one:',one)
    results = cursor.fetchall()
    print('Results Type:',type(results))
    print('Results:',results)
    for e in results:
        print(e)
except:
    print('Error')



