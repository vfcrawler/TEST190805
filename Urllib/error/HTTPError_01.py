# -*-coding:utf-8-*-
import urllib.request
import urllib.error

try:
    res = urllib.request.urlopen('http://cuiqingcai.com/index1.htm')
except urllib.error.HTTPError as e:
    # 以换行符打印 sep='\n'
    print(e.code,e.reason,e.headers)

