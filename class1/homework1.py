def game():
    my_hp = 1000
    em_hp = 1000
    my_power = 200
    em_power = 199
    
    while True:
        my_hp = my_hp - em_power
        print(my_hp)
        em_hp = em_hp - my_power
        print(em_hp)
        if my_hp <= 0:
            print("i lose")
            break
        elif em_hp <= 0:
            print("i win")
            break
game()