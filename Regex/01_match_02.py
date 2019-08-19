import re

content = 'Hello 123 4567 World_This is a Regex Demo'

ret = re.match(r'^Hello.*Demo$',content)

print(type(ret))
print(ret)

print(ret.group())
print(ret.span())
