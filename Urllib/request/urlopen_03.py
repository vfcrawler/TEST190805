import urllib.request
import urllib.parse

dicts = {'hello':'world'}

# 将字典类型的参数 转化为 字符串类型的参数
str_dicts = urllib.parse.urlencode(dicts)
# 返回字符串类型
print(type(str_dicts))
print(str_dicts)

# 将字符串类型转化为字节流类型，需要指定编码格式 encoding='utf-8'
data = bytes(str_dicts,encoding='utf-8')
# 返回字节流类型
print(type(data))
print(data)

res = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(res.read().decode('utf-8'))



