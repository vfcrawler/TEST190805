from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 定义要检核的页面地址
URL='https://passport.bilibili.com/login'

class CrackBiliGeetest():

    def __init__(self):
        '''
        初始化
        '''
        # 定义浏览器对象
        self.browser = webdriver.Chrome()
        # 定义显式等待对象
        self.wait = WebDriverWait(self.browser,20)


    def open(self):
        self.browser.get(URL)
        self.browser.maximize_window()




if __name__ == '__main__':
    blblcrack = CrackBiliGeetest()
    blblcrack.open()


