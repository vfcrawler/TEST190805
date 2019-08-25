from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="links.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)

# 获取第一个li节点的所有祖先节点
res1 = html.xpath('//li[1]/ancestor::*')

# 获取第一个li节点的所有祖先节点中的div节点
res2 = html.xpath('//li[1]//ancestor::div')

# 获取第一个li节点的所有属性值
res3 = html.xpath('//li[1]//attribute::*')

# 获取第一个li节点的所有a直接子节点,并且a节点的href属性为link1.html
res4 = html.xpath('//li[1]//child::a[@href="link1.html"]')

# 获取第一个li节点的所有span子孙节点
res5 = html.xpath('//li[1]//descendant::span')

# 获取第一个li节点结束标签的后续第二个节点
res6 = html.xpath('//li[1]/following::*[2]')

# 获取第一个li节点结束标签后续的同级节点
res7 = html.xpath('//li[1]/following-sibling::*')

print(res1,res2,res3,res4,res5,res6,res7,sep='\n')







