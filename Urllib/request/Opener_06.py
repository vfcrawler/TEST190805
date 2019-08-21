import urllib.request
import urllib.error
import http.cookiejar

# 定义要读取的cookies文件
filename = 'lwpcookies.txt'

# 定义LWPCookieJar对象，用于读取cookies文件
cookie_jar = http.cookiejar.LWPCookieJar()

# 调用load()方法来读取cookies文件
# ignore_discard是指即使cookies将被丢弃也将它保存下来
# ignore_expires是指如果cookies已经过期也将它保存并且文件已存在时将覆盖
cookie_jar.load(filename,ignore_discard=True,ignore_expires=True)

# 构造HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 构造Opener对象
opener = urllib.request.build_opener(handler)

try:
    res = opener.open('http://www.baidu.com')
    print(res.status)
    print(res.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)