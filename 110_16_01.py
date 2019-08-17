import re

str_input = '<div class="nam">中国</div>'

res = re.findall(r'<div class=".*">(.*?)</div>',str_input)

print(type(res))

print(res)




