# Python装饰器（decorator）在实现的时候，有一些细节需要被注意。
# 例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）
# 所以，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
# 写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的所有属性和名称和docstring。


\无参装饰器（调用timmer装饰器函数时没传参）
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs) # 最原始foo的返回值
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

@timmer
def foo():
    time.sleep(3)
    print('from foo')
foo()



\装饰器修订
import time
from functools import wraps # 让inner函数看起来和原函数一模一样，在内部函数的正上方。会将func函数内置的 python属性原封不动的赋值给inner函数。

def timmer(func):
    @wraps(func) # 代替下方的 inner.__doc__=func.__doc__
                 # 加在最内层函数正上方，使用wraps函数可以省去__doc__的操作，不仅如此还会将python内置给index函数的属性原封不动的赋值给inner函数。
    def inner(*args,**kwargs):   # *args,**kwargs来处理home函数的参数问题，因为index函数执行时没有参数，而home函数有。
        start_time=time.time()
        res=func(*args,**kwargs) # 最原始index函数的return的返回值，*和**是inner函数怎么接过来怎么传来得。
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
        return res # 处理原始(index和home)函数的return返回值
    # inner.__doc__=func.__doc__  # 保证原始函数的注释信息不丢。
    return inner

@timmer  # 无参装饰器，直接@的。有参装饰器是@timmer('xxx')的形式
def index():
    '''
    index function  
    :return:
    '''
    time.sleep(3)
    print('welcome to index page')
    return 123

@timmer # home=timmer(home) # home=inner
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)
    return 456

res=index()      # res=inner()，无参数
print(res)

res=home('egon') # inner('egon'),有参数
print(res)

# print(index.__doc__) # 打印函数注释信息,有装饰器时查到的是None。
print(help(index))  # __doc__

