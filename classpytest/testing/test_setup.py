# 一个.py文件就是一个模块
# 通常用的最多，方法级别、类级别，因为测试用例写在类里面



class   TestC:

    def setup_class(self):
        print("开始")

    def teardown_class(self):
        print("结束")



    def test_a(self):
        print("123")

    def test_b(self):
        print("456")


class   TestD:

    def setup_class(self):
        print("开始1")

    def teardown_class(self):
        print("结束1")



    def test_c(self):
        print("789")

    def test_d(self):
        print("1113")