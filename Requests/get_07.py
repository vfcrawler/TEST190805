import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res = requests.get('https://www.zhihu.com/explore',headers=headers,verify=False)
print(res.text)





