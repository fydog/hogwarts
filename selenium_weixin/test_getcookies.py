from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome --remote-debugging-port=9222
# 复用浏览器，cmd 开启
# http://localhost:9222/

class TestGetCookie:
    def setup_class(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown_class(self):
        pass

    def test_getcookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')


