from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.base import BasePage
from appium_weixin_po.page.settingmemberpage import SettingMemberPage


class MemberDetailPage(BasePage):
    _setting_member_ele = (MobileBy.ID, 'hjz')
    def goto_setting_member(self):
        self.find_and_click(self._setting_member_ele)
        return SettingMemberPage(self._driver)