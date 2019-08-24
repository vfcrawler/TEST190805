import urllib.parse

# 定义字典类型的参数
params = {
    'name':'world'
}

# 基础链接
base_url = 'http://www.baidu.com'

# 将字典类型的参数序列化成GET请求的参数
new_params = urllib.parse.urlencode(params)
print('序列化后的GET参数：',new_params)

# 拼接URL
url = urllib.parse.urljoin(base_url,new_params)
print('拼接后的URL：',url)

