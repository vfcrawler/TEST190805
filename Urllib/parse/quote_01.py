import  urllib.parse

keyword='壁纸'

n_keyword = urllib.parse.quote(keyword)
print('URL编码格式：',n_keyword)

url = 'http://www.baidu.com/s?wd='+n_keyword

print(url)
