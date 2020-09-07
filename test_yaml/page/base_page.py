import yaml
from appium.webdriver.webdriver import WebDriver
from typing import List

from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "image_cancel")]
    _error_cont = 0
    # 设置错误次数
    _error_max = 10
    # 错误次数最大值
    _params = {}
    def __init__(self, driver:WebDriver=None):
        # 指定driver类型
        self._driver = driver
        # 调用driver方法


    def find(self, by, locator=None):
        # 定义find ，弹窗黑名单
        # *by解元组
        # 三步表达式：by如果是tuple，用find_element(*by),否则用find_element(by, locator)
        # try.. except.. else 捕获异常
        try:
            Find_element =  self._driver.find_elements(*by) \
            if isinstance(by, tuple) \
            else \
            self._driver.find_element(by, locator)
            self._error_cont = 0
            return Find_element
        except Exception as e:
            self._error_cont+=1
            if self._error_cont >= self._error_max:
                # 如果错误次数大于等于最大错误值，抛异常
                raise e
            for black in self._black_list:
                black_elements = self._driver.find_elements(*black)
                if len(black_elements) > 0:
                    black_elements[0].click()
                    return self.find(by, locator)
                raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value , by, locator)
                raise e

    def steps(self, path):
        # 读yaml文件
        with open(path, encoding='utf-8') as f:
            steps : List[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step['by'], step['locator'])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                            # value命中yaml，替换value
                        self.send(content, step['by'], step['locator'])

