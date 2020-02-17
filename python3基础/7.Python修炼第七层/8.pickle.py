class Person:
    rol = '人'  # 数据属性、静态属性、类属性
    country = '中国'

    def __init__(self, name, age, life_value):  # 初始化方法
        self.name = name  # 属性、对象属性
        self.theage = age
        self.life_value = life_value
        self.aggr = 1

    def attack(self, dog_obj):  # 函数属性、动态属性、方法
        print('%s攻击了%s' % (self.name, dog_obj.name))
        dog_obj.life_value -= self.aggr

class Weapon:
    def __init__(self,aggr,name,money):
        self.aggr = aggr
        self.name = name
        self.money = money

    def kill(self,dog_obj):
        print('%s武器暴击%s,伤害%s'%(self.name,dog_obj.name,self.aggr))
        dog_obj.life_value -= self.aggr
alex = Person('alex', 38, 500)
knife = Weapon(200,'杀猪刀',1900)
alex.weapon = knife
import pickle
ret = pickle.dumps(alex)
print(ret)

pickle.loads