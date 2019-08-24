import requests

res = requests.get('https://www.taobao.com',timeout=None)

print(res.status_code)

