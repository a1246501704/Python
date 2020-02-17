# issubclass(子类，父类)
# 判断A是不是B的父类
class A:pass
class B(A):pass
print(issubclass(B,A)) # True

# isinstance(对象，类名)
# 判断一个对象是不是这个类的实例(子类)
b = B()
print(isinstance(b,B)) # True
print(isinstance(b,A)) # True


\什么叫反射
# 通过字符串 来反射到真实数据上
# 去访问一个字符串形式的key,再去取相对应的值
# 只要 . 点能访问的属性，都可以反射出来

# 使用字符串的形式去获取变量
a = 1
b = 2
name = input('变量名 :')
if name == 'a':
    print(a)

\使用反射来调用类中的方法和属性，对象的属性
# 使用反射调用类中的属性
class A:
    role = 'Person'
    country = 'China'
name = input('属性名: ') # 如果输入hello会报错，因为类中没有。加if判断
# getattr实现类似A.role
if hasattr(A,name):     # 类中有这个属性就返回True，没有就返回False。
    print(getattr(A,name)) # getattr去查找
'''
属性名: role  # 输入role
Person
'''

# 使用反射调用类中的属性和方法
class Person:
    role = 'Person'
    country = 'China'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def func(self):
        print('%s in func'%self.name)

alex = Person('alex',80)
# name = input('属性名 ：')
# Person.role
# alex.name  alex.age
if hasattr(alex,'name'):
    print(getattr(alex,'name')) # alex
if hasattr(alex,'func'):
    func = getattr(alex,'func') # alex in func
    func()


\反射的方法
def func2(self):
    print('%s in func2' % self.name)

# setattr设置属性和方法
alex.sex = None
setattr(alex,'sex','不详')
print(alex.sex)
setattr(alex,'func2',func2)  # setattr绑定方法是一个假的，在使用的时候必须要手动传self对象。
alex.func2(alex)
print(alex.func)

# delattr删除一个属性
delattr(alex,'name')  # 等同于 del alex.name
alex.name

\反射同样适用于模块（结合 demo1.py）
# 导入其他模块
import demo1
print(demo1.a)
print(getattr(demo1,'a'))
demo1.qqxing()
getattr(demo1,'qqxing')()

# 本模块中
a = 'aaaaa'
import sys
this_module = sys.modules[__name__] # __name__表示本模块
print(getattr(this_module,'a'))


# 反射遵循的是：a.b结构 -->反射成 getattr(a,'b')的规则
#hasattr getattr setattr delattr
#类反射 静态属性、类方法
#对象反射 方法、属性
#模块反射 函数，变量
#本模块反射 函数，变量



\反射方法
# hasattr  判断有没有
print(hasattr(f,'name'))  # f.name
print(hasattr(f,'f1'))    # f.f1
print(hasattr(f,'x'))     # f.x

# setattr 增,改
setattr(f,'age',18)  # f.age=18

# getattr 查属性  查方法
print(getattr(f,'name'))      # f.name
print(getattr(f,'name',None)) # f.name
print(getattr(f,'abc',None))  # f.abc

print(getattr(f,'f1'))
getattr(f,'f1')()

func=getattr(f,'f1') # f.f1
print(func)
func()

# delattr 删除
delattr(f,'name') # del f.name
print(f.__dict__)

\例子
class Ftpserver:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def run(self):
        while True:
            cmd=input('>>: ').strip()
            if not cmd:continue
            if hasattr(self,cmd):  
                func=getattr(self,cmd)
                func()

    def get(self):
        print('get func')

    def put(self):
        print('put func')

f=Ftpserver('192.168.1.1',21)
f.run()









