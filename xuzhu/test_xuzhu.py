"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
from day2_practice.test_tonglao import TongLao

#，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”

class XuZhu(TongLao):
    def __init__(self,hp,epower):
        super(XuZhu, self).__init__(hp,epower)
        print("XuZhu继承童姥")

    def read(self):
        print("罪过罪过")

ins_xuzhu = XuZhu(1000,200)
ins_xuzhu.read()

ins_tonglao = TongLao(1000,200)
ins_tonglao.see_people("李秋水")
ins_tonglao.see_people("丁春秋")
ins_tonglao.fight_zms(2000,100)

