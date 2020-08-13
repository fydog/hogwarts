import pytest
import yaml
import sys
sys.path.append('..')

from classpytest.demo.calculator import Calculator

# 读取测试数据
def get_datas():
    with open('../datas/cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['myids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['myids']
        dcountdatas= mydatas['dcount']['datas']
        dcountids = mydatas['dcount']['myids']
    return [adddatas, addids, divdatas, divids, dcountdatas, dcountids]

# 文件名： test_开头
# 类名： Test 开头
# 方法名： test_ 开头
class TestCal:

    def setup_class(self):
        self.cal = Calculator()
        print("开始")
    # 初始化

    def teardown_class(self):
        # cal = Calculator()
        print("结束")

    @pytest.mark.add
    # 添加标签，add。 命令：pytest test_cal.py -vs -m "add"
    # @pytest.mark.parametrize("a , b, expect", [
    #     (1,1,2),
    #     (1,2,3),
    #     (1,3,5)
    # ], ids=['int', 'xx', 'yyy'] ) # 参数化 , ids命名测试用例结果
    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])

    def test_add(self, a, b, expect):
        # cal = Calculator()
        result = self.cal.add(a, b)
        assert expect == result

    @pytest.mark.div
    # @pytest.mark.parametrize('a', [10, 20, 30])
    # @pytest.mark.parametrize('b', [1, 2, 3])
    # @pytest.mark.parametrize('expect', [10, 20, 30])
    # # 笛卡尔积
    @pytest.mark.parametrize('a, b, expect', get_datas()[2], ids=get_datas()[3])

    def test_div(self, a, b, expect):
        # cal = Calculator()
        result = self.cal.div(a, b)
        assert expect == result

    @pytest.mark.dcount
    @pytest.mark.parametrize('a, expect', get_datas()[4], ids=get_datas()[5])

    def test_dcount(self,a ,expect):
        result = self.cal.dcount(a)
        assert expect == result
