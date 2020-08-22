import shelve

from selenium import webdriver

from selenium_weixin.base import Base


class TestWeixin(Base):

    def test_weixin(self):
        db = shelve.open("mydb/loginweixin")
        cookies = db['cookie']
        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys('D:\名单.xlsx')
        assert '名单.xlsx' == self.driver.find_element_by_xpath('//*[@id="upload_file_name"]').text




