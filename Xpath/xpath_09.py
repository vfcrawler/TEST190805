from lxml import etree

# 构造一个XPath可解析的对象
html = etree.parse('test.html',parser=etree.HTMLParser())

# 调用xpath(路径选择表达式)的方法,选中href属性为link4.html的a节点，
# 然后再获取其父节点，然后再获取其class属性
res = html.xpath('//a[@href="link4.html"]/parent::*/@class')

print(res)
