from bs4 import BeautifulSoup
html = '''
<html><head><title> The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1" >
<span>Elsie</span>
</a>
</p>
<p class="story">...</p>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

# 输出第一个a节点的父节点元素
print(soup.a.parent)


