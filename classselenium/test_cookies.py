# cookie临时储存shelve方法
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestClasscookies:

    def setup(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass

    def test_savecookies(self):
        self.driver.get('https://www.csdn.net/')
        savecookies = self.driver.get_cookies()
        print(savecookies)

        for cookie in savecookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        db = shelve.open('mydb/logincookies')
        cookies = db['cookie']
        db.close()

