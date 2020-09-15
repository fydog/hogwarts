from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.base import BasePage
from appium_weixin_po.page.contactpage import ContactPage


class MainPage(BasePage):

    _contact_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_contact(self):
        self.find_and_click(self._contact_element)
        return ContactPage(self._driver)

