import requests
import urllib.parse

# 定义URL
url = 'http://httpbin.org/post'

# 定义data
data = {
    'name':'workd'
}

# 定义headers
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 定义requests.Session对象
s = requests.Session()

# 构造requests.Request对象
req = requests.Request(url=url,data=data,headers=headers,method='POST')

# 将requests.Request对象转化为 Prepared Request对象
pre_req = s.prepare_request(req)

# 调用requests.Session对象的send方法
res = s.send(pre_req)

print(res.text)