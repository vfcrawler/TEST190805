import urllib.request

res = urllib.request.urlopen('http://www.baidu.com')

# 返回 http.client.HTTPResponse 类型
print(type(res))

# 返回响应的头部信息headers 元组列表类型
print(res.getheaders())

# 返回响应的头部信息headers中指定key的值
print(res.getheader('Server'))

# 返回响应结果的状态码 200-请求成功,404-网页未找到
print(res.status)














