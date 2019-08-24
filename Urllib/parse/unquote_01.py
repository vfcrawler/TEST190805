import urllib.parse

url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'

print(urllib.parse.unquote(url))

