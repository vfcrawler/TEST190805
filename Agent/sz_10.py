from selenium import webdriver

service_arg = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=9743'
]

browser = webdriver.PhantomJS(service_args=service_arg)
browser.get('http://httpbin.org/get')

print(browser.page_source)

