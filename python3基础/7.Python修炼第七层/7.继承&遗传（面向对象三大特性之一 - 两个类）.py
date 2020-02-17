# 继承 —— 面向对象的三大特性之一
# 想产生继承关系，必然是两个类以上.
# 继承表达的是一种 什么 是 什么的关系

\初识继承
# 什么是继承
继承是一种创建新类的方式，新建的类可以继承一个或多个父类（python支持多继承），父类又可称为基类或超类，新建的类称为派生类或子类。
子类会“”遗传”父类的属性，从而解决代码重用问题（比如练习7中Garen与Riven类有很多冗余的代码）

# python中类的继承分为：单继承和多继承
class ParentClass1: # 定义父类
    pass
class ParentClass2: # 定义父类
    pass
class SubClass1(ParentClass1): # 单继承，基类是ParentClass1，派生类是SubClass
    pass
class SubClass2(ParentClass1,ParentClass2): # python支持多继承，用逗号分隔开多个继承的类
    pass

# 查看继承
>>> SubClass1.__bases__ #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
(<class '__main__.ParentClass1'>,)
>>> SubClass2.__bases__
(<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)

# 经典类与新式类
1.只有在python2中才分新式类和经典类，python3中统一都是新式类.
2.在python2中，没有显式的继承object类的类，以及该类的子类，都是经典类
3.在python2中，显式地声明继承object的类，以及该类的子类，都是新式类
3.在python3中，无论是否继承object，都默认继承object，即python3中所有类均为新式类
# 关于新式类与经典类的区别，我们稍后讨论

# 提示：如果没有指定基类，python的类会默认继承object类，object是所有python类的基类，它提供了一些常见方法（如__str__）的实现。
>>> ParentClass1.__bases__
(<class 'object'>,)
>>> ParentClass2.__bases__
(<class 'object'>,)

\二 继承与抽象（先抽象再继承）
继承描述的是子类与父类之间的关系，是一种什么是什么的关系。要找出这种关系，必须先抽象再继承
抽象即抽取类似或者说比较像的部分。

抽象分成两个层次： 
1.将奥巴马和梅西这俩对象比较像的部分抽取成类； 
2.将人，猪，狗这三个类比较像的部分抽取成父类。
抽象最主要的作用是划分类别（可以隔离关注点，降低复杂度）
图片：继承1、继承2

\三 继承与重用性
# 使用继承来重用代码比较好的例子
==========================第一部分
例如
　　猫可以：喵喵叫、吃、喝、拉、撒
　　狗可以：汪汪叫、吃、喝、拉、撒

如果我们要分别为猫和狗创建一个类，那么就需要为 猫 和 狗 实现他们所有的功能，伪代码如下：
 
# 猫和狗有大量相同的内容
class 猫：

    def 喵喵叫(self):
        print '喵喵叫'

    def 吃(self):
        # do something

    def 喝(self):
        # do something

    def 拉(self):
        # do something

    def 撒(self):
        # do something

class 狗：

    def 汪汪叫(self):
        print '喵喵叫'

    def 吃(self):
        # do something

    def 喝(self):
        # do something

    def 拉(self):
        # do something

    def 撒(self):
        # do something

==========================第二部分
上述代码不难看出，吃、喝、拉、撒是猫和狗都具有的功能，而我们却分别的猫和狗的类中编写了两次。如果使用 继承 的思想，如下实现：

　　动物：吃、喝、拉、撒

　　   猫：喵喵叫（猫继承动物的功能）

　　   狗：汪汪叫（狗继承动物的功能）

伪代码如下：
class 动物:

    def 吃(self):
        # do something

    def 喝(self):
        # do something

    def 拉(self):
        # do something

    def 撒(self):
        # do something

# 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class 猫(动物)：

    def 喵喵叫(self):
        print '喵喵叫'
        
# 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class 狗(动物)：

    def 汪汪叫(self):
        print '喵喵叫'

==========================第三部分
# 继承的代码实现
class Animal:

    def eat(self):
        print("%s 吃 " %self.name)

    def drink(self):
        print ("%s 喝 " %self.name)

    def shit(self):
        print ("%s 拉 " %self.name)

    def pee(self):
        print ("%s 撒 " %self.name)

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        print('喵喵叫')

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed='狗'

    def cry(self):
        print('汪汪叫')

# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()

