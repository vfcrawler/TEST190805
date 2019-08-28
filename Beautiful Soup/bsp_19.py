from bs4 import BeautifulSoup

html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jav</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li><li class="element"
>Bars</li>
</ul>
</div>
</div>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

# 查询属性id值为list-1的节点
print(soup.find_all(attrs={'id':'list-1'}))

# 查询属性name为elements的节点
print(soup.find_all(attrs={'name':'elements'}))

