import requests

res = requests.get('https://www.taobao.com',timeout=(2,5))

print(res.status_code)