在开发程序的过程中，如果我们定义了一个类A，然后又想新建立另外一个类B，但是类B的大部分内容与类A的相同时，我们不可能从头开始写一个类B，这就用到了类的继承的概念。
通过继承的方式新建类B，让B继承A，B会‘遗传’A的所有属性(数据属性和函数属性)，实现代码重用。
class Hero:
    def __init__(self,nickname,aggressivity,life_value):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value

    def move_forward(self):
        print('%s move forward' %self.nickname)

    def move_backward(self):
        print('%s move backward' %self.nickname)

    def move_left(self):
        print('%s move forward' %self.nickname)

    def move_right(self):
        print('%s move forward' %self.nickname)

    def attack(self,enemy):
        enemy.life_value-=self.aggressivity
class Garen(Hero):
    pass

class Riven(Hero):
    pass

g1=Garen('草丛伦',100,300)
r1=Riven('锐雯雯',57,200)

print(g1.life_value)
r1.attack(g1)
print(g1.life_value)

'''
注意：像g1.life_value之类的属性引用，会先从实例中找life_value然后去类中找，然后再去父类中找...直到最顶级的父类。
'''
\重点！！！：再看属性查找
class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar(Foo):
    def f1(self):
        print('Foo.f1')


b=Bar() 
b.f2() 
'''
Foo.f2
Foo.f1
''' 

\四 派生
当然子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了。
class Riven(Hero):
    camp='Noxus'
    def attack(self,enemy): # 在自己这里定义新的attack,不再使用父类的attack,且不会影响父类
        print('from riven')

    def fly(self): # 在自己这里定义新的
        print('%s is flying' %self.nickname)
在子类中，新建的重名的函数属性，在编辑函数内功能的时候，有可能需要重用父类中重名的那个函数功能，应该是用调用普通函数的方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值
class Riven(Hero):
    camp='Noxus'
    def __init__(self,nickname,aggressivity,life_value,skin):
        Hero.__init__(self,nickname,aggressivity,life_value) #调用父类功能
        self.skin=skin #新属性
    def attack(self,enemy): #在自己这里定义新的attack,不再使用父类的attack,且不会影响父类
        Hero.attack(self,enemy) #调用功能
        print('from riven')
    def fly(self): #在自己这里定义新的
        print('%s is flying' %self.nickname)

r1=Riven('锐雯雯',57,200,'比基尼')
r1.fly()
print(r1.skin)

'''
运行结果
锐雯雯 is flying
比基尼

'''
\五 组合与重用性
软件重用的重要方式除了继承之外还有另外一种方式，即：组合。组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合
>>> class Equip: #武器装备类
...     def fire(self):
...         print('release Fire skill')
... 
>>> class Riven: #英雄Riven的类,一个英雄需要有装备,因而需要组合Equip类
...     camp='Noxus'
...     def __init__(self,nickname):
...         self.nickname=nickname
...         self.equip=Equip() # 用Equip类产生一个装备,赋值给实例的equip属性
... 
>>> r1=Riven('锐雯雯')
>>> r1.equip.fire() #可以使用组合的类产生的对象所持有的方法
release Fire skill

组合与继承都是有效地利用已有类的资源的重要方式。但是二者的概念和使用场景皆不同，
1.继承的方式
    通过继承建立了派生类与基类之间的关系，它是一种'是'的关系，比如白马是马，人是动物。
    当类之间有很多相同的功能，提取这些共同的功能做成基类，用继承比较好，比如老师是人，学生是人

2.组合的方式
    用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如教授有生日，教授教python和linux课程，教授有学生s1、s2、s3...

# 例子：继承与组合
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title=job_title
        self.course=[]
        self.students=[]

class Student(People): # 类的继承
    def __init__(self,name,age,sex):
        People.__init__(self,name,age,sex)
        self.course=[]

egon=Teacher('egon',18,'male','沙河霸道金牌讲师')
s1=Student('牛榴弹',18,'female')

python=Course('python','3mons',3000.0)
linux=Course('python','3mons',3000.0)

#为老师egon和学生s1添加课程
egon.course.append(python) # 类的组合
egon.course.append(linux)
s1.course.append(python)

#为老师egon添加学生s1
egon.students.append(s1)

#使用
for obj in egon.course:
    obj.tell_info()
