from pyquery import PyQuery as pq

html='''
<div class='wrap'>
    Hello,World
    <p>This is a paragraph.</p>
</div>
'''
# 完成PyQuery对象的初始化
# (自动补全不完整的HTML的节点)
doc = pq(html)

wrap = doc('.wrap')
print(wrap)
wrap.find('p').remove()
print(wrap)
print(wrap.text())
