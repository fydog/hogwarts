from classselenium.base import Base


class TestTanchuang(Base):


    def test_tanchuang(self):

        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()


    def test_xialaicaidan(self):
        # 隐藏按钮
        self.driver.get('http://www.baidu.com')
        setting_position = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        self.action.move_to_element(setting_position).perform()
        self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()