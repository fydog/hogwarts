from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_weixin_po.page.addingpage import AddingMemberPage
from selenium_weixin_po.page.base import BasePage


class ContactPage(BasePage):


    def go_to_add(self):
        self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[1]').click()
        return AddingMemberPage(self.driver)


    def get_member_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list1 = []
        for name in name_list:
            list1.append(name.text)
        return list1