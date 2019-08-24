from urllib.parse import urljoin

# 新链接缺失scheme、netloc属性，基础链接提供scheme、netloc属性
print(urljoin('http://www.baidu.com',
              'FAQ.html'))

# 新链接无缺失
print(urljoin('http://www.baidu.com',
              'https://cuiqiangcai.com/FAQ.html'))

# 新链接无缺失
print(urljoin('http://www.baidu.com/about.html',
              'https://cuiqiangcai.com/FAQ.html'))

# 新链接无缺失
print(urljoin('http://www.baidu.com/about.html',
              'https://cuiqingcai.com/FAQ.html?question=2'))

# 新链接无缺失
print(urljoin('http://www.baidu.com?wd=abc',
              'https://cuiqingcai.com/index.php'))

# 新链接缺失scheme、netloc、path属性，基础链接提供scheme、netloc属性
print(urljoin('http://www.baidu.com',
              '?category=2#comment'))

# 新链接缺失scheme、netloc、path属性，基础链接提供netloc属性
print(urljoin('www.baidu.com',
              '?category=2#comment'))

# 新链接缺失scheme、netloc、path属性，基础链接提供netloc属性
print(urljoin('www.baidu.com#comment',
              '?category=2'))














