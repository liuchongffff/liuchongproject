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

    #对打多轮
    while True:
        my_hp = mhp - epower
        energy_hp = ehp - mpower
        if my_hp <=0:
            print(f"i lose the game. myhp:{my_hp} enemy_hp:{energy_hp}")
            break
        elif energy_hp <= 0:
            print(f"the enemy lose the game. myhp:{my_hp} enemy_hp:{energy_hp}")
            break
#调用
fight()
