import urllib.parse

# 待解析的URL中没有附加协议
# 指定默认的协议schema='https'
res = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment',
                            scheme='https')
print(res)


