from pyquery import PyQuery as pq

html='''
<div id="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html">
<span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4 html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
# 完成PyQuery对象的初始化
# (自动补全不完整的HTML的节点)
doc = pq(html)

# 获取class为list的节点
items = doc('.list')

# 再获取它的祖先节点
parents = items.parents()

# 输出parents的类型
print(type(parents))

# 输出parents
print(parents)


