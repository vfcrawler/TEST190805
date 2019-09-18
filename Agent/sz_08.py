from selenium import webdriver


proxy = '172.16.1.117:8080'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--proxy-sever=http://'+proxy)

browser = webdriver.Chrome(chrome_options=chrome_option)
browser.get('http://httpbin.org/get')


