import pytest
import sys
sys.path.append('../..')
# 文件名： test_开头
# 类名： Test 开头
# 方法名： test_ 开头


class TestCal:

    @pytest.mark.add
    def test_add(self, get_datas, get_cal):
        result = round(get_cal.add(get_datas[0],get_datas[1]), 2)
        assert get_datas[2] == result
    # round()方法返回浮点数x的四舍五入值，round( x [, n]  )，x -- 数值表达式，n -- 数值表达式，表示从小数点位数。

    # @pytest.mark.div
    # # @pytest.mark.parametrize('a, b, expect', get_datas()[2], ids=get_datas()[3])
    # def test_div(self, get_datas, get_cal):
    #     result = round(get_cal.div(get_datas[0],get_datas[1], 2)
    #     assert get_datas[2] == result
    #
    # @pytest.mark.dcount
    # # @pytest.mark.parametrize('a, expect', get_datas()[4], ids=get_datas()[5])
    # def test_dcount(self,get_datas, get_cal):
    #     result = get_cal.dcount(get_datas[0],get_datas[1])
    #     assert get_datas[2] == result
