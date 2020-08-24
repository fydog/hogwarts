from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage
from selenium_weixin_OP.Page.add_member_page import AddmemberPage
from selenium_weixin_OP.Page.upload_page import UploadPage


class ContactPage(BasePage):

    def goto_addmember(self):
        self.find(By.XPATH, '//*[@id="js_contacts81"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        return AddmemberPage(self._driver)


    def goto_add_appartment(self):
        self.find(By.CLASS_NAME, ".member_colLeft_top_addBtn").click()
        self.find(By.CLASS_NAME, ".js_create_party").click()
        self.find(By.CLASS_NAME, ".qui_inputText ww_inputText").send_keys()
        # 选择部门  缺
        return ContactPage(self._driver)


    def goto_upload(self):
        self.find(By.CLASS_NAME,".ww_btn_PartDropdown_left").click()
        self.find(By.CLASS_NAME, ".qui_dropdownMenu_itemLink ww_dropdownMenu_itemLink js_import_member").click()
        return UploadPage(self._driver)