from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage
from selenium_weixin_OP.Page.login_page import LoginPage


class RegisterPage(BasePage):

    def goto_login(self):
        self.find(By.ID, 'submit_btn').click()
        return LoginPage(self._driver)