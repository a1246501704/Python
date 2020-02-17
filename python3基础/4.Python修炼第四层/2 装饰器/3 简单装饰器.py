
\装饰器就是闭包函数的一种应用场景

\1、为什么要用装饰器：
    开放封闭原则: 对扩展是开放的，对修改是封闭的。

\2、什么是装饰器
    - 作用: 用来装饰它人，装饰器本身可以是任意可调用对象，被装饰器的对象也可以是任意可调用对象.
    - 遵循的原则: 1、不修改被装饰对象的源代码 2、不修改被装饰对象的调用方式.
    - 目标: 在遵循原则1和2的前提，为被装饰器对象添加上新功能.

\装饰器语法
# 被装饰函数的正上方，单独一行。会将被装饰对象当作参数传给装饰器，在赋值给一个和被装饰对象同名的函数。
        @deco1
        @deco2
        @deco3
        def foo():
            pass

        foo=deco1(deco2(deco3(foo)))

\3、装饰器的使用（在被装饰对象的正上方@xxxx写上装饰器名字）
# 统计index函数的运行时间
import time

# 将统计index函数的运行时间,定义成一个功能函数(可以使用pycharm断点来看执行过程)

# 简单装饰器-low版本
def timmer(func):
    # func=index # func就是最原始的index函数的内存地址，加括号就能运行。
    def inner(): # inner这个闭包函数包裹着上层作用域中的func函数
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
    return inner

def index():
    time.sleep(3)
    print('welcome to index page')

index=timmer(index) # 调用方式不能变，括号中的index是最原始的index。（使用这行也可以实现装饰器）
index() # 调用时已经是被装饰过的index函数了，执行的是inner函数。先执行timmer函数，在inner函数
'''
welcone ti index page
run time is : 3.004794120788574
'''

# 装饰器语法-正确方式
def timmer(func):
    # func=index # func就是最原始的index函数的内存地址，加括号就能运行。
    def inner(): # inner这个闭包函数包裹着上层作用域中的func函数
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
    return inner

@timmer # 实际就是上面的index=timmer(index)。将正下方的index函数名当作参数传给了timmer函数再赋值给新得index函数。
def index():
    time.sleep(3)
    print('welcome to index page')

index() # 调用时已经是被装饰过的index函数了，执行的是inner函数。先执行timmer函数，在timmer函数
'''
welcone ti index page
run time is : 3.004794120788574
'''










