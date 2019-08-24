import requests

res = requests.get('https://www.jianshu.com',cert=('/path/server.crt','/path/key'))
print(res.status_code)

