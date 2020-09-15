from appium_weixin_po.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.page.editmemberpage import EditMemberPage


class SettingMemberPage(BasePage):
    _edit_detail_ele = (MobileBy.XPATH, "//*[@text='编辑成员']")
    def goto_edit_detail(self):
        self.find_and_click(self._edit_detail_ele)
        return EditMemberPage(self._driver)