from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="links.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)

# 获取满足条件的第1个li节点
res1 = html.xpath('//li[1]//a/text()')

# 获取满足条件的最后1个节点
res2 = html.xpath('//li[last()]/a/text()')

# 获取满足条件的索引位置<3的节点（即第1个li和第2个li节点）
res3 = html.xpath('//li[position()<3]/a/text()')

# 获取满足条件的倒数第3个的节点(即last()-2 也可以是 最后一个节点前移2个节点)
res4 = html.xpath('//li[last()-2]/a/text()')

print(res1,res2,res3,res4,sep='\n')




