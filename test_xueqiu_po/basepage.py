import logging

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    _driver : WebDriver = None
    _current_element: WebElement = None
    def start(self):
        caps = {
            'platformName' : 'android',
            'deviceName' : 'hogwarts',
            'appPackage' : 'com.xueqiu.android',
            'appActivity' : '.view.WelcomeActivityAlias',
            'noReset' : True
        }
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(15)
        return  self

    def stop(self):
        self._driver.quit()

    def find(self,by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    # 读取po的每一步，po_method po方法的名字
    def po_run(self, po_method , **kwargs):
        # read yaml
        with open('page.yml') as f:
            yaml_data = yaml.safe_load(f)
        # find search
            for step in yaml_data[po_method]:
        # find by click send_keys
                if isinstance(step, dict):
                    # 如果step是个词典， key代表id  sendkeys click
                    for key in step.keys():
                        if key=='id':
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key=='send_keys':
                            text = str(step[key])
                            for k,v in kwargs.items():
                                text = text.replace('${' + k + '}', v)
                            self.send_keys(text)
                            # 替换yaml的send_keys内容
                        else:
                            logging.error(f'dont know{step}')


