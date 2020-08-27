#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client 里面提供的api


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)
        self.action = TouchAction(self.driver)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_xueqiu_press(self):

        window_rect = self.driver.get_window_rect()
        print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        self.action.press(x = x1, y = y_start).wait(1000).move_to(x = x1,y = y_end).release().perform()
