from pyquery import PyQuery as pq

# 指定url参数完成PyQuery对象的初始化
doc = pq(url='https://www.cuiqingcai.com')

# 输出title节点
print(doc('title'))

