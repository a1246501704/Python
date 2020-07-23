property      # property装饰器就是负责把一个方法变成一个属性去调用，无需加()
classmethod   # classmethod是一个 类方法，虽然属于类，可以访问类的其他成员，但是不能访问实例化对象的参数。并且可以在不把类实例化的前提下，通过类名进行调用，但是值得注意的是，classmethod也可以通过实例调用。
staticmethod  # staticmethod是一个 静态方法，即这个方法是一个普通方法，虽然属于类，但是不能访问类和实例的其他成员。并且可以在不把类实例化的前提下，通过类名进行调用。值得注意的是，staticmethod也可以通过实例调用。
而使用 @staticmethod 或 @classmethod，就可以不需要实例化，直接类名.方法名()来调用。

\property属性: property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

# 定义
一个可以使实例方法用起来像实例属性一样的特殊关键字，可以对应于某个方法，通过使用property属性，能够简化调用者在获取数据的流程(使代码更加简明)。
property属性的定义和调用要注意以下几点：
    1.调用时，无需括号，加上就错了
    2.并且仅有一个self参数


\实现property属性的两种方式
# 1.装饰器
新式类中的属性有三种访问方式，并分别对应了三个被
@property对应读取
@方法名.setter修改
@方法名.deleter删除属性

class Goods:
    def __init__(self):
        self.age = 18

    @property
    def price(self): # 读取
        return self.age
     
    # 方法名.setter
    @price.setter # 设置,仅可接收除self外的一个参数
    def price(self, value):
        self.age = value
     
    # 方法名.deleter
    @price.deleter # 删除
    def price(self):
        del self.age

 
# ############### 调用 ###############
obj = Goods()  # 实例化对象 
print(obj.age) # 18
print(obj.price) # 18  # property实现了在调用 price 时不用加括号了，对内 price 是一个方法，对外是一个属性。
obj.age = 123  # 修改age的值
del obj.age    # 删除age属性的值

# 1.2 使用property取代getter和setter方法
使用@property装饰器改进私有属性的get和set方法
class Money(object):
    def __init__(self):
        self.__money = 0
 
    # 使用装饰器对money进行装饰，那么会自动添加一个叫money的属性，当调用获取money的值时，调用装饰的方法
    @property
    def money(self):
        return self.__money
 
    # 使用装饰器对money进行装饰，当对money设置值时，调用装饰的方法
    @money.setter # 这样__money这个私有属性就可以在外面修改了
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
 
a = Money()
a.money = 100
print(a.money) # 100
# 用途
    1.希望不从外部被修改 所以设置成私有的属性（__开头）
    2.但是又希望能从外部查看 所以使用一个property
    3.又是私有属性又希望在外面可以修改  属性名.setter

# 2.类属性
当使用 类属性 的方式创建property属性时，property()方法有四个参数
    第一个参数是方法名(查)，调用  对象.属性          # 时自动触发执行方法
    第二个参数是方法名(改)，调用  对象.属性 ＝ XXX   # 时自动触发执行方法
    第三个参数是方法名(删)，调用  del 对象.属性      # 时自动触发执行方法
    第四个参数是字符串(描)，调用  对象.属性.doc      # 此参数是该属性的描述信息
class Goods(object):
    def __init__(self):  
        self.price = 100    # 原价
        self.discount = 0.8 # 折扣
 
    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.price * self.discount
        return new_price
 
    def set_price(self, value):
        self.price = value
 
    def del_price(self):
        del self.price
                       # 获取      设置       删除        描述文档
    PRICE = property(get_price, set_price, del_price, '价格属性描述...') # 对象.属性.doc 测试发现不好使
    # 使用此方式设置
  
obj = Goods()
print(obj.PRICE) # 获取商品价格 80
obj.PRICE = 200  # 修改商品原价
print(obj.PRICE) # 获取商品价格 160
del obj.PRICE    # 删除商品原价



\classmethod: 绑定方法,classmehtod是给类用的，即绑定到类，哪个类在使用时就会将这个类本身当做参数传给classmethod类方法的第一个参数（即便是对象来调用也会将类当作第一个参数传入），python为我们内置了函数classmethod来把类中的函数定义成类方法
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
类方法（不需要实例化类就可以被类本身调用）

# 绑定方法：
    # 对象使用时会将对象本身当作第一个对象传入
    # 类使用时会将类本身当作第一个对象传入
    # 实例化的对象无法调用被 @classmethod装饰的方法

# 限制
    # 可以使用类的 静态属性 ，但不能使用对象的变量。

class A:
    country = 'China'
    def func1(self):
        self.name = 'alex'

    def func2(self):
        print('funrc 2')

    @classmethod       # 类方法：就是不需要传具体的对象self，但是可以使用类的属性、静态属性、方法。可以使用一些公共变量，但不能使用对象的变量，因为不能给c_method传self。
    def c_method(cls): # cls固定传，就是自己这个类 A。被装饰的对象不需要实例化，直接使用 类名.方法名()  就可以调用。
        print('in class method')
        print(cls.country)
        cls().func2()

    @staticmethod      # 静态方法，不可以使用类里的其他变量。
    def s_method():
        print('in static method')
        # print(country) # 加了@staticmethod 装饰器后就无法调用类里面的 属性和方法了,加cls也不行。

A.c_method()
A.s_method()

# in class method
# China
# funrc 2
# in static method


