import urllib.request
import urllib.error

try:
    res = urllib.request.urlopen('http://cuiqingcai.com/index1.htm')
#先捕获子类HTTPError
except urllib.error.HTTPError as e:
    print(e.code,e.reason,e.headers,sep='\n')
#再捕获父类URLError
except urllib.error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
