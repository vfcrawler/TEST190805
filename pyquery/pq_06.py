from pyquery import PyQuery as pq

html='''
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
'''
# 完成PyQuery对象的初始化
# (自动补全不完整的HTML的节点)
doc = pq(html)
# 获取class为list的节点
items = doc('.list')
print(type(items))
print(items)

# 获取class为list的节点的li节点
item = items.find('li')
print(type(item))
print(item)


