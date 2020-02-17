#人狗大战
class Dog:
    def __init__(self,name,type,aggr):
        self.name = name        # 名字
        self.dog_type = type    # 类型
        self.aggr = aggr        # 攻击力
        self.life_value = 2000  # 生命值

    def bite(self,person_obj):  # self==egg,person_obj=alex
        # 咬这个动作伴随着属性的变化，掉血。狗咬人人掉血。
        print('%s咬了%s'%(self.name,person_obj.name))
        person_obj.life_value -= self.aggr # 人掉的血就是狗的攻击力，修改了另一个类实例化对象的属性值。

class Person:
    rol = '人'         #数据属性、静态属性、类属性
    country = '中国'
    def __init__(self,name,age,life_value): #初始化方法
        self.name = name       #属性、对象属性
        self.theage = age
        self.life_value = life_value
        self.aggr = 1

    def attack(self,dog_obj):  #函数属性、动态属性、方法
        print('%s攻击了%s'%(self.name,dog_obj.name))
        dog_obj.life_value -= self.aggr

alex = Person('alex',38,500)
egg = Dog('egon','二哈',20)
print(alex.life_value)
egg.bite(alex)   # Dog.bite(egg,alex)
print(alex.life_value)

print(egg.life_value)
alex.attack(egg)
print(egg.life_value)

#类的定义
#对象
#实例化
#对象之间交互



