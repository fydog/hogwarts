from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage
from selenium_weixin_OP.Page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.CSS_SELECTOR, '//*[@id="menu_contacts"]/span').click()
        return ContactPage(self._driver)