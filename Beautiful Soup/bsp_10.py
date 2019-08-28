from bs4 import BeautifulSoup
html = '''
<html><head><title> The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1" ><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

# 输出第1个p节点的所有子孙节点
print(soup.p.children)

# 输出第1个p节点的所有子孙节点的类型
print(type(soup.p.children))

# 遍历输出所有的列表元素
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
for i,e in enumerate(soup.p.children):
    print(i,e)


