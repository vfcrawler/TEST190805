import requests

files = {
    'file': open('favicon.ico','rb')
}

res = requests.post('http://httpbin.org/post',files=files)
print(res.text)