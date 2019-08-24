import requests

proxies = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}

res = requests.get('https://www.taobao.com',proxies=proxies,verify=False)
print(res.status_code)
