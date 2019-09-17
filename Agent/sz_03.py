import socks
import socket
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9743)
socket.socket = socks.socksocket

try:
    res = request.urlopen('http://httpbin.org/get')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)



