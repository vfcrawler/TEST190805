from urllib.request import ProxyHandler,build_opener
from urllib.request import URLError

# 构造ProxyHandler对象
proxy_Handler = ProxyHandler(
    {
        'http':'http://127.0.0.1:9743',
        'https':'https://127.0.0.1:9743'
    }
)

# 构造Opener对象
opener = build_opener(proxy_Handler)

try:
    res = opener.open('http://www.baidu.com')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

