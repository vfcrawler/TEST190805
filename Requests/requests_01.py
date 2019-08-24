import requests

res = requests.get('http://www.baidu.com')

print(type(res))
print(res)

print(res.status_code)
print(type(res.status_code))

print(type(res.text))
print(res.text)

print(type(res.content))
print(res.content)

print(type(res.cookies))
print(res.cookies)



