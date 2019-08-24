import requests

url = 'http://httpbin.org/post'

data = {
    'name':'germey'
}

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

s = requests.Session()
req = requests.Request(url=url,data=data,headers=headers,method='POST')

pre_req = s.prepare_request(req)

res = s.send(pre_req)

print(res.text)