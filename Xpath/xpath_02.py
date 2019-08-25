from lxml import etree

# 构造一个XPath可解析的对象
html = etree.parse('test.html',etree.HTMLParser())

# 输出修正后的HTML文本，但是结果是bytes类型
res = etree.tostring(html)

# 将其转化为str类型
ret = res.decode('utf-8')

print(ret)

