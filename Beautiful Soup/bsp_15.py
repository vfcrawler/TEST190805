from bs4 import BeautifulSoup
html='''
<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
 class="sister" id="link2">Lacie</a>
</p>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

print('Next Siblings:')
# 输出第一个a节点的下一个兄弟节点的类型
print(type(soup.a.next_sibling))
# 输出第一个a节点的下一个兄弟节点
print(soup.a.next_sibling)
# 输出第一个a节点的下一个兄弟节点的文本内容
print(soup.a.next_sibling.string)
print('Parent:')
# 输出第一个a节点的所有祖先节点
print(type(soup.a.parents))
# 输出第一个a节点的最近的祖先节点
print(list(soup.a.parents)[0])
# 获取第一个a节点的最近祖先节点的class属性
print(list(soup.a.parents)[0].attrs['class'])


