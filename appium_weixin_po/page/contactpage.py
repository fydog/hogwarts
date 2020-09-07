from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.base import BasePage
from appium_weixin_po.page.invitepage import InviteMemberPage
from appium_weixin_po.page.memberdetail import MemberDetailPage


class ContactPage(BasePage):
    _invite_text = '添加成员'
    _get_member_list_ele = (MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/b5p']//android.widget.TextView")

    def goto_invite(self):
        self.find_by_scroll_and_click(self._invite_text)
        return InviteMemberPage(self._driver)


    def find_member(self,_member_name_text):
        self.find_by_scroll_and_click(_member_name_text)
        return MemberDetailPage(self._driver)

    def get_member_list(self):
        name_list = self.finds(self._get_member_list_ele)
        list0 = []
        for name in name_list:
            list0.append(name.text)
        return list0