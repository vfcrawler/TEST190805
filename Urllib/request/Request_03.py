from urllib import request,parse

url = 'http://httpbin.org/post'

dict = {'Hello':'World'}

data = bytes(parse.urlencode(dict),encoding='utf-8')

req = request.Request(url,data=data,method='Post')

# 使用add_header设置headers头部信息的User-Agent属性
req.add_header('User-Agent','Mozilla/4.0(compatible; MSIE 5.5; Windows NT)')

# 使用add_header设置headers头部信息的Host属性
req.add_header('Host','httpbin.org')

res = request.urlopen(req)

print(res.read().decode('utf-8'))


