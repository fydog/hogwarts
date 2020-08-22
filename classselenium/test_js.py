from classselenium.base import Base


class TestJs(Base):

    def test_js(self):
        self.driver.get("https://www.baidu.com/s?ie=UTF-8&wd=selenium%20js")
        # self.driver.find_element_by_id("kw").send_keys("ceshi")
        element = self.driver.execute_script("document.documentElement.scrollTop=1000")
