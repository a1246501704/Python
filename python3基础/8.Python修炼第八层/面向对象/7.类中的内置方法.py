现在我们来总结下所有的系统定义属性和方法， 先来看下保留属性：
>>> Class1.__doc__      # 类型帮助信息 'Class1 Doc.' 
>>> Class1.__name__     # 类型名称 'Class1' 
>>> Class1.__module__   # 类型所在模块 '__main__' 
>>> Class1.__bases__    # 类型所继承的基类 (<type 'object'>,) 
>>> Class1.__dict__     # 类型字典，存储所有类型成员信息。 <dictproxy object at 0x00D3AD70> 
>>> Class1().__class__  # 类型 <class '__main__.Class1'> 
>>> Class1().__module__ # 实例类型所在模块 '__main__' 
>>> Class1().__dict__   # 对象字典，存储所有实例成员信息。 {'i': 1234}

\类的基础方法
序号	目的	            所编写代码	  Python 实际调用
①	初始化一个实例	       x = MyClass()	x.__init__()
②	字符串的“官方”表现形式	repr(x)	         x.__repr__()
③	字符串的“非正式”值	    str(x)	        x.__str__()
④	字节数组的“非正式”值	bytes(x)	    x.__bytes__()
⑤	格式化字符串的值	format(x, format_spec)	x.__format__(format_spec)
1、对 __init__() 方法的调用发生在实例被创建 之后 。如果要控制实际创建进程，请使用 __new__() 方法。
2、按照约定， __repr__() 方法所返回的字符串为合法的 Python 表达式。
3、在调用 print(x) 的同时也调用了 __str__() 方法。
4、由于 bytes 类型的引入而从 Python 3 开始出现。

\行为方式与迭代器类似的类
序号	目的	             所编写代码	   Python 实际调用
①	遍历某个序列	         iter(seq)	  seq.__iter__()
②	从迭代器中获取下一个值	   next(seq)	seq.__next__()
③	按逆序创建一个迭代器	  reversed(seq)	seq.__reversed__()
1、无论何时创建迭代器都将调用 __iter__() 方法。这是用初始值对迭代器进行初始化的绝佳之处。
2、无论何时从迭代器中获取下一个值都将调用 __next__() 方法。
3、__reversed__() 方法并不常用。它以一个现有序列为参数，并将该序列中所有元素从尾到头以逆序排列生成一个新的迭代器。


\ __call__方法 
class A:
    def __call__(self, *args, **kwargs):
        print('aaaaaaaa')

a = A()() # 打印aaaaaaaa
# a() # 打印aaaaaaaa,直接调用A类

\__init__初始化方法
\ __new__构造方法
class A:
    def __init__(self):     # 初始化方法
        self.x = 1
        print('in init function')
    def __new__(cls, *args, **kwargs):  # 构造方法
        print('in new function')
        return object.__new__(A, *args, **kwargs) # 传类
a = A()   #在用A类实例化对象时，先调用__new__方法先构造一个对象，再用__init__初始化属性
'''
in new function
in init function
'''
\__str__方法（对象被打印时触发执行 __str__）
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __str__(self): # 在对象被打印时触发执行
        return '<name:%s age:%s sex:%s>' %(self.name,self.age,self.sex)

p1=People('egon',18,'male')
p2=People('alex',38,'male')


print(p1)
print(p2)


\单例模式（从头到尾只有一个实例）不管实例化多少次，每次获取的都是同一个对象。不怎么用。
class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(A, *args, **kw)
        return cls._instance
    
    def __str__(self):
        return 'singleton 的 实例'

    def __repr__(self):
        return 'singleton repr'
one = Singleton()
two = Singleton()
print('%s'%one)
#print('%r'%one) # repr是str的备胎，%r时如果有__repr__就取它，没有取__str__。%s时取__str__。
two.a = 3
print(one.a)
print(id(one))
print(id(two))
print(one == two)
print(one is two)

#面试的时候会用，平时很少用。
#单例模式是一种设计模式
#设计模式早期只在java里使用

print('%r is somebody'%'alex') # 显示字符串真实的样子
print('%s is somebody'%'alex') # 把字符串拼进去


\面试题
#这个类有100个对象，只要name和sex相同，我就认为是相同的对象。要求对100个对象进行去重。
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __hash__(self):
        return hash(self.name+self.sex)

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:return True


p_lst = []
for i in range(84):
    p_lst.append(Person('egon',i,'male'))

print(p_lst)
print(set(p_lst))
