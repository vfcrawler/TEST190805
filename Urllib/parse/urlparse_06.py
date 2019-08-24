import urllib.parse
res = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(res))
print(res)
print('用属性名scheme获取:',res.scheme)
print('用索引获取:',res[0])

print('用属性名netloc获取:',res.netloc)
print('用索引获取:',res[1])


