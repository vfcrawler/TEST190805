from urllib.request import  HTTPBasicAuthHandler
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import build_opener
from urllib.error import URLError

username='hello'
password='world'
url='http://localhost:5000/'

# 构造HTTPPasswordMgrWithDefaultRealm对象
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,user=username,passwd=password,uri=url)

# 构造HTTPBasicAuthHandler对象
auth_Handler = HTTPBasicAuthHandler(p)

# 构造Opener
opener = build_opener(auth_Handler)

try:
    res = opener.open(url)
    content = res.read().decode('utf-8')
    print(content)
except URLError as e:
    print(e.reason)



