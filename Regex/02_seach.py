import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

ret = re.match('Hello.*?(\d+).*?Demo',content)

print(ret)

