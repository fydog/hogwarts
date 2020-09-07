#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
App 类：
app 常用的方法：比如 启动应用，关闭应用，重启应用，进入首页
"""
from appium import webdriver

from appium_weixin_po.base import BasePage
from appium_weixin_po.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        """
        启动应用
        如果driver已经被实例化，就复用已有的driver
        如果driver=None ，就要重新创建一个driver
        """
        if self._driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self._driver.implicitly_wait(5)
        else:
            # 启动 caps 里面设置的appPackage appActivity
            self._driver.launch_app()
            # 启动 任何一个包和activity
            # self.driver.start_activity()
        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()

    def stop(self):
        self._driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self._driver)