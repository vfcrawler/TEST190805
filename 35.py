import datetime

year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入该月的第几天:'))

targetdate = datetime.date(year,month,day)
dayofyear = (targetdate-datetime.date(year-1,12,31)).days

print('日期%s是%s年中的第%s天,请知悉!'
      %(targetdate.strftime('%Y-%m-%d'),year,dayofyear))

