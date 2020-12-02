from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin.base1 import Base
from appium_weixin.page.contact_page import ContactPage


class MainPage(Base):

    def go_to_contact_page(self):
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
        # 进入通讯录
        return ContactPage()