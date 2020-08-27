# 作业
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction



class TestCase:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        # 隐式等待
        self.driver.implicitly_wait(5)
        self.action = TouchAction(self.driver)

    def test_add(self):
        username = "用户1"
        gender = "男"
        phonenumber = "18100010001"
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='添加成员']").click()
        # 添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 手动添加
        self.driver.find_element(MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.tencent.wework:id/azh' and @text='必填']").send_keys(username)
        # 添加姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 添加性别
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bf_']/android.widget.RelativeLayout[1]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bf_']/android.widget.RelativeLayout[2]").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenumber)
        # 填手机号
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='设置部门']").click()
        # 进入部门选择
        self.driver.find_element(MobileBy.XPATH, "//*[@text='测试']").click()
        # 选择部门
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/g_3']").click()
        # 确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext

    def test_delete(self):
        username = "用户1"
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='用户1']").click()
        # 点击用户1
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hjz']").click()
        # 进入个人信息
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()

        window_rect = self.driver.get_window_rect()
        print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 7)
        # 滑动2次，1次没反应
        for i in range(2):
            self.action.press(x=x1, y=y_start).wait(1000).move_to(x=x1, y=y_end).release().perform()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bfe']").click()
        # 删除成员
        result = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b5p']//android.view.ViewGroup").text
        assert result != username
        # 断言：列表里没username

    def teardown(self):
        pass









