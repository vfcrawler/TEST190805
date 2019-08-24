import requests

res = requests.get('https://www.zhihu.com/explore',verify=False)
print(res.text)

