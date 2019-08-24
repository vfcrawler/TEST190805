import urllib.parse

data =[
        'http',
        'www.baidu.com',
        'index.html',
        'id=5',
        'comment'
      ]

res = urllib.parse.urlunsplit(data)
print(res)

