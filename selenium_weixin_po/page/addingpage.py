from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_weixin_po.page.base import BasePage


class AddingMemberPage(BasePage):

    def adding_member(self):
        _username = "张宁1"
        _memberid = 'zhangning1'
        _phonenumber = '18700000000'
        from selenium_weixin_po.page.contactpage import ContactPage
        self.find(By.XPATH, '//*[@id="username"]').send_keys(_username)
        self.find(By.LINK_TEXT,'成员唯一标识，设定以后不支持修改').send_keys(_memberid)
        self.find(By.LINK_TEXT,'成员通过验证该手机后可加入企业').send_keys(_phonenumber)
        self.find(By.XPATH,'//*[@id="js_contacts157"]/div/div[2]/div/div[4]/div/form/div[2]/div[5]/div/div[2]/label/input').click()
        self.find(By.XPATH,'//*[@id="js_contacts157"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        return ContactPage(self.driver)