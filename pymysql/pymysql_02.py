import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     port=3306)

cursor = db.cursor()
cursor.execute('select version()')

data = cursor.fetchone()
print('DataBase Version:',data)
cursor.execute("create database spiders default character set utf8mb4")
db.close()





