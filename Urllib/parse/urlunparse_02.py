import urllib.parse

data = [
        'http',
        'www.baidu.com',
        'index.html',
        'user'
        ]
res = urllib.parse.urlunparse(data)
print(type(res))
print(res)