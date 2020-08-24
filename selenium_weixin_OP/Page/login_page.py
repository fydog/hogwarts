from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage
from selenium_weixin_OP.Page.register_page import RegisterPage


class LoginPage(BasePage):

    _url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, "").click()
        return RegisterPage(self._driver)

    def goto_login(self):
        pass