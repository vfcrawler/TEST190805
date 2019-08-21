import urllib.request

# 构造Request对象
request = urllib.request.Request('http://www.baidu.com')

# 使用Urlopen(Request对象)的方式发送请求
res = urllib.request.urlopen(request)

print(res.read().decode('utf-8'))