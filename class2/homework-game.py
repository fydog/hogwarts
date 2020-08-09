class TongLao:
    # hp = 0
    # hit = 0
    # em_hp = 0
    # em_hit = 0

    # def __init__(self, hp, em_hp, hit, em_hit):
    #     self.hp = hp
    #     self.em_hp = em_hp
    #     self.hit = hit
    #     self.em_hit= em_hit

    def see_people(self, name):
        # self.see_people() = name
        if name == "WYZ":
            print("师弟！")
        elif name == "LQS":
            print("呸！贱人！")
        elif name == "DCQ":
            print("叛徒！")

    # def fight(self, hp, em_hp, hit, em_hit):
    #     self.hp = self.hp - self.em_hit
    #     self.em_hp = self.em_hp - self.hit
    #     if self.hp > self.em_hp:
    #         print("i win")
    #     else:
    #         print("i lose")

    def fight_zms(self, hp, em_hp, hit, em_hit):
        hp = hp / 2
        hit = hit * 2
        hp = hp - em_hit
        em_hp = em_hp - hit
        if hp > em_hp:
            print("赢了")
        else:
            print("输了")

class Xuzhu(TongLao):

    def read(self):
        print("罪过罪过")

a = TongLao()
a.see_people("WYZ")
# a.fight(1000,1000,300,100)
a.fight_zms(1000,1000,300,100)

b = Xuzhu()
b.read()
            
