import re

content = 'Hello 123 4567 World_This is a Regex Demo'

ret = re.match(r'Hello\s\d{3}\s\d{4}\s\w{10}',content)
# 返回 <class '_sre.SRE_Match'> 类型
print(type(ret))
print(ret)

# group()方法返回匹配规则的第一个字符串(字符串类型)
print(type(ret.group()))
print(ret.group())

# 返回匹配字符串的开始和结束的索引(元组类型)
print(type(ret.span()))
print(ret.span())




