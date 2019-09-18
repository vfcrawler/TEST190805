import requests

proxy = 'ad240066:Sem900917@172.16.1.117:8080'

proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy
}

try:
    res = requests.get('http://httpbin.org/get',proxies=proxies)
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('Error:',e.args)




