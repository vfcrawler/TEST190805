from lxml import etree

# 构造一个XPath可解析的对象
html = etree.parse('test.html',parser=etree.HTMLParser())

# 调用xpath(路径选择表达式)的方法,class为item-0的li节点
res = html.xpath('//li[@class="item-0"]')

print(res)