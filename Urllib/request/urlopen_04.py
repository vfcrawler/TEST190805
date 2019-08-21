import urllib.request

# 设置超时时间为1秒
res = urllib.request.urlopen('https://www.python.org',timeout=0.1)

print(res.read().decode('utf-8'))

