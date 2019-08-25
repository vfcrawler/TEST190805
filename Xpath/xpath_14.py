from lxml import etree

# 构造一个XPath可解析的对象
html = etree.parse('test.html',parser=etree.HTMLParser())

# 调用xpath(路径选择表达式)的方法,
# 获取所有li节点下所有a节点的href的属性
res = html.xpath('//li/a/@href')

print(res)

