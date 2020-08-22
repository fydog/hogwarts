from classselenium.base import Base

class TestBaidushitu(Base):

    def test_shitu(self):
        self.driver.get('https://graph.baidu.com/pcpage/index?tpl_from=pc')

        img_add = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[6]/div/div/div[3]/div/form/input')\
            .send_keys('D:\123.jpg')
        self.driver.execute_script('arguments[0].click();', img_add)