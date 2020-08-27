from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Base:

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


    def setup(self):
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

