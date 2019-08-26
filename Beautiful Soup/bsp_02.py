from bs4 import BeautifulSoup

text = '''
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

# BeautifulSoup初始化可自动补全不完整的节点
# 例如 html节点 ...
soup = BeautifulSoup(text,features='lxml')

# 输出soup类型
print(type(soup))

# 输出soup
print(soup)

# 输出美化后的soup (即以标准的缩进格式输出)
print(soup.prettify())

# 输出title节点的文本
print(soup.title.string)









