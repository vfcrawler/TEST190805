import re
from bs4 import BeautifulSoup

html='''
<div class="panel">
<div class="panel-body">
<a>Hello,this is a link></a>
<a>Hello,this is a link,too</a>
</div>
</div>
'''
# 初始化BeautifulSoup对象(自动补全不完整的HTML的节点)
soup = BeautifulSoup(html,features='lxml')

# 返回所有节点文本匹配link的节点
print(soup.find_all(text=re.compile('link')))
