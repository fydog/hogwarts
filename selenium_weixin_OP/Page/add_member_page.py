from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage
from selenium_weixin_OP.Page.contact_page import ContactPage


class AddmemberPage(BasePage):

    def add_member(self,username,memberadd_acctid):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(memberadd_acctid)
        self.find(By.CLASS_NAME, ".qui_btn ww_btn js_btn_save").click()
        return ContactPage(self._driver)