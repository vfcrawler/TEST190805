from urllib import request,parse

url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}

dict = {'Hello':'World'}

data = bytes(parse.urlencode(dict),encoding='utf-8')

req = request.Request(url,data=data,headers=headers,method='Post')
res = request.urlopen(req)

print(res.read().decode('utf-8'))


