import pytest
import yaml


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
        print("结束")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])

    def test_add(self, a, b, expect):
        # cal = Calculator()
        result = round(self.cal.add(a, b), 2)
        assert expect == result
    # round()方法返回浮点数x的四舍五入值，round( x [, n]  )，x -- 数值表达式，n -- 数值表达式，表示从小数点位数。

    @pytest.mark.div
    @pytest.mark.parametrize('a, b, expect', get_datas()[2], ids=get_datas()[3])

    def test_div(self, a, b, expect):
        result = round(self.cal.div(a, b),2)
        assert expect == result

    @pytest.mark.dcount
    @pytest.mark.parametrize('a, expect', get_datas()[4], ids=get_datas()[5])

    def test_dcount(self,a ,expect):
        result = self.cal.dcount(a)
        assert expect == result
