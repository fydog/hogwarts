from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.base import BasePage
from appium_weixin_po.page.manualaddpage import ManualAddPage


class InviteMemberPage(BasePage):
    _manual_invite_element = (MobileBy.ID, 'hs_')
    def goto_manual_add_member(self):
        self.find_and_click(self._manual_invite_element)
        return ManualAddPage(self._driver)