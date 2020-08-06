"""
打斗多个回合，谁最后血量最多
"""
def fight():
    mhp = 1000
    mpower = 120
    ehp = 1000
    epower = 100
    print(f"the game begin. ")

    while True:
        mhp = mhp - epower
        ehp = ehp - mpower
        if mhp <=0:
            print(f"i lose the game. ")
            break
        elif ehp <= 0:
            print(f"the enemy lose the game. ")
            break

#调用
fight()
