import requests

res = requests.get('http://localhost:5000',
                   auth=('username','password'))

print(res.status_code)
