"""
打斗多个回合，谁最后血量最多
"""
def fight():
    my_hp = 0
    energy_hp = 0
    mhp = 1000
    mpower = 100
    ehp = 1000
    epower = 100
    print(f"the game begin. ")
    my_hp = mhp - epower
    energy_hp = ehp - mpower

    while True:
        if my_hp <=0:
            print(f"i lose the game. ")
            break
        elif energy_hp <= 0:
            print(f"the enemy lose the game. ")
            break
        my_hp = my_hp - epower
        energy_hp = energy_hp - mpower

#调用
fight()
