import re
import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url = 'https://www.zhihu.com/explore'
res = requests.get(url,headers=headers,verify=False)
pattern = re.compile('<a.*?ExploreSpecialCard-contentTitle.*?>(.*?)</a>',flags=re.S)

ret = re.findall(pattern,res.text)

print(type(ret))
for e in ret:
    print(e)

