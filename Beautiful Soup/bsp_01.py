from bs4 import BeautifulSoup

# 完成BeautifulSoup对象初始化
soup = BeautifulSoup('<p>Hello</p>', features='lxml')

print(soup.p.string)

