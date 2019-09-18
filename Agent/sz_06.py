import requests

proxy = '127.0.0.1:9742'

proxies = {
    'http':'socks5://'+proxy,
    'https':'socks5://'+proxy
}

try:
    res = requests.get('http://httpbin.org/get',proxies=proxies)
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('Error:',e.args)



