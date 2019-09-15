# -*-coding:utf-8-*-

import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

# 定义要登陆的地址
URL='https://passport.bilibili.com/login'

# 定义用户名
USERNAME = '18250151878'

# 定义密码
PASSWORD = 'wei8899'

# 定义左边框的距离
BORDER = 50

class CrackBiliGeetest():

    # 初始化
    def __init__(self):
        # 定义浏览器对象
        self.browser = webdriver.Chrome()
        # 定义显式等待对象
        self.wait = WebDriverWait(self.browser,15)
        self.location = None
        self.screenshot = None


    # '''
    # 打开要登录的地址
    # '''
    def open(self):
        self.browser.get(URL)
        # 最大化
        self.browser.maximize_window()

    # '''
    # 关闭浏览器
    # '''
    def close(self):
        self.browser.close()


    # '''
    # 输入账户
    # '''
    def submit_username(self):
        input_UserName = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    '#login-username'
                )
            )
        )
        input_UserName.send_keys(USERNAME)
        time.sleep(1)


    # '''
    # 输入密码
    # '''
    def submit_password(self):
        input_Password=self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    '#login-passwd'
                )
            )
        )
        input_Password.send_keys(PASSWORD)
        time.sleep(1)


    # '''
    # 点击登录按钮,即出现验证码页面
    # '''
    def click_login_button(self):
        btnLogin = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '#geetest-wrap > ul > li.btn-box > a.btn.btn-login'
                )
            )
        )
        btnLogin.click()
        time.sleep(1)

    # 获取网页截图对象
    def get_screenshot(self):

        screenshot = self.browser.get_screenshot_as_png()
        print(type(screenshot))
        screenshot = Image.open(BytesIO(screenshot))

        return screenshot



    # 获取验证码图片的坐标
    def get_position(self):

        img = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute'
                )
            )
        )

        location = img.location
        size = img.size

        left = location['x']
        top = location['y']
        right = location['x']+size['width']
        bottom = location['y']+size['height']

        # self.location = (int(left),int(top),int(right),int(bottom))

        return (int(left),int(top),int(right),int(bottom))


    # 获取验证码图片
    def get_image(self,name):

        screenshot = self.get_screenshot()

        if self.location is None:
            self.location = self.get_position()

        cropImg = screenshot.crop(self.location)
        cropImg.save(name+'.png')
        time.sleep(2)
        return cropImg

    # 清空缺口样式
    def delete_img_style(self):
        jsscript = 'document.querySelectorAll("canvas")[3].style="display:block"'
        self.browser.execute_script(jsscript)
        time.sleep(2)

    # 获取滑块按钮
    def get_slider_button(self):

        btnSlider = self.wait.until(EC.element_to_be_clickable((
            By.CLASS_NAME,
            'geetest_slider_button'
        )))

        return btnSlider

    # 判断两张图片的像素是否相等
    def is_pixel_equal(self,img_1,img_2,x,y):
        '''

        :param img_1: 带缺口图片
        :param img_2: 不带缺口图片
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        '''

        pixel_1 = img_1.load()[x,y]
        pixel_2 = img_2.load()[x,y]

        # 阈值
        thresold = 60

        if (abs(pixel_1[0]-pixel_2[0])<thresold
                and abs(pixel_1[1]-pixel_2[1])<thresold
                and abs(pixel_1[2]-pixel_2[2])<thresold):
            return True
        else:
            return False

    # 获取滑动的偏移量
    def get_gap(self,img_1,img_2):
        '''
        :param img_1: 带缺口图片
        :param img_2: 不带缺口图片
        :return:
        '''
        distance=60

        width = img_2.size[0]
        height = img_2.size[1]

        for i in range(distance,width):
            for j in range(height):
                if not self.is_pixel_equal(img_1,img_2,i,j):
                    # print(i)
                    distance = i
        # print(img_2.size[0], img_2.size[1])
        print(distance)
        return distance

    # 获取移动轨迹
    def get_track(self,distance):

        track = [] #移动轨迹

        current = 0 #当前位移

        mid = distance * 3/5 #减速阈值(移动的轨迹是先加速后减速)
        print(mid)

        t = 0.8 #时间间隔

        v = 0 #初速度

        distance += 14 #滑超过一段距离

        a = 0

        while current < distance:
            if current < mid:
                a = 1 #加速度为正
            else:
                a = -0.5 #加速度为负

            v0 = v #初速度v0

            v = v0 + a*t #当前速度v

            # 滑动的距离
            move = v0 * t + (1/2) * a * t * t

            current += move

            track.append(round(move))

        print(track)

        return track


    # 模拟释放鼠标抖动
    def shake_mouse(self):
        ActionChains(self.browser).move_by_offset(xoffset=2,yoffset=0).perform()
        ActionChains(self.browser).move_by_offset(xoffset=-3, yoffset=0).perform()


    # 拖动鼠标至缺口处
    def move_to_gap(self,slider,tracks):
        back_tracks = [-1, -1, -2, -2, -3, -2, -2, -1, -1]
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:  # 正向
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.01)
        for x in back_tracks:  # 逆向
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        self.shake_mouse()
        time.sleep(0.01)
        ActionChains(self.browser).release().perform()


    def start(self):
        try:
            self.open() #打开B站
            self.submit_username() #输入用户名
            self.submit_password() #输入密码
            self.click_login_button() #点击登陆按钮,出现验证码图片

            #进入滑动验证码的循环,成功后退出循环
            while True:
                img_1 = self.get_image(name='img_1')            # 获取带缺口的图片
                self.delete_img_style()                         # 执行js代码，不带缺口的图片出现
                img_2 = self.get_image(name='img_2')            # 获取不带缺口的图片

                distance = self.get_gap(img_1,img_2) - BORDER    # 计算需要滑动的距离
                tracks = self.get_track(distance)                # 计算轨迹

                slider = self.get_slider_button()               # 捕获滑块按钮

                self.move_to_gap(slider,tracks)                 # 拖动滑块至缺口处

                slider_box = self.wait.until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '/html/body/div[3]/div[2]/div[6]/div/div[1]/div[2]'
                        )
                    )
                )

                if slider_box.get_attribute('class') == 'geetest_slider geetest_success':
                    print('已完成滑动验证码验证')
                    break
                else:
                    print('验证失败,刷新验证码重新验证')
                    btn_refresh = self.wait.until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '/html/body/div[3]/div[2]/div[6]/div/div[2]/div/a[2]'
                            )
                        )
                    )
                    btn_refresh.click()
                    time.sleep(1)
                    print('已刷新验证码,再次进行验证')
                    time.sleep(1)
        except Exception as e:
            print(e.message)

            # self.close()
            print('关闭浏览器,重新启动浏览器进行登录')
            time.sleep(5)
            self.start()
            print('已重新启动浏览器')


if __name__ == '__main__':

    # 实例化CrackBiliGeetest类
    crack = CrackBiliGeetest()
    crack.start()
