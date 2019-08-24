import requests

res = requests.get('https://www.taobao.com',timeout=1)

print(res.status_code)
