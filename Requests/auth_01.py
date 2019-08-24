import requests
import requests.auth

res = requests.get('http://localhost:5000',
                   auth=requests.auth.HTTPBasicAuth('username','password'))
print(res.status_code)



