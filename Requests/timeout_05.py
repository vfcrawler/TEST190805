import requests

res = requests.get('https://www.taobao.com')

print(res.status_code)

