import shelve
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, chrome
from selenium.webdriver.common.action_chains import ActionChains

class Base:

    def setup_class(self):
        # option = Options()
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)




    def teardown_class(self):
        # self.driver.quit()
        pass