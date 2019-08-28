from bs4 import BeautifulSoup
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list id="list-1">
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

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)