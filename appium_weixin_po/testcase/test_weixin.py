import pytest
import yaml
from appium_weixin_po.page.app import App


def get_member_datas():
    with open('../member_add.yaml', 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas

def get_delete_datas():
    with open('../member_delete.yaml', 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas



class TestWeixin:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()


    @pytest.mark.parametrize(
        'membername,membergender,memberphonenumber',get_member_datas()
    )
    def test_add_member(self,membername, membergender, memberphonenumber):
        result = self.main.goto_contact().goto_invite().goto_manual_add_member().\
            add_member_name(membername).add_member_gender(membergender).\
            add_member_phone(memberphonenumber).choose_apartment().\
            save().get_toasttext()
        assert result == '添加成功'

    @pytest.mark.parametrize(
        '_member_name_text',get_delete_datas()
    )
    def test_delete_member(self,_member_name_text):
        result = self.main.goto_contact().find_member(_member_name_text).goto_setting_member().\
            goto_edit_detail().delete_member().get_member_list()
        print(result)
        print(_member_name_text)
        assert _member_name_text not in result