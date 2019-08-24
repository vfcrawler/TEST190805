import urllib.parse

res = urllib.parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(type(res))
print(res)
