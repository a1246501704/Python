\ 组合 —— 面向对象的一种功能 
# 组合 - 是两个类之间的事儿
# 描述的是一种所属关系

\ 组合例一：
# 组合表达的是：什么有什么的关系，比如每个人都有生日,生日是由年月日组成。
class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

class Person:
    def __init__(self,name):
        self.name = name

alex_birth = Birthday(1968,1,1)
print(alex_birth.year)
alex = Person('alex')
alex.birth = alex_birth  # Birthday类的对象是alex的birth属性,这就是组合。
print(alex.birth.year)
print(alex.__dict__)     # {'name': 'alex', 'birth': <__main__.Birthday object at 0x1036201d0>}

或者

class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

class Person:
    def __init__(self,name,birth):
        self.name = name
        self.birthday = birth

alex_birth = Birthday(1968,1,1) # Birthday类的对象
print(alex_birth.year)
alex = Person('alex',alex_birth) # Birthday类的对象alex_birth是Person类对象alex的birth属性,这也是组合。
print(alex.birthday.year) 
print(alex.__dict__)      # {'name': 'alex', 'birthday': <__main__.Birthday object at 0x103c201d0>}


\ 组合例二：
# 人狗大战
# 人：人有武器，人和武器之间就是组合关系。
# 武器：伤害、属性
class Weapon: # 武器类
    def __init__(self,aggr,name,money):
        self.aggr = aggr
        self.name = name
        self.money = money

    def kill(self,dog_obj):
        # 属性的变化
        print('%s武器暴击%s,伤害%s'%(self.name,dog_obj.name,self.aggr))
        dog_obj.life_value -= self.aggr

class Dog: # 狗类
    def __init__(self, name, type, aggr):
        self.name = name
        self.dog_type = type
        self.aggr = aggr
        self.life_value = 2000

    def bite(self, person_obj):  # self==egg,person_obj=alex
        # 属性的变化
        print('%s咬了%s' % (self.name, person_obj.name))
        person_obj.life_value -= self.aggr

class Person: # 人类
    rol = '人'  # 数据属性、静态属性、类属性
    country = '中国'

    def __init__(self, name, age, life_value):  # 初始化方法
        self.name = name  # 属性、对象属性
        self.theage = age
        self.life_value = life_value
        self.aggr = 1

    def attack(self, dog_obj):  # 函数属性、动态属性、方法
        # 属性的变化
        print('%s攻击了%s' % (self.name, dog_obj.name))
        dog_obj.life_value -= self.aggr

knife = Weapon(200,'杀猪刀',1900)
alex = Person('alex',38,500)
egg = Dog('egon','二哈',20)

alex.money = 2000
if alex.money > knife.money:
    alex.money -= knife.money
    alex.weapon = knife

print(egg.life_value)
alex.weapon.kill(egg) # 组合。 也可以写成 alex.knife.kill(egg)
print(egg.life_value)

