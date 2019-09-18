from selenium import webdriver

service_args=[
    '--proxy=127.0.0.1',
    '--proxy-type=9743',
    '--proxy-auth=username:password'
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')

print(browser.page_source)


