# property
# classmethod 类方法
# staticmethod

\property : property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return self.r *self.r *3.14

c1 = Circle(5)
print(c1.area) # property实现了在调用area时不用加括号了，对内area是一个方法，对外是一个属性。

class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)

p1=People('egon',75,1.85)
print(p1.bmi) # 调用类里面的方法时不用加括号


class A:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter  # 这样__name这个私有属性就可以在外面修改了
    def name(self,new_name):
        if type(new_name) is str:
            self.__name = new_name

a = A('alex')
print(a.name)
# 希望不从外部被修改 所以设置成私有的属性
# 但是又希望能从外部查看 所以使用一个property
# 又是私有属性又希望在外面可以修改  属性名.setter
a.name = 'alex_sb'
print(a.name)

\classmethod: 绑定方法,classmehtod是给类用的，即绑定到类，哪个类在使用时会将这个类本身当做参数传给类方法的第一个参数（即便是对象来调用也会将类当作第一个参数传入），python为我们内置了函数classmethod来把类中的函数定义成类方法
# 绑定方法：
    # 对象使用时会将对象本身当作第一个对象传入
    # 类使用时会将类本身当作第一个对象传入
class A:
    country = 'China'
    def func(self):
        self.name= 'alex'

    @classmethod       # 类方法：就是不需要传具体的对象，但是可以使用类的属性、静态属性。可以使用一些变量，但不能使用对象的变量。
    def c_method(cls): # cls固定传，就是自己这个类 A。被装饰的对象不需要实例化，直接使用 类名.方法名()  就可以调用。
        print('in class method')
        print(cls.country)

    @staticmethod      # 静态方法，不可以使用类里的其他变量。
    def s_method():
        print('in static method')
        # print(country) # 加了@staticmethod 装饰器后就无法调用类里面的 属性和方法了,加cls也不行。

A.c_method()
A.s_method()

#完全的面向对象编程
#所有的方法代码都必须写类里
#只能把原来的函数写进类里
#而原本又只是函数 所以就加上一个staticmethod装饰器

\staticmethod: 非绑定方法,在类内部用staticmethod装饰的函数即非绑定方法，就是普通函数statimethod不与类或对象绑定，谁都可以调用，没有自动传值效果
# 对象和类都能用，不会自动传任何参数。
import hashlib
import time
class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port
    @staticmethod    # 被装饰的对象不需要实例化，直接使用 类名.方法名  就可以调用
    def create_id(): # 就是一个普通工具
        m=hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

print(MySQL.create_id) # <function MySQL.create_id at 0x0000000001E6B9D8> #查看结果为普通函数
conn=MySQL('127.0.0.1',3306)
print(conn.create_id)  # <function MySQL.create_id at 0x00000000026FB9D8> #查看结果为普通函数

\classmethod与staticmethod的区别
import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    @staticmethod
    def from_conf():
        return MySQL(settings.HOST,settings.PORT)

    # @classmethod #哪个类来调用,就将哪个类当做第一个参数传入
    # def from_conf(cls):
    #     return cls(settings.HOST,settings.PORT)

    def __str__(self):
        return '就不告诉你'

class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' %(self.host,self.port)

m=Mariadb.from_conf()
print(m) # 我们的意图是想触发Mariadb.__str__,但是结果触发了MySQL.__str__的执行，打印就不告诉你：


\练习
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @staticmethod
    def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间，将本类当作第一个参数传给now()。触发__init__初始化方法。
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
    @staticmethod
    def tomorrow():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

a=Date('1987',11,27) # 自己定义时间
b=Date.now()         # 采用当前时间
c=Date.tomorrow()    # 采用明天的时间

print(a.year,a.month,a.day)
print(b.year,b.month,b.day)
print(c.year,c.month,c.day)


#分割线==============================
import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @staticmethod
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e) #我们的意图是想触发EuroDate.__str__,但是结果为
'''
输出结果:
<__main__.Date object at 0x1013f9d68>
'''
# 因为e就是用Date类产生的,所以根本不会触发EuroDate.__str__,解决方法就是用classmethod

import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    # @staticmethod
    # def now():
    #     t=time.localtime()
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday)

    @classmethod #改成类方法
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday) #哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
'''
输出结果:
year:2017 month:3 day:3
'''