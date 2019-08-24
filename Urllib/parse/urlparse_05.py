import urllib.parse

res = urllib.parse.urlparse('http://www.baidu.com#comment',
                            allow_fragments=False)
print(res)

