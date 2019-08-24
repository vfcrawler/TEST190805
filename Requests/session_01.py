import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/num/123122312')
res = s.get('http://httpbin.org/cookies')
print(res.text)


