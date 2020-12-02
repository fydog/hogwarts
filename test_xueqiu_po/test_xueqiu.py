import pytest

from test_xueqiu_po.demo_page import DemoPage
from test_xueqiu_po.utils import Utils


class TestXueqiu:

    data = Utils.from_file('test_search.yml')
    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start()

    def setup(self):
        pass

    def teardown(self):
        self.demo.back()

    def teardown_class(self):
        self.demo.stop()


    # 测试数据的数据驱动
    @pytest.mark.parametrize('username,password',[
        ("user1","word1"),
        ("user1", "word2")
    ])
    def test_login(self, username, password):
        # 测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1==1

    # @pytest.mark.parametrize('keyword',[
    #      'alibaba',
    #      # 'jingdong',
    #      # 'baiduo'
    # ]
    # )
    @pytest.mark.parametrize(
        data['keys'], data['values']
    )
    def test_search(self, keyword):
        print(keyword)
        self.demo.search(keyword)




