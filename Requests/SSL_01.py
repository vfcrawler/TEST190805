import requests

res = requests.get('https://www.jianshu.com')
print(res.status_code)
