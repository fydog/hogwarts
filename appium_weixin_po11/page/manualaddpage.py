from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.base import BasePage


class ManualAddPage(BasePage):
    _member_name_ele = (MobileBy.ID, 'b2i')
    _member_gender_ele = (MobileBy.XPATH, "//*[@text='男']")
    _member_male_ele = (MobileBy.XPATH, "//*[@text='男']")
    _member_female_ele = (MobileBy.XPATH, "//*[@text='女']")
    _member_phonenumber_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    _choose_apartment_ele = (MobileBy.XPATH, "//android.widget.TextView[@text='设置部门']")
    _member_apartment_ele = (MobileBy.XPATH, "//*[@text='测试']")
    _confrim_ele = (MobileBy.ID,'gir')
    _auto_invite_text = '保存后自动发送邀请通知'
    _save_button_ele = (MobileBy.XPATH, "//*[@text='保存']")

    def add_member_name(self,membername):
        self.find_and_sendkeys(self._member_name_ele, membername)
        return self

    def add_member_gender(self,membergender):
        self.find_and_click(self._member_gender_ele)
        if membergender=='男':
            self.find_and_click(self._member_male_ele)
        else:
            self.find_and_click(self._member_female_ele)
        return self

    def add_member_phone(self, memberphonenumber):
        self.find_and_sendkeys(self._member_phonenumber_ele, memberphonenumber)
        return self

    def choose_apartment(self):
        self.find_and_click(self._choose_apartment_ele)
        self.find_and_click(self._member_apartment_ele)
        self.find_and_click(self._confrim_ele)
        return self


    def save(self):
        from appium_weixin_po.page.contactpage import ContactPage
        self.find_by_scroll_and_click(self._auto_invite_text)
        self.find_and_click(self._save_button_ele)
        return ContactPage(self._driver)
