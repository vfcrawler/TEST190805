import urllib.parse

# url中存在http协议
# schema参数指定https协议
res = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment',
                            scheme='https')
print(res)