class A(object):

    # 属性默认为类属性（可以给直接被类本身调用）
    num = "类属性"

    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self): # self : 表示实例化类后的地址id
        print("func1")
        print(self)

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):  # cls : 表示没用被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()

    # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
    def func3():
        print("func3")
        print(A.num) # 属性是可以直接用类本身调用的
    
# A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()
A.func3()


\staticmethod: 非绑定方法（静态方法）,在类内部用 staticmethod 装饰的函数即非绑定方法，就是普通函数 statimethod 不与类或对象绑定，谁都可以调用，没有自动传值效果
staticmethod用于修饰类中的方法,使其可以在不创建类实例的情况下调用方法，这样做的好处是执行效率比较高。当然，也可以像一般的方法一样用实例调用该方法。该方法一般被称为静态方法。
静态方法不可以引用类中的属性或方法，其参数列表也不需要约定的默认参数self。我个人觉得，静态方法就是类对外部函数的封装，有助于优化代码结构和提高程序的可读性。
当然了，被封装的方法应该尽可能的和封装它的类的功能相匹配。
# 对象和类都能用，不会自动传任何参数。

# 用途:
    # 当使用完全的面向对象编程时，就是将所有的方法代码都必须写类里。
    # 这时只能把函数写都写进类里，而原本又只是普通函数（不属于任何类的函数）也要放在类中。
    # 所以就加上一个 staticmethod 装饰器，让这个函数还是一个单独的函数 在外面使用  类名.方法名 直接调用

# 限制
    # 不允许使用类 静态属性、方法
    # @staticmethod 返回被装饰函数这个静态方法，该方法不强制要求传递参数
    # @staticmethod 静态方法只是名义上归属类管理，但是不能使用类变量和实例变量，是类的工具包放在函数前（该函数不传入self或者cls），所以不能访问类属性和实例属性


如下声明一个静态方法
class C(object):
    #声明一个静态方法
    @staticmethod
    def f(): # 没传self哦
        print('is staticmethod')
# 以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。
C.f()      # 静态方法无需实例化
C().f()    # 也可以实例化后调用
# cobj = C() # 同等于 C().f()
# cobj.f()        



import hashlib
import time
class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port

    @staticmethod    # 被装饰的对象不需要实例化，直接使用 类名.方法名  就可以调用
    def create_id(): # 就是一个普通的方法，没传self哦。
        m=hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

print(MySQL.create_id) # <function MySQL.create_id at 0x0000000001E6B9D8> #查看结果为普通函数
conn=MySQL('127.0.0.1',3306)
print(conn.create_id)  # <function MySQL.create_id at 0x00000000026FB9D8> #查看结果为普通函数




# staticmethod 参数要求是 Callable（可调用的）, 也就是说 Class 也是可以的：
class C1(object):
    @staticmethod
    class C2(object):
        def __init__(self, val = 1):
            self.val = val
        def shout(self):  
            print("Python世界第%d!"%self.val)
tmp = C1.C2(0)
print(type(tmp))    # 输出 : <class '__main__.C1.C2'>
tmp.shout()         # 输出 : Python世界第0!

\classmethod 与 staticmethod 的区别
　　在python中，要调用一个类中的方法，一般的操作步骤如下：
    　　步骤1、实例化此类
    　　步骤2、调用此类中的方法
　　@classmethod修饰的函数：第一个参数必须是表示自身类的cls
　　@staticmethod修饰的函数：不需要表示自身对象的self，也不需要表示自身类的cls，跟普通函数一样
class cal:
    cal_name = '计算器'
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property           # 在cal_add函数前加上@property，使得该函数可直接调用，封装起来
    def cal_add(self):
        return self.x + self.y

                        # 在cal_info函数前加上 @classmethod，则该函数变为类方法，
    @classmethod        # 该函数只能访问到类的数据属性，不能获取实例的数据属性(self的、__init__的)
    def cal_info(cls):  # python自动传入位置参数cls就是类本身
        print('这是一个%s'%cls.cal_name)   # cls.cal_name 调用类自己的数据属性
        # print(x)      # 报错，不支持
        # print(cls.x)  # 报错，不支持

    @staticmethod        # 静态方法 类或实例均可调用
    def cal_test(a,b,c): # 该静态方法函数里不传入 self 或 cls
        print(a,b,c)

c1 = cal(10,11)
print(c1.cal_add)   # 21
cal.cal_test(1,2,3) # 1 2 3
c1.cal_test(1,2,3)  # 1 2 3
cal.cal_info()      # 这是一个计算器


class newC(object):
    val = 100
    def func(self):
        print('run func')

    @classmethod
    def class_func(cls):  # cls == newC
        print('run class_func')
        print(cls.val)
        cls().func()

    @staticmethod
    def static_func():
        print('run static_func')
        print(newC.val)
        new = newC.func()

newC.class_func()
# newC.static_func() # 报错，非实例化调用类方法

new = newC()
new.class_func()    # 实例化调用类方法
# new.static_func() # 报错，非实例化调用类方法

\练习
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @staticmethod
    def now(): # 用Date.now()的形式去产生实例,该实例用的是当前时间，将本类当作第一个参数传给now()。触发__init__初始化方法。
        t=time.localtime() # 获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) # 新建实例并且返回

    @staticmethod
    def tomorrow(): # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
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

e=EuroDate.now() # 继承自父类的now方法
print(e)         # 我们的意图是想触发EuroDate.__str__,但是结果为
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
        return cls(t.tm_year,t.tm_mon,t.tm_mday) # 哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e) # 我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
'''
输出结果:
year:2017 month:3 day:3
'''