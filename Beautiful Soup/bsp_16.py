from bs4 import BeautifulSoup
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list id="list-1">
<li class="element">Foo/li>
<li class="element">Bar</li>
<li class="element">Jav</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bars</li>
</ul>
</div>
</div>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')
# 查询name为ul的节点元素
print(soup.find_all(name='ul'))
# 输出查询name为ul的第1个节点元素的数据类型
print(type(soup.find_all(name='ul')[0]))
