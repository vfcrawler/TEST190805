import requests

s = requests.session()
s.get('http://httpbin.org/cookies/set/num/123122312')
res = s.get('http://httpbin.org/cookies')
print(res.text)


