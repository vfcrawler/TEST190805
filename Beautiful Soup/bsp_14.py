from bs4 import BeautifulSoup
html = '''
<html><head><title> The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1" >
<span>Elsie</span>
</a>Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

# 获取第一个a节点的后面的兄弟节点
print('后面的兄弟节点:',soup.a.next_sibling)
# 获取第一个a节点的前面的兄弟节点
print('前面的兄弟节点：',soup.a.previous_sibling)
# 获取第一个a节点的后面的所有兄弟节点
print('前面的所有兄弟节点:',list(enumerate(soup.a.next_siblings)))
# 获取第一个a节点的前面的所有兄弟节点
print('后面的所有兄弟节点:',list(enumerate(soup.a.previous_siblings)))


