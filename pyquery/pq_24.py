from pyquery import PyQuery as pq

html='''
<ul class="list">
<li class="item-0 active"><a href="link3.html">
<span class="bold">third item</span></a></li>
</ul>
'''
# 完成PyQuery对象的初始化
# (自动补全不完整的HTML的节点)
doc = pq(html)

li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)