import requests

res = requests.get('http://httpbin.org/get')

print(type(res.json()))
print(res.json())


