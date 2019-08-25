from lxml import etree

# 声明一段残缺的HTML文本
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

# 调用HTML类进行初始化，构造一个XPath可解析的对象
html = etree.HTML(text)

# 输出修正后的HTML文本，但是结果是bytes类型
res = etree.tostring(html)

print(type(res))
print(res)

# 将decode()方法将其转化为str类型
res1 = res.decode('utf-8')

print(type(res1))
print(res1)





