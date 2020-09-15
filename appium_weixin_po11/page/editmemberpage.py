from appium_weixin_po.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

class EditMemberPage(BasePage):
    _delete_button_text = '删除成员'
    _delete_comfirm_button_ele = (MobileBy.XPATH, "//*[@text='确定']")
    def delete_member(self):
        from appium_weixin_po.page.contactpage import ContactPage
        self.find_by_scroll_and_click(self._delete_button_text)
        self.find_and_click(self._delete_comfirm_button_ele)
        return ContactPage(self._driver)