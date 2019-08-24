import urllib.parse

res = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=2#comment',
                            allow_fragments=False)
print(res)