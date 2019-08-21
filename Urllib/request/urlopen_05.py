import socket
import urllib.request
import urllib.error

try:
    # 设置超时时间为0.1秒
    res = urllib.request.urlopen('https://www.python.org', timeout=0.1)
    print(res.read().decode('utf-8'))
except urllib.error.URLError as e:
    # 返回出错异常原因的数据类型
    print(type(e.reason))
    # 返回出错异常原因
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print('超时')


