import requests

data={
    'name':'germy',
    'age':22
}
res = requests.post('http://httpbin.org/post',data=data)
print(res.text)
