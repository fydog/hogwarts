from selenium.webdriver.common.by import By

from selenium_weixin_OP.Module.BasePage import BasePage


class UploadPage(BasePage):
    def upload(self):
        self.find(By.ID, "js_upload_file_input").send_keys("D:/名单.xlsx")
        