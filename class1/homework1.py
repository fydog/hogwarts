def game():
    my_hp = 1000
    en_hp = 1000
    my_power = 200
    en_power = 199
    
    while True:
        my_hp = my_hp - en_power
        print(my_hp)
        en_hp = en_hp - my_power
        print(en_hp)
        if my_hp <= 0:
            print("i lose")
            break
        elif en_hp <= 0:
            print("i win")
            break
game()