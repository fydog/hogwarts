from appium.webdriver.common.mobileby import MobileBy

from appium_weixin.base1 import Base
from appium_weixin.page.go_to_addpage import GoToAddPage


class ContactPage(Base):


    def go_to_addpage(self):

        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='添加成员']").click()

        return GoToAddPage()


    def get_member_list(self):
        name_list = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b5p']//android.view.ViewGroup").text
        list1 = []
        for name in name_list:
            list1.append(name.text)
        return list1