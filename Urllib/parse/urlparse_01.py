import urllib.parse

ret = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')

print('返回数据类型:',type(ret),sep='\n')
print('返回结果：',ret,sep='\n')
