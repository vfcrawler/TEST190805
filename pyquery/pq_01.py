# 引入PyQuery对象，并且使用别名pq
from pyquery import PyQuery as pq

html='''
<div>
<ul
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4 html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

# 初始化PyQuery对象(自动补全不完整的HTML的节点)
doc = pq(html)
# 输出的类型
print(type(doc('li')))
# 输出所有的li节点
print(doc('li'))

