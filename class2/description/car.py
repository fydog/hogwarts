# 汽身重量1000kg，加50kg油，百公里耗油5kg，500公里后车重多少.
# 开了500公里，再次加了80kg油，求总重量
class Car:
    # car_weight = 1000
    # gas_weight = 50
    # km = 1000

    def __init__(self, car_weight, gas_weight, used_gas, km):
        self.car_weight = car_weight
        # 赋值
        self.gas_weight = gas_weight
        self.used_gas =used_gas
        self.km = km

    def total_weight(self):
        total_weight = self.car_weight + self.gas_weight - (self.km / 100)*self.used_gas
        print(f"最后重量{total_weight}kg") 
        total_weight = int(total_weight)
        # print(type(total_weight))
        return total_weight

class Add(Car):

    def __init__(self, car_weight, gas_weight, used_gas, km, add_km, add_gas):
        super().__init__(car_weight, gas_weight, used_gas, km)
        self.add_km = add_km
        self.add_gas = add_gas


    def final_weight(self):
        # print(type(self.add_gas))
        # print(type(self.add_km))
        # print(type(self.used_gas))
        # print(type(self.total_weight))
        final_weight = self.total_weight() + self.add_gas - (self.add_km / 100)*self.used_gas
        # final_weight = self.car_weight + self.gas_weight - (self.km / 100)*self.used_gas + self.add_gas - (self.add_km / 100)*self.used_gas
        print(f"最后重量{final_weight}kg")
       

a = Car(1000, 50, 5, 500)
# 实例化
a.total_weight()

b = Add(1000, 50, 5, 500, 500, 80)
b.final_weight()
