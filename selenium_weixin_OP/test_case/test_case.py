from selenium_weixin_OP.Module.BasePage import BasePage
import pytest

from selenium_weixin_OP.Page.main_page import MainPage


class TestCase(BasePage):

    def setup(self):
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.main = MainPage()

    def teardown(self):
        pass

    def test_addmember(self):
        # add_member = self.main.goto_contact().goto_addmember("李阳","liyang")
        self.main.goto_contact().goto_addmember("李阳", "liyang")



