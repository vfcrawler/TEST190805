import http.cookiejar
import urllib.request
import urllib.error

# 定义要生成的文件名
filename = 'cookies.txt'

# 构造MozillaCookieJar对象，用于生成文件
cookie_jar = http.cookiejar.MozillaCookieJar(filename)

# 构造HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 构造Opener对象
opener = urllib.request.build_opener(handler)

try:
    res = opener.open('http://www.baidu.com')
    # save方法需要传递两个参数
    # ignore_discard是指即使cookies将被丢弃也将它保存下来
    # ignore_expires是指如果cookies已经过期也将它保存并且文件已存在时将覆盖
    cookie_jar.save(ignore_discard=True,ignore_expires=True)
except urllib.error.URLError as e:
    print(e.reason)

