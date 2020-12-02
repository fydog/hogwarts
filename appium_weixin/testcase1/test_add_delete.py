from appium_weixin.base1 import Base
from appium_weixin.page.main_page import MainPage


class TestCase(Base):

    # def setup(self):
    #     from appium_weixin.steppage.mainpage import MainPage
    #     self.main = MainPage()

    def test_add(self):
        from appium_weixin.page.main_page import MainPage
        self.main = MainPage()
        result = self.main.go_to_contact_page().go_to_addpage().go_to_adding_page().adding_member().return_to_contact().get_member_list()
        assert '用户1' == result