from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'test@test.com'
PASSWORD = '123456'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        '''
        获取初始验证按钮
        :return: 按钮对象
        '''
        button = self.wait.until(
            EC.element_to_be_clickable(
                By.CLASS_NAME,
                'geetest_radar_tip')
        )
        return button


    # # 点击验证按钮
    # button = get_geetest_button()
    # button.click()

    def get_screenshot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))

        return screenshot

if __name__ == '__main__':
    a = CrackGeetest()
    ret = a.get_screenshot()
    print(type(ret))
    ret.show()