'''
提示：当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好
'''
\六 子类中调用父类的方法
# 强调：二者使用哪一种都可以，但最好不要混合使用
# 方法一：指名道姓，即父类名.父类方法()
class Vehicle: # 定义交通工具类
     Country='China'
     def __init__(self,name,speed,load,power):
         self.name=name
         self.speed=speed
         self.load=load
         self.power=power

     def run(self):
         print('开动啦...')

class Subway(Vehicle): # 地铁
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)  # 指名道姓方式
        self.line=line

    def run(self):
        print('地铁%s号线欢迎您' %self.line)
        Vehicle.run(self)

line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
line13.run()
'''
地铁13号线欢迎您
开动啦...
'''
# 方法二：super()
class Vehicle: # 定义交通工具类
     Country='China'
     def __init__(self,name,speed,load,power):
         self.name=name
         self.speed=speed
         self.load=load
         self.power=power

     def run(self):
         print('开动啦...')

class Subway(Vehicle): # 地铁
    def __init__(self,name,speed,load,power,line):
        # super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
        super().__init__(name,speed,load,power)  # super方式
        self.line=line

    def run(self):
        print('地铁%s号线欢迎您' %self.line)
        super(Subway,self).run()

class Mobike(Vehicle): # 摩拜单车
    pass

line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
line13.run()

\继承查找顺序
即使没有直接继承关系，super仍然会按照mro继续往后查找
#A没有继承B,但是A内super会基于C.mro()继续往后找
class A:
    def test(self):
        super().test()
class B:
    def test(self):
        print('from B')
class C(A,B):
    pass

c=C()
c.test() #打印结果:from B


print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

\指名道姓与super()的区别
#指名道姓（深度优先）
class A:
    def __init__(self):
        print('A的构造方法')
class B(A):
    def __init__(self):
        print('B的构造方法')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C的构造方法')
        A.__init__(self)

class D(B,C):
    def __init__(self):
        print('D的构造方法')
        B.__init__(self)
        C.__init__(self)

    pass
f1=D() #A.__init__被重复调用
'''
D的构造方法
B的构造方法
A的构造方法
C的构造方法
A的构造方法
'''

#使用super(广度优先)
class A:
    def __init__(self):
        print('A的构造方法')
class B(A):
    def __init__(self):
        print('B的构造方法')
        super(B,self).__init__()

class C(A):
    def __init__(self):
        print('C的构造方法')
        super(C,self).__init__()

class D(B,C):
    def __init__(self):
        print('D的构造方法')
        super(D,self).__init__()

f1=D() #super()会基于mro列表,往后找
'''
D的构造方法
B的构造方法
C的构造方法
A的构造方法
'''
# 当你使用super()函数时,Python会在MRO列表上继续搜索下一个类。只要每个重定义的方法统一使用super()并只调用它一次,那么控制流最终会遍历完整个MRO列表,每个方法也只会被调用一次
# （注意注意注意：使用super调用的所有属性，都是从MRO列表当前的位置往后找，千万不要通过看代码去找继承关系，一定要看MRO列表）


\关于类的详细讲解
class Animal: # 父类
    def __init__(self,name,aggr,life_value):
        self.name = name  # 共有属性
        self.aggr = aggr  # 共有属性
        self.life_value = life_value # 共有属性

    def func(self):
        print(self.name)

class Foo: # 父类
    def func(self):
        print(self.name)

class Dog(Animal,Foo): # Dog子类继承Animal父类和Foo父类，类加括号就是继承类。
    def __init__(self,name,aggr,life_value,type): 
        # 如果Dog类自己没有__init__而父类有需要传给用父类的__init__方法。
        # 如果自己有__init__方法，父类也有__init__方法，那么实例化时要按照两个类需要的参数传值，把父类需要的传给父类。自己的留下（派生属性）。
        #Animal.__init__(self,name,aggr,life_value) # 经典类。这是传给父类的。
        super().__init__(name,aggr,life_value)  # 新式类，使用super()方法就不用传self了。这是传给父类的。
        self.dogtype = type    # 派生属性,独有的。

    def bite(self):            # 派生方法,独有的。
        Animal.func(self) # 调父类的func方法
        # Foo.func()      # 两个父类中都有func方法时，不建议这样越级使用，说明程序设计的有问题。
        super().func()    # 当继承多个类时默认从多个父类中按照从左到右开始找，此func方法是在Animal类中就找到了，所以不会在Foo类中找。

