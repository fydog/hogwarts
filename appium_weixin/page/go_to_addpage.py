from appium.webdriver.common.mobileby import MobileBy

from appium_weixin.base1 import Base
from appium_weixin.page.add_page import AddingPage



class GoToAddPage(Base):


    def go_to_adding_page(self):

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 手动添加
        return AddingPage()

    def return_to_contact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hjo']").click()
        from appium_weixin.page.contact_page import ContactPage
        return ContactPage()
