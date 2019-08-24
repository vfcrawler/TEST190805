import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
res = requests.get('https://www.jianshu.com',headers=headers,verify=False)

# 获取状态码 status_code
print(type(res.status_code),res.status_code)
# 获取响应头 headers
print(type(res.headers),res.headers)
# 获取Cookies
print(type(res.cookies),res.cookies)
# 获取URL
print(type(res.url),res.url)
# 获取请求历史 history
print(type(res.history),res.history)



