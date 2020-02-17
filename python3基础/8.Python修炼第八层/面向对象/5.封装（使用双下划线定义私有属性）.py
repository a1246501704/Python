\一 引子
# 从封装本身的意思去理解，封装就好像是拿来一个麻袋，把小猫，小狗，小王八，还有alex一起装进麻袋，然后把麻袋封上口子。照这种逻辑看，封装=‘隐藏’，这种理解是相当片面的

\二 先看如何隐藏
# 在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）
# 先看如何隐藏  __开头
# 其实这仅仅这是一种变形操作且仅仅只在类定义阶段发生变形
# 类中所有双下划线开头的名称如__x都会在类定义时自动变形成：_类名__x的形式：

class A:
    __N=0 # 类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
    def __init__(self):
        self.__X=10  # 变形为self._A__X

    def __foo(self): # 变形为_A__foo
        print('from A')

    def bar(self):
        self.__foo() # 只有在类内部才可以通过__foo的形式访问到.

print(A._A__N) # 0   A._A__N是可以访问到的，但是不合规。
# 这种，在外部是无法通过__x这个名字访问到。为什么呢？看下面，在类中定义时带双下划线的属性都加了 _类名__属性
print(A.__dict__) # {'__module__': '__main__', '_A__N': 0, '__init__': <function A.__init__ at 0x106d32ae8>, '_A__foo': <function A.__foo at 0x106d56158>, 'bar': <function A.bar at 0x106d561e0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
obj=A()
obj.bar()  # from A  


# 在类内定义，在类外不让使用。那定义有什么用呢？
class Goods:
    __DISCONT = 0.8  # 加了双下划线就被定义成了一个私有的属性
    def __init__(self,org_price):
        self.price = org_price * Goods.__DISCONT # 在内部就使用了

apple = Goods(10)
print(apple.price) # 8.0

\在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
#正常情况
>>> class A:
...     def fa(self):
...         print('from A')
...     def test(self):
...         self.fa()
... 
>>> class B(A):
...     def fa(self):
...         print('from B')
... 
>>> b=B()
>>> b.test()
from B
 
#把fa定义成私有的，即__fa
>>> class A:
...     def __fa(self): #在定义时就变形为_A__fa
...         print('from A')
...     def test(self):
...         self.__fa() #只会与自己所在的类为准,即调用_A__fa
... 
>>> class B(A):
...     def __fa(self):
...         print('from B')
... 
>>> b=B()
>>> b.test()
from A


#在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
class Foo:
    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def f2(self):
        self.__f1() #self._Foo_f1

class Bar(Foo):
    def __f1(self): #_Bar__f1
        print('Bar.f1')

# b=Bar()
# b.f2()



\封装不是单纯意义的隐藏
封装的真谛在于明确地区分内外，封装的属性可以直接在内部使用，而不能被外部直接使用，然而定义属性的目的终归是要用，外部要想用类隐藏的属性，需要我们为其开辟接口，
让外部能够间接地用到我们隐藏起来的属性，那这么做的意义何在？？？
# 1：封装数据：将数据隐藏起来这不是目的。隐藏起来然后对外提供操作该数据的接口，然后我们可以在接口附加上对该数据操作的限制，以此完成对数据属性操作的严格控制。
class Teacher:
    def __init__(self,name,age):
        # self.__name=name
        # self.__age=age
        self.set_info(name,age)

    def tell_info(self):
        print('姓名:%s,年龄:%s' %(self.__name,self.__age))
    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')
        self.__name=name
        self.__age=age

t=Teacher('egon',18)
t.tell_info()

t.set_info('egon',19)
t.tell_info()


# 2：封装函数属性：为了隔离复杂度
封装方法举例： 
1. 你的身体没有一处不体现着封装的概念：你的身体把膀胱尿道等等这些尿的功能隐藏了起来，然后为你提供一个尿的接口就可以了（接口就是你的。。。，），你总不能把膀胱挂在身体外面，上厕所的时候就跟别人炫耀：hi，man，你瞅我的膀胱，看看我是怎么尿的。
2. 电视机本身是一个黑盒子，隐藏了所有细节，但是一定会对外提供了一堆按钮，这些按钮也正是接口的概念，所以说，封装并不是单纯意义的隐藏！！！
3. 快门就是傻瓜相机为傻瓜们提供的方法，该方法将内部复杂的照相功能都隐藏起来了
提示：在编程语言里，对外提供的接口（接口可理解为了一个入口），可以是函数，称为接口函数，这与接口的概念还不一样，接口代表一组接口函数的集合体。

#取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱
#对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做
#隔离了复杂度,同时也提升了安全性

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()


\封装与扩展性
封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使用用者只知道一个接口(函数)，只要接口（函数）名、参数不变，
使用者的代码永远无需改变。这就提供一个良好的合作基础——或者说，只要接口这个基础约定不变，则代码改变不足为虑。
#类的设计者
class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.__high=high
    def tell_area(self): # 对外提供的接口，隐藏了内部的实现细节，此时我们想求的是面积
        return self.__width * self.__length

#使用者
>>> r1=Room('卧室','egon',20,20,20)
>>> r1.tell_area()       # 使用者调用接口tell_area

#类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.__high=high
    def tell_area(self): # 对外提供的接口，隐藏内部实现，此时我们想求的是体积,内部逻辑变了,只需求修该下列一行就可以很简答的实现,而且外部调用感知不到,仍然使用该方法，但是功能已经变了
        return self.__width * self.__length * self.__high

#对于仍然在使用tell_area接口的人来说，根本无需改动自己的代码，就可以用上新功能
>>> r1.tell_area()