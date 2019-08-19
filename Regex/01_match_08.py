import re

content = '(百度)www.baidu.com'

ret1 = re.match('\(百度\)www\.baidu\.com',content)

print(ret1.group())



