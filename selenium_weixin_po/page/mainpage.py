from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_weixin_po.page.base import BasePage
from selenium_weixin_po.page.contactpage import ContactPage


class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_contact(self):

        self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)