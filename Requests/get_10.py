import requests

res = requests.get('http://ww.baidu.com')

exit() if not res.status_code == requests.codes.ok else print('Request Successfully')
