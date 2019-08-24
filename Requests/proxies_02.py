import requests
import urllib3

proxies = {
    'http':'http:user:password@10.10.1.10:3128'
}

urllib3.disable_warnings()

res = requests.get('https://www.taobao.com',proxies=proxies,verify=False)

print(res.status_code)


