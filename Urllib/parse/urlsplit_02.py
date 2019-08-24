import urllib.parse

res = urllib.parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')

print('用属性名res.scheme获取：'+res.scheme)
print('用索引res[0]获取：'+res[0])
print('用属性名res.netloc获取：'+res.netloc)
print('用索引res[1]获取：'+res[1])