class Person(Animal):# 如果此处不继承父类下面也可以指名道姓的使用父类，只不过实例化出来的对象不能直接调用父类的其他方法。
    def __init__(self,name,aggr,life_value,money):
        Animal.__init__(self,name,aggr,life_value)
        self.money = money

    def attack(self):pass

egg = Dog('egon',100,2000,'金毛')
egg.bite() # egon
print(egg.__dict__)   # {'name': 'egon', 'aggr': 100, 'life_value': 2000, 'dogtype': '金毛'}
alex = Person('alex',100,2000,2000)
print(alex.__dict__)  # {'name': 'alex', 'aggr': 100, 'life_value': 2000, 'money': 2000}
alex.func()           # 可以直接调用父类中的方法
# Dog继承了Animal、Foo
# 父类 ：Animal
# 子类 ：Dog

\总结:
# 一个类可以有多个子类
# 子类调用方法；先调自己的，自己没有就调用父类的
# 写继承的过程：是先抽象，后继承。从对象往上写。
# 派生：父类没有的属性和方法在子类中就是派生出来的，称为派生属性和派生方法。


\多继承
# 一个类可以拥有多个父类
class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(C.__base__) # <class '__main__.A'> 查看继承了哪些类，只显示第一个父类A。
print(A.__base__) # <class 'object'>     输出object类（基类）

# object: 基类（类祖宗）,C的父类是A类和B类、C的爷爷类是object类、A和B的父类是object类。
    # 如果一个类有指定的父类，那么他的父类就是被指定的那个
    # 如果一个类没有指定的父类，那么他的父类就是object
    # 凡是继承了object类的类都是新式类
# python3里所有的类都是新式类
# 新式类调用父类的方法：
    # 指名道姓:父类名.方法名(self,aggr1...)；   ----> python2经典类只支持此方式
    # super关键字:super().方法名(aggr1,...)   ----> 只适用于新式类，python3

\案例:
# 教授类:（级别高、能力多）
    # 属性 年龄 姓名
    # 行为 讲课 写专利
# 教师类:（级别低、能力少）
    # 属性 年龄 姓名
    # 行为 讲课
# 教授是教师（继承表达的是一种 什么 是 什么的关系，即教授也能干教师的活，但教师干不了教授的活）
# 教师是父类/基类
# 教授是子类: 教授在教师的基础上可以做更多的事情，多出来的行为就是派生方法。

class Teacher:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def teach(self):
        print('%s正在讲课'%self.name)

class Professor(Teacher):
    def print_write(self):
        print('%s正在写专利'%self.name)

egon = Professor('egon',18,20000)
print(egon.__dict__)
print(egon.salary)
egon.teach() # 调用父类的teach方法
egon.print_write()

====================================================

class Teacher:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.teach()

    def teach(self):
        print('%s正在讲课'%self.name)

class Professor(Teacher):
    def print_write(self):
        print('%s正在写专利'%self.name)

    def teach(self):
        # super().teach()
        print('教授%s正在讲课'%self.name)

egon = Professor('egon',18,20000)
egon.teach() # 先读Professor类中的teach方法
print(egon.__dict__)
print(egon.salary)
egon.teach()
egon.print_write()


# 新式类多继承, 执行父类的方法是,python3 广度优先（就近走路，先把只有一条路的先走。多条路的后走。）。

class A:
    def func(self):
        print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B,C):pass
    # def func(self):
    #     print('D')

d = D()
d.func()
==============================================================
class A:
    def func(self):
        print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B):pass
    # def func(self):
    #     print('D')

class E(C):
    def func(self):
        print('E')

class F(D,E):pass
    # def func(self):
    #     print('F')

# f = F()
# f.func()

# 查看广度优先调用顺序
print(F.mro())  # [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

#经典类和新式类的区别
# 1、关于基类 ： 新式类默认继承object
# 2、关于在子类中执行父类的方法:新式类有super，经典类只能用指名道姓。
# 3、关于多继承：新式类 广度优先（mro），经典类：深度优先
# 在py3没有经典类，只有新式类；而在py2里经典类和新式类共存。

#关于继承：
# 子类继承父类
# 子类的对象调用方法，优先在子类中找，如果子类中有，就执行子类中的
#                               如果子类中没有，就执行父类的。多个父类以广度优先为准。

#写代码时关注self到底是哪个类的实例化对象

https://www.cnblogs.com/Eva-J/articles/7293890.html

