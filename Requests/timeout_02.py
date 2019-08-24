import socket

import requests

try:
    res = requests.get('https://www.taobao.com',timeout=0.1)
except requests.exceptions.ReadTimeout as e:
    print('Time Out')
else:
    print(res.status_code)
