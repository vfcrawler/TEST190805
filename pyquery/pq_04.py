from pyquery import PyQuery as pq

# 指定本地文件名来完成PyQuery对象的初始化
# (自动补全不完整的HTML的节点)
doc = pq(filename='demo.html')

# 输出所有的li节点
print(doc('li'))

