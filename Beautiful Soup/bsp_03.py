from bs4 import BeautifulSoup

html = '''
<html><head><title> The Dormouse's story</title>/head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b>
</p>
<p class="story">Once upon a time there 
were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" 
id="link1" ><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" 
id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" 
id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 初始化BeautifulSoup对象
soup = BeautifulSoup(html,'lxml')

# 输出title节点
print(soup.title)

# 输出title节点类型
print(type(soup.title))

# 输出title节点的文本
print(soup.title.string)

# 输出head节点
print(soup.head)

# 输出文档中第一个p节点
print(soup.p)




