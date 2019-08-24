import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()

# 调用set_url()方法来设置robots.txt文件的链接
rp.set_url('http://www.jianshu.com/robots.txt')

# 调用read()方法来读取
rp.read()

# 判断是否允许抓取URL
print(rp.can_fetch('*','http://www.jianshu.com/'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))


