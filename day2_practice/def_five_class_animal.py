"""
定义五种动物类：
猫
狗
猪
鸡
鸟
"""

#定义class cat
class Animal_Cat:
    #定义cat类的实体构造函数，描绘其身高，长度，重量，颜色
    def __init__(self, height,len,weight,color ):
        self.heght = height
        self.len = len
        self.weight = weight
        self.color = color

    # 定义cat类的eat行为，告诉cat喜欢吃鱼
    def eat(self):
        print("猫吃鱼")
    ##定义cat类的play行为，告诉cat喜欢爬树
    def play(self):
        print("猫喜欢爬树")
    ##定义cat类所属的种类，打印cat属于哺乳动物
    def belong_animal(self):
        print("猫是哺乳动物")

#定义class Dog，描述身高，体重，长度，颜色以及eat，play，belong_aninmal等方法的行为
class Animal_Dog:
    #定义Dog类的实体构造函数，描绘其身高，长度，重量，颜色
    def __init__(self, height,len,weight,color ):
        self.heght = height
        self.len = len
        self.weight = weight
        self.color = color

    # 定义Dog类的eat行为，告诉Dog喜欢吃肉
    def eat(self):
        print("狗吃骨头")
    # 定义Dog类的play行为，告诉Dog喜欢看家护院
    def play(self):
        print("狗喜欢看家护院")
    # 定义Dog类的belong_animal行为，告诉Dog属于哺乳动物
    def belong_animal(self):
        print("狗是哺乳动物")

#定义class Pig
class Animal_Pig:
    #定义Pig类的实体构造函数，描绘其身高，长度，重量，颜色
    def __init__(self, height,len,weight,color ):
        self.heght = height
        self.len = len
        self.weight = weight
        self.color = color

    # 定义Pig类的eat行为，告诉cat喜欢吃杂事
    def eat(self):
        print("猫吃鱼")

    ##定义Pig类的play行为，告诉Pig喜欢爬树
    def play(self):
        print("猪喜欢睡觉")
    ##定义Pig类所属的种类，打印Pig属于哺乳动物
    def belong_animal(self):
        print("猪是哺乳动物")



#定义class Chicken
class Animal_Chicken:
    #定义Chicken类的实体构造函数，描绘其身高，长度，重量，颜色
    def __init__(self, height,len,weight,color ):
        self.heght = height
        self.len = len
        self.weight = weight
        self.color = color

    # 定义Chicken类的eat行为，告诉Chicken喜欢吃小米
    def eat(self):
        print("鸡吃小米")
    ##定义Chicken类的play行为，告诉Chicken喜欢下蛋
    def play(self):
        print("鸡喜欢下蛋")
    ##定义Chicken类所属的种类，打印Chicken属于禽类
    def belong_animal(self):
        print("鸡是禽类")



#定义class Bird
class Animal_Bird:
    #定义Bird类的实体构造函数，描绘其身高，长度，重量，颜色
    def __init__(self, height,len,weight,color ):
        self.heght = height
        self.len = len
        self.weight = weight
        self.color = color

    # 定义Bird类的eat行为，告诉Bird喜欢吃虫子
    def eat(self):
        print("小鸟吃虫子")
    ##定义Bird类的play行为，告诉Bird喜欢飞翔
    def play(self):
        print("小鸟喜欢飞翔")
    ##定义Chicken类所属的种类，打印Bird属于飞禽类
    def belong_animal(self):
        print("Bird是飞禽类")

#定义一个chicken类实体变量
chicken=Animal_Chicken(20,15,5,"blue")
chicken.play()

#定义一个Animal_Bird类实体变量
bird=Animal_Bird(5,7,1,"red")
bird.play()

#定义一个Animal_Pig类实体变量
pig=Animal_Pig(50,100,150,"black")
pig.play()

#定义一个dog=Animal_Dog类实体变量
dog=Animal_Dog(50,70,30,"black")
dog.play()

#定义一个dog=Animal_Cat类实体变量
cat=Animal_Cat(15,25,6,"black")
cat.play()
