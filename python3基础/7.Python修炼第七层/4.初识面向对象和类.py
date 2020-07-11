\类与对象
类即类别、种类，是面向对象设计最重要的概念，对象是特征与技能的结合体，而类则是一系列对象相似的特征与技能的结合体
那么问题来了，先有的一个个具体存在的对象（比如一个具体存在的人），还是先有的人类这个概念，这个问题需要分两种情况去看

# 在现实世界中：先有对象，再有类
世界上肯定是先出现各种各样的实际存在的物体，然后随着人类文明的发展，人类站在不同的角度总结出了不同的种类，如人类、动物类、植物类等概念
也就说，对象是具体的存在，而类仅仅只是一个概念，并不真实存在

# 在程序中：务必保证先定义类，后产生对象
这与函数的使用是类似的，先定义函数，后调用函数，类也是一样的，在程序中需要先定义类，后调用类。
不一样的是，调用函数会执行函数体代码返回的是函数体执行的结果，而调用类会产生对象，返回的是对象。

#def
\面向过程编程
    # 固定的目的 固定的结果
    # 从头到尾把要执行的步骤堆积出来就好了
#class
\面向对象编程
    # 有一个抽象的过程
    # 上帝视角：结果不能预测

class Person:          # 类名首字母大写，并不是规定。而是一个约定俗成的约定。
    '''
    这是一个测试类
    '''
    rol = '人'         # 数据属性、静态属性
    country = '中国'
    def attack(self):  # 函数属性、动态属性、方法
        pass

# Person类名全局唯一
print(callable(Person)) # 判断是否可调用
print(Person())     # 返回一个对象。一个类名加上括号就会返回一个对象，多次一个类名加上括号返回的是不同的对象。
print(Person.rol)   #.属性名，返回属性的值  人
Person.rol = '人类'  # 修改属性的值
print(Person.__dict__)  # 查看类的字典属性
# {'__module__': '__main__', 'role': '人类', 'country': '中国', 'attack': <function Person.attack at 0x105b4fae8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
print(Person.__dict__['role']) # 人 ，可以调用但不可以修改。
# 类也有一个属于自己的名称空间：静态属性和动态属性
print(Person.country) # 中国
print(Person.attack) # <function Person.attack at 0x106532ae8>
# print(Person.attack())  报错：没有self参数


\类的定义
# class 类名:
#     静态属性 = '值'
#     def 方法(self):
#         pass
#
# 对象 = 类名()
# 对象.静态属性
# 对象.方法 #可以调用不能执行

\python为类内置的特殊属性
类名.__name__  # 类的名字(字符串)
    Person
类名.__doc__   # 类的文档字符串
    这是一个测试类
类名.__base__  # 类的第一个父类(在讲继承时会讲)
    <class 'object'>
类名.__bases__ # 类所有父类构成的元组(在讲继承时会讲)
    (<class 'object'>,)
