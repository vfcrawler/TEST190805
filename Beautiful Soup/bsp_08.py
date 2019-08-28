from bs4 import BeautifulSoup

html = '''
<html><head><title> The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1" ><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML节点)
soup = BeautifulSoup(html,features='lxml')

# 获取head节点元素中的title节点元素的类型
print(type(soup.head.title))

# 获取head节点元素中的title节点元素
print(soup.head.title)

# 获取head节点元素中的title节点的文本内容
print(soup.head.title.string)
