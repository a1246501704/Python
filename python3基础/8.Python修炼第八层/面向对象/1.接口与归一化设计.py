\为何要用接口
接口提取了一群类共同的函数，可以把接口当做一个函数的集合。然后让子类去实现接口中的函数。
这么做的意义在于归一化，什么叫归一化，就是只要是基于同一个接口实现的类，那么所有的这些类产生的对象在使用时，从用法上来说都一样。

\归一化的好处在于：
1. 归一化让使用者无需关心对象的类是什么，只需要的知道这些对象都具备某些功能就可以了，这极大地降低了使用者的使用难度。
2. 归一化使得高层的外部使用者可以不加区分的处理所有接口兼容的对象集合
2.1：就好象linux的泛文件概念一样，所有东西都可以当文件处理，不必关心它是内存、磁盘、网络还是屏幕（当然，对底层设计者，当然也可以区分出“字符设备”和“块设备”，然后做出针对性的设计：细致到什么程度，视需求而定）。
2.2：再比如：我们有一个汽车接口，里面定义了汽车所有的功能，然后由本田汽车的类，奥迪汽车的类，大众汽车的类，他们都实现了汽车接口，
     这样就好办了，大家只需要学会了怎么开汽车，那么无论是本田，还是奥迪，还是大众我们都会开了，开的时候根本无需关心我开的是哪一类车，操作手法（函数调用）都一样

\3. 模仿interface
在python中根本就没有一个叫做interface的关键字，如果非要去模仿接口的概念
可以借助第三方模块：
http://pypi.python.org/pypi/zope.interface
twisted的twisted\internet\interface.py里使用zope.interface
文档 https://zopeinterface.readthedocs.io/en/latest/
设计模式：https://github.com/faif/python-patterns

 

\4. 使用继承实现归一化
继承的两种用途
一：继承基类的方法，并且做出自己的改变或者扩展（代码重用）
二：声明某个子类兼容于某基类，定义一个接口类（模仿java的Interface），接口类中定义了一些接口名（就是函数名）且并未实现接口的功能，子类继承接口类，并且实现接口中的功能
实践中，继承的第一种含义意义并不很大，甚至常常是有害的。因为它使得子类与基类出现强耦合。
继承的第二种含义非常重要。它又叫“接口继承”。
接口继承实质上是要求“做出一个良好的抽象，这个抽象规定了一个兼容接口，使得外部调用者无需关心具体细节，可一视同仁的处理实现了特定接口的所有对象”——这在程序设计上，叫做归一化。
class Interface:       # 定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
    def read(self):    # 定接口函数read
        pass

    def write(self):   # 定义接口函数write
        pass

class Txt(Interface):  # 文本，具体实现read和write
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的写方法')

class Sata(Interface): # 磁盘，具体实现read和write
    def du(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的写方法')

class Process(Interface):
    def read(self):
        print('进程数据的读取方法')

    def xie(self):
        print('进程数据的写方法')

t=Txt()
s=Sata()
p=Process()

t.read()
s.read() # 自己没有read方法，调用父类的。
p.read()
'''
文本数据的读取方法
进程数据的读取方法
'''


#做出一个良好的抽象
class Payment(object):
    #规定了一个兼容接口
    def pay(self):
        pass

#微信支付
class WeChatPay(object):
    def pay(self,money):
        print('微信支付了%s'%money)

#支付宝支付
class AliPay(object):
    def pay(self,money):
        print('支付宝支付了%s'%money)

#苹果支付
class ApplePay(object):
    def pay(self,money):
        print('苹果支付了%s'%money)

def pay(obj,money): # 多态
    obj.pay(money)  # obj是支付方式

weixin = WeChatPay()
alipay = AliPay()
applepay = ApplePay()
# weixin.pay(100) # 如果没有最下面这个单独的pay方法，也可以这样执行。
#调用者无需关心具体实现细节，可以一视同仁的处理实现了特定接口的所有对象
pay(weixin,100)
pay(alipay,200)
pay(applepay,300)
'''
微信支付了100
支付宝支付了200
苹果支付了300
'''
# 上面的代码只是看起来像接口，其实并没有起到接口的作用，子类完全可以不用去实现接口 ，这就用到了抽象类。