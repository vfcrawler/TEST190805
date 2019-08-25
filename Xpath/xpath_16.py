from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)

res = html.xpath('//li[contains(@class,"li")]/a/text()')

print(res)

