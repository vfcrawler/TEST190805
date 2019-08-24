import requests

res = requests.get('http://www.baidu.com')
print(res.cookies)
print(res.cookies.items())
for k,v in res.cookies.items():
    print(k+'='+v)