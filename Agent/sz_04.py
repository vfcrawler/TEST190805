import requests

proxy = '127.0.0.1:9743'

proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy
}

try:
    res = requests.get('http://httpbin.org/get',proxies=proxies)
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('Error:',e.args)

