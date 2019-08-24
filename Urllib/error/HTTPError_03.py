import socket
import urllib.request
import urllib.error

try:
    res = urllib.request.urlopen('http://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    # 打印reason的数据类型
    print(type(e.reason))
    # 判断reason是否为socket.timeout对象
    if isinstance(e.reason,socket.timeout):
        print('Time Out')

