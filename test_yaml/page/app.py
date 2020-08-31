from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from test_yaml.page.base_page import BasePage
from test_yaml.page.main import Main


class App(BasePage):
    def start(self):
        _package="com.xueqiu.android"
        _activity=".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["noReset"] = "true"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self._driver.implicitly_wait(8)
            self.action = TouchAction(self._driver)
        else:
            self._driver.start_activity(_package, _activity)

        return  self

    def main(self):
        return  Main(self._driver)
