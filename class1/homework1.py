# 设计一个小游戏，一个多回合制游戏，每个角色都有hp 和power，
# hp代表血量，power代表攻击力，hp的初始值为1000，
# power的初始值为200。打斗多个回合
def game():
# 定义函数game
    my_hp = 1000
    # 设置我方血量1000点
    em_hp = 1000
    # 设置敌人血量1000点
    my_power = 200
    # 设置我方攻击力200点
    em_power = 199
    # 设置敌人攻击力199点
    
    while True:
        # while true循环
        my_hp = my_hp - em_power
        # 设置我方血量计算方法
        print(my_hp)
        # 每回合结束打印我方当前血量
        em_hp = em_hp - my_power
        # 设置敌人的血量计算方法
        print(em_hp)
        # 每回合结束打印敌人当前血量
        if my_hp <= 0:
            # if语句，当我的血量<=0时
            print("i lose")
            # 打印 i lose
            break
            # 终止循环
        elif em_hp <= 0:
             # if语句，当敌人血量<=0时
            print("i win")
            # 打印 i win
            break
            # 终止循环
game()
# 调用函数