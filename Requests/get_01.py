import requests

res = requests.get('http://httpbin.org/get')
print(type(res.text))
print(res.text)
