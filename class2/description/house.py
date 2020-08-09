# 描述楼房的墙纸，楼层，面积

class House:   

    def __init__(self, wallpaper, floor, area):
        self.wallpaper = wallpaper
        self.floor  = floor
        self.area = area

    def wallpaper_color(self):
        print(f"墙纸颜色{self.wallpaper}")

    def floor_f(self):
        print(f"楼层{self.floor}")

    def area_a(self):
        print(f"面积是{self.area}")

a = House("white",3,30)
a.wallpaper_color()
a.floor_f()
a.area_a()
