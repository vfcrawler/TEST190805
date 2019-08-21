import http.cookiejar
import urllib.request
import urllib.error

# 首先必须构造一个CookieJar对象
cookie_jar = http.cookiejar.CookieJar()

# 构造HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 构造Opener对象
opener = urllib.request.build_opener(handler)

try:
    res = opener.open('http://www.baidu.com')
    for item in cookie_jar:
        print(item.name+'='+item.value)
except urllib.error.URLError as e:
    print(e.reason)






