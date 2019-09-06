import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     port=3306,
                     db='spiders')
cursor = db.cursor()

sql = '''
create table if not exists students
(
id varchar(255) NOT NULL,
name VARCHAR(255) NOT null,
age int not null,
primary key(id)
)
'''
result = cursor.execute(sql)
db.close()