from pyquery import PyQuery as pq

html='''
<div class="wrap">
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

# 获取所有的li的节点,再调用items()方法
lis = doc('li').items()

# 打印lis类型
print(type(lis))

# 遍历输出lis中的每个元素及其类型
for li in lis:
    print(li,type(li))
