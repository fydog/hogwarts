from selenium import webdriver


class Base:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def teardown_method(self, method):
        pass