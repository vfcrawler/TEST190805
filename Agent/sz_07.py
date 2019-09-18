import socks
import socket
import requests


socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9742)
socket.socket = socks.socksocket

try:
    res = requests.get('http://httpbin.org/get')
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('Error:',e.args)