类名.__dict__  # 类的字典属性
    {'__module__': '__main__', 'role': '人', 'country': '中国', 'attack': <function Person.attack at 0x106d32ae8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
类名.__module__# 类定义所在的模块
    __main__
类名.__class__ # 实例对应的类(仅新式类中)
    <class 'type'>


\类的使用+__init__初始化方法
class Person: # 也可以写成 Person()，括号可写可不写。
    rol = '人'         # 数据属性、静态属性、类属性
    country = '中国'
    def __init__(self,name,age,life_value): # __init__是初始化方法，参数必传。只要实例化实例就会触发__init__方法执行。
        # self.__dict__['name'] = name # 同等于 self.name = name
        self.name = name  # 属性、对象属性，__init__方法接收过来的参数如果没有和self关联。实例化后的对象无法操作没有关联的参数。
        self.theage = age
        self.life_value = life_value
        self.aggr = 200   # 共有且不需要初始化时传入的参数，可以在初始化方法中写死。
        # return None  # __init__不需要返回值，默认就返回的self
    def attack(self):     # 函数属性、动态属性、方法。self就是上面的self就是实例化的对象名。也可以写别的参数。
        #self只是一个形式参数，可以叫其他名字，但正常没人会这样
        #self是水性杨花，哪个对象调这个方法，self就是谁。
        print('attack方法被%s执行了'%self.name)

alex = Person('alex',38,2000)  #alex 对象，alex和self是同一个对象
print(alex.name)        # alex
print(alex.theage)      # 38
print(alex.life_value)  # 2000
#类加上括号的过程：就是实例化
    #1.先创建了一个对象 self.__dict__ = {}
    #2.才执行初始化方法__init__,同时把创建的对象扔到了__init__参数里。这个对象就是self。
Person.rol
alex.level = '150'      # 给alex对象创建一个属性
print(alex.level)       # 查看alex的level属性，即使类的__init__初始化方法中没有也可以为对象再单独添加属性。
alex.name = 'Alexander' # 修改alex的name属性
print(alex.name)        # 查看alex的name属性
print(alex.__dict__['name'])    # 对象也有__dict__属性
alex.__dict__['name'] = 'alex'  # 对象可以使用dict来修改属性的值，使用类名不可以修改。
print(alex.name)
alex.theage = 48        # 对象在修改自己的属性时使用的是__init__方法中self.后面的值，不是使用传给__init__的值。
print(alex.theage)      # 48
print(alex.__dict__)    # 实例化的每个对象都有属于自己的 __dict__ {'name': 'alex', 'theage': 48, 'life_value': 2000, 'aggr': 200, 'level': '150'}
egg = Person('egon',38,2000)
print(egg.name)         # egon
egg.name = 'egon-egg'   
print(egg.name)         # egon-egg
print(alex.name)        # Alexander

# 1.类名加括号得到对象(实例)，这个过程就是实例化。
# 2.类是我们自己抽象出来的
# 3.实例化 对象 = 类名()
# 4.类经过实例化就产生了对象/实例
# 5.类中可以有任意python代码，这些代码在类定义阶段便会执行
# 6.因而会产生新的名称空间，用来存放类的变量名与函数名，可以通过Person.__dict__查看
# 7.对于经典类来说我们可以通过该字典操作类名称空间的名字（新式类有限制），但python为我们提供专门的.语法
# 8.点是访问属性的语法，类中定义的名字，都是类的属性
# 9.所有对象都需要的参数放在__init__的参数中，必须被传。对象私有的可以实例化后再单独赋值。
# 10.传给__init__方法的参数如果不和self关联，属于白传。实例化后的对象是无法使用此参数的。关联后在self.__dict__中才会有。


\真正使用方法的不是类而是对象
alex = Person('alex',38,2000)  # alex 对象
egg = Person('egon',18,1000)   # egg 对象

Person.attack(alex)  # attack方法被alex执行了
Person.attack(egg)   # attack方法被egg执行了
alex.attack()   #同等于 Person.attack(alex)
egg.attack()    #同等于 Person.attack(egg)

#类：静态属性 动态属性
#类可以调用静态属性
#类可以查看动态属性 却必须要带上具体的对象参数才能调用动态属性
#对象：可以拥有自己的对象属性，并且可以调用类中的方法。

\对象可以调用类的方法么，可以
# 属性查找
# 1. 类的数据属性是所有对象共享的
# 2. 类的函数属性是绑定给对象用的
class Person:
    rol = '人'         # 数据属性、静态属性、类属性
    country = '中国'
    def __init__(self,name,age,life_value): #初始化方法
        # self.__dict__['name'] = name
        self.name = name       # 属性、对象属性
        self.theage = age
        self.life_value = life_value

    def attack(self):  # 函数属性、动态属性、方法
        #self只是一个形式参数，可以叫其他名字，但正常没人会这样
        #self是水性杨花，那个对象调这个方法，self就是那个对象
        print('attack方法被%s执行了'%self.name)

egg = Person('egon',18,1000)
alex = Person('alex',38,2000)
print(alex.rol)     # 人
print(alex.country) # 中国
egg.aggr = 200
alex.country = '印度'
print(alex.country) # 印度
print(egg.country)  # 中国 ，egg取的类的country的值
print(alex.__dict__)# {'name': 'alex', 'theage': 38, 'life_value': 2000, 'country': '印度'}
print(egg.__dict__) # {'name': 'egon', 'theage': 18, 'life_value': 1000, 'aggr': 200}

# 类有属于自己的命名空间
# 对象也是，实例化后所有的属性都在自己的命名空间生成了一份。修改和添加也只是在自己的命名空间生效。类的静态属性不会变。
# 类不可以调用对象的属性
# 但是对象在寻找属性的时候，是先找自己名称空间的，找不到就找类名称空间里的，类也找不到就找父类...最后都找不到就抛出异常。  

\绑定到对象的方法的特殊之处
class OldboyStudent:
    school='oldboy'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def learn(self):
        print('%s is learning' %self.name) #新增self.name

    def eat(self):
        print('%s is eating' %self.name)

    def sleep(self):
        print('%s is sleeping' %self.name)


s1=OldboyStudent('李坦克','男',18)
s2=OldboyStudent('王大炮','女',38)
s3=OldboyStudent('牛榴弹','男',78)
# 类中定义的函数（没有被任何装饰器装饰的）是类的函数属性，类可以使用，但必须遵循函数的参数规则，有几个参数需要传几个参数

OldboyStudent.learn(s1) #李坦克 is learning
OldboyStudent.learn(s2) #王大炮 is learning
OldboyStudent.learn(s3) #牛榴弹 is learning
# 类中定义的函数（没有被任何装饰器装饰的）,其实主要是给对象使用的，而且是绑定到对象的，虽然所有对象指向的都是相同的功能，但是绑定到不同的对象就是不同的绑定方法
# 强调：绑定到对象的方法的特殊之处在于，绑定给谁就由谁来调用，谁来调用，就会将‘谁’本身当做第一个参数传给方法，即自动传值（方法__init__也是一样的道理）

s1.learn() #等同于OldboyStudent.learn(s1)
s2.learn() #等同于OldboyStudent.learn(s2)
s3.learn() #等同于OldboyStudent.learn(s3)
# 注意：绑定到对象的方法的这种自动传值的特征，决定了在类中定义的函数都要默认写一个参数self，self可以是任意名字，但是约定俗成地写出self。



\练习
# 写一个狗类

class Dog:
    def __init__(self,name,type):
        self.name = name
        self.dog_type = type
        self.life_value = 2000

    def bite(self,name):
        print('%s咬了%s'%(self.name,name))

旺财 = Dog('旺财','土狗')
#使用init去进行属性的初识化
#1.规范所有的对象都拥有一些基础的属性
#2.方便

print(旺财.name)
print(旺财.dog_type)
print(旺财.life_value)
旺财.bite('alex')   #Dog.bite(旺财,'alex')

# 练习1
#创建一个类,实例化对象，需要做一个计数器，这个类每实例化一次，计数器加一
#所有的对象共享这个计数个数
class Dog:
    counter = 0
    def __init__(self,name,type):
        self.name = name
        self.dog_type = type
        self.life_value = 2000
        Dog.counter += 1

史努比 = Dog('史努比','大白狗')
史努比2 = Dog('史努比','大白狗')
print(史努比.counter)
print(史努比2.counter)

# 练习2
#创建一个圆形类
#有一个属性：圆的半径
#提供两个方法：计算圆面积（圆面积=圆周率×半径×半径） 、计算圆周长（圆的周长=直径×圆周率）
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r**2*pi

    def perimeter(self):
        return self.r*2*pi

c1 = Circle(5) # 传入半径
print(c1.area())
print(c1.perimeter())
c2 = Circle(20)
print(c2.area())
print(c2.perimeter())


# 练习3
# 在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健

# 两个人物 --> 人类
# 姓名 年龄 性别  ---> 属性
# 行为  --> 方法
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def shangshan(self):
        print('%s,%s岁,%s,上山去砍柴'%(self.name,self.age,self.sex))

    def kaiche(self):
        print('%s,%s岁,%s,开车去东北'%(self.name,self.age,self.sex))

    def dabaojian(self):
        print('%s,%s岁,%s,最爱大保健'%(self.name,self.age,self.sex))

xiaoming = Person('小明',10,'男') # 实例化一个小明
old_li = Person('老李',90,'男')   # 实例化一个老李
xiaoming.shangshan()
old_li.shangshan()

#面向过程和面向对象编程
#思路1 从只关心某一个对象变成抽象规范了一类对象
#思路2 当多个函数都需要传递同样的多个参数的时候，考虑使用面向对象的思想。

