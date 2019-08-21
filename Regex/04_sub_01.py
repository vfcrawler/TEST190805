import re

content = '54aK54yr5oiR54ix5L2g'

ret  = re.sub('\d+','',content,re.S)

# 返回字符串类型
print(type(ret))

# 返回替换后的字符串
print(ret)

