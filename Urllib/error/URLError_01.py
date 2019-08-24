import urllib.request
import urllib.error

try:
    res = urllib.request.urlopen('http://dedecc123.com/index.htm')
except urllib.error.URLError as e:
    print(e.reason)

