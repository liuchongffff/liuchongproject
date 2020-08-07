"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""

class TongLao:
    #定义构造函数：hp代表血量，epower代表武力值
    def __init__(self,hp,epower):
        self.hp=hp
        self.epower=epower
        print(f"TongLao hp is {self.hp}, power is {epower}")

    #定义see_people方法，
    #参数：name
    #功能描述：根据name名称，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！
    def see_people(self,name):
        if name=="WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name== "丁春秋":
            print("叛徒")
        else:
            print("错误")
            raise Exception

    #定义方法fight_zms方法（天山折梅手），
    #参数：无
    #函数描述：调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    #        需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self, hp,power):
            self.hp = self.hp/2
            self.epower = self.epower*10
            tl_hp = self.hp - power
            enery_hp = hp - self.epower
            if tl_hp > enery_hp:
                print(f"童姥的血量：{tl_hp}, 敌人的血量：{enery_hp}")
                print("童姥获胜")
            elif tl_hp < enery_hp:
                print(f"童姥的血量：{tl_hp}, 敌人的血量：{enery_hp}")
                print("童姥失败")
            else:
                print(f"童姥的血量：{tl_hp}, 敌人的血量：{enery_hp}")
                print("打成平手")
