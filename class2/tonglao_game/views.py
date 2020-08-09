class TongLao:
# 创建tonglao类


    def see_people(self, name):
    # 定义see_people方法
        if name == "WYZ":
        # 如果输入字符串WYZ
            print("师弟！")
            # 打印“师弟！”
        elif name == "LQS":
        # 如果输入字符串LQS
            print("呸！贱人！")
            # 打印“呸！贱人！”
        elif name == "DCQ":
        # 如果打印字符串DCQ
            print("叛徒！")
            # 打印“叛徒！”

    def fight_zms(self, hp, em_hp, hit, em_hit):
    # 定义fight_zms方法，设置参数名称
        hp = hp / 2
        # hp减半
        hit = hit * 2
        # 攻击力加倍
        hp = hp - em_hit
        # hp计算方法：原hp-敌人攻击力
        em_hp = em_hp - hit
        # 敌人血量计算方法: 原敌人-我方加倍的攻击力
        if hp > em_hp:
        # if语句,如果我方剩余血量大于敌人血量
            print("赢了")
            # 输出 “赢了”
        else:
        # 则
            print("我的我的输了")
            # 输出“输了”

class Xuzhu(TongLao):
# 创建Xuzhu类，继承Tonglao类

    def read(self):
    # 定义read方法
        print("罪过罪过")
        # 当调用read方法，输出“罪过罪过”
