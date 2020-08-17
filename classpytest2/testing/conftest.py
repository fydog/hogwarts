import os
from typing import List
import pytest
# import sys
import yaml
from classpytest2.calculator import Calculator

# sys.path.append('../..')

# id设置中文
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope='class')
def get_cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")


# 读取测试数据
def get_datas():
    # mydatapath = os.path.dirname(__file__) + '/datas/cal.yml'
    with open('../datas/cal.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addids = mydatas['add']['myids']
        divdatas = mydatas['div']['datas']
        divids = mydatas['div']['myids']
        dcountdatas= mydatas['dcount']['datas']
        dcountids = mydatas['dcount']['myids']
    return [adddatas, addids, divdatas, divids, dcountdatas, dcountids]

@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas(request):
    return request.param
