import re

content = 'Hello 1234567 World_This is a Regex Demo'

ret = re.match(r'^Hello\s(\d+)\sWorld',content)

print(ret.group())
print(ret.span())
print(ret.group(1))


