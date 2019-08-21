import re

content1 = '''2016-12-15 12:00'''
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'

# 也支持修饰符
pattern = re.compile('\s+\d{2}:\d{2}',re.S)

# 返回_sre.SRE_Pattern 类型
print(type(pattern))

result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)

print(result1,result2,result3)