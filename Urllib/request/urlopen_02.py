import urllib.request

res1 = urllib.request.urlopen('http://www.baidu.com')
res2 = urllib.request.urlopen('https://www.python.org')

# 返回 http.client.HTTPResponse 类型
print(type(res1))

# 返回响应内容的类型
print(type(res1.read()))

# 读取响应内容
print(res2.read().decode('utf-8'))


