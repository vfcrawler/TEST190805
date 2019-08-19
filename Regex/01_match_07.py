import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

ret = re.match(r'^Hello.*?(\d+).*?Demo$',content,re.S)
print(ret)



