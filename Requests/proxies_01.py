import requests

proxies = {
 'http':'http://10.10.1.10.3128',
 'https':'https://10.10.1.10.3128'
}

res = requests.get('https://www.taobao.com',proxies=proxies)
print(res.status_code)

