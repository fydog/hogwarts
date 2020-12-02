from appium.webdriver.common.mobileby import MobileBy
from appium_weixin.base1 import Base
# from appium_weixin.steppage.contact_page import ContactPage


class AddingPage(Base):
    def adding_member(self):

        username = "用户1"
        gender = "男"
        phonenumber = "18100010001"
        self.driver.find_element(MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.tencent.wework:id/azh' and @text='必填']")\
            .send_keys(username)
        # 添加姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 添加性别
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bf_']/android.widget.RelativeLayout[1]").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bf_']/android.widget.RelativeLayout[2]").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenumber)
        # 填手机号
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='设置部门']").click()
        # 进入部门选择
        self.driver.find_element(MobileBy.XPATH, "//*[@text='测试']").click()
        # 选择部门
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/g_3']").click()
        # 确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from appium_weixin.page.contact_page import ContactPage
        return ContactPage()

