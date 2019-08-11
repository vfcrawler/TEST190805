import datetime

def dayofyear(dt):
    datetime1 = dt
    datetime2 = datetime.date(year=int(datetime1.year), month=1, day=1)
    return (datetime1-datetime2).days+1


if __name__ == '__main__':

    try:
        year = input('请输入年份:')
        month = input('请输入月份:')
        day = input('请输入天:')

        datetime1 = datetime.date(year=int(year), month=int(month), day=int(day))
        dayofyear = dayofyear(datetime1)

        print('%s是%d年中的第%d天'%(
                                    datetime1.strftime('%Y-%m-%d'),
                                    datetime1.year,
                                    dayofyear ))

    except Exception as e:
        print('输入异常:',e)

