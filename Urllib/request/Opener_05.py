import urllib.request
import http.cookiejar
import urllib.error

# 定义要生成的文件名
filename='lwpcookies.txt'

# 构造LWPCookieJar对象，用于生成文件
cookie_jar = http.cookiejar.LWPCookieJar(filename)

# 构造HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 构造Opener对象
opener = urllib.request.build_opener(handler)

try:
    res = opener.open('http://www.baidu.com')
    cookie_jar.save(ignore_discard=True,ignore_expires=True)
except urllib.error.URLError as e:
    print(e.reason)



