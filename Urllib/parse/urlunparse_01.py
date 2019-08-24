import urllib.parse

data = [
        'http',
        'www.baidu.com',
        'index.html',
        'user',
        'id=6',
        'comment'
        ]
res = urllib.parse.urlunparse(data)
print(type(res))
print(res)

