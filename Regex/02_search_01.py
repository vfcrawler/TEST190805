import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

ret = re.search('Hello.*?(\d+).*?Demo',content)

print(type(ret))
print(ret)

print(ret.group())
print(ret.group(1))



