import urllib.robotparser
import urllib.request

rp = urllib.robotparser.RobotFileParser()

# 读取robots.txt文件的内容
req = urllib.request.urlopen('http://www.jianshu.com/robots.txt')
robots = req.read().decode('utf-8').split('\n')

# 调用parse()方法来读取和分析
rp.parse(robots)

# 判断是否允许抓取URL
print(rp.can_fetch('*','http://www.jianshu.com/'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))


