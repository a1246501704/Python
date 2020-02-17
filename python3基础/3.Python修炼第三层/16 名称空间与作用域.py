\一、什么是名称空间？
# 名称空间：存放名字的地方，三种名称空间，（之前遗留的问题x=1，1存放于内存中，那名字x存放在哪里呢？名称空间正是存放名字x与1绑定关系的地方）
'''
名称空间：存放名字与值绑定关系的地方


内置名称空间：
    存放的是：内置的名字与值的绑定关系(print、len)
    生效：python解释器启动
    失效：Python解释器关闭

全局名称空间
    存放的是：py文件级别定义的名字与值的绑定（变量）
    生效：执行python文件时，将该文件级别定义的名字与值的绑定关系存放起来
    失效：文件执行完毕

局部名称空间
    存放的是：函数内部定义的名字与值的绑定关系
    生效：调用函数时，临时生效
    失效：函数调用结束
'''

\二、名称空间的加载顺序
'''
加载顺序：先内置名称空间 --> 再全局名称空间 --> 最后局部名称空间

python test.py
#1、python解释器先启动，因而首先加载的是：内置名称空间
#2、执行test.py文件，然后以文件为基础，加载全局名称空间
#3、在执行文件的过程中如果调用函数，则临时产生局部名称空间
'''

\三、名字的查找顺序
'''
查找名字的顺序：先局部名称空间 --> 再全局名称空间 --> 最后内置名称空间
'''
# 需要注意的是：在全局无法查看局部的，在局部可以查看全局的，如下示例

# max=1
def f1():
    # max=2
    def f2():
        # max=3
        print(max) # 局部虽然可以读到全局的max变量，但是如果要想修改需要在局部作用域中使用global max声明为全局变量。
    f2()
f1()
print(max)

\四、作用域

# 1、作用域即范围
#         - 全局作用域范围（包含内置名称空间与全局名称空间属于该范围）：全局存活，全局有效。
# 　      - 局部作用域范围（包含局部名称空间属于该范围）：临时存活，局部有效。

# 2、作用域关系是在函数定义阶段就已经固定的，与函数的调用位置无关，如下
x=1
def f1():
    def f2():
        print(x)
    return f2
x=100
def f3(func):
    x=2
    func()
x=10000
f3(f1())

\查看作用域：globals(),locals()

LEGB      # 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
locals()  # 是函数内的名字空间，包括局部变量和形参
enclosing # 外部嵌套函数的名字空间（闭包中常见）f3上层的f2那层的名字空间
globals() # 全局变量，函数定义所在模块的名字空间
builtins  # 内置模块的名字空间

作用域关系，在函数定义时就已经固定
于调用位置无关，在调用函数时，必须必须必须
回到函数原来的定义的位置去找作用域关系


\global与locals关键字
x=1011111111111111111111111111111111111111111
def f1(a):
    y='fffffffffffffffffffffffffffffff1'
    print(locals())  # 查看局部作用域中的名字,a也是f1的locals中的名字
    print(globals()) # 查看全局作用域中的名字

print(locals())
print(globals())
print(dir(globals()['__builtins__'])) # dir可以查看内部名称空间的名字
print(locals() is globals())

f1(12321312312312312312312312312312312312313213)

'''
#作用域关系，在函数定义时，就已经固定了，与调用位置无关
'''

x=10000000000000000000000000
def f1():
    print(x)
    def f2():
        # x='123123123123123123123123123123123'
        print(x)
    return f2   # 通过将f2函数返回，可以跨层级调用函数。

f=f1()
# print(f) # 可以看到是f1内部的f2，f()调用的是f1内部的f2函数

def func():
    x=123
    f()   # 在这里调f函数要到f函数定义的位置的层级关系中去找x的值。
x='hello' # 在func之前修改x的值f2中的x就是hello,因为f2是f1中return的函数。而在f1中打印x还是全局的x的值
func()




\闭包函数：
#1. 定义在函数内部的函数
#2. 包含对外部作用域名字的引用，而不是对全局作用域名字的引用,那么该内部函数就称为闭包函数.
闭包函数  了解
global与nonlocal关键字

什么是闭包
    #内部函数包含对外部作用域而非全局作用域的引用
    #提示：之前我们都是通过参数将外部的值传给函数，闭包提供了另外一种思路，包起来喽，包起呦，包起来哇
def counter():
    n=0
    def incr():
        nonlocal n
        x=n
        n+=1
        return x
    return incr

c=counter()
print(c())
print(c())
print(c())
print(c.__closure__[0].cell_contents) #查看闭包的元素

闭包的意义与应用
    #闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域
    #应用领域：延迟计算（原来我们是传参，现在我们是包起来）
from urllib.request import urlopen

def index(url):
    def get():
        return urlopen(url).read()
    return get

baidu=index('http://www.baidu.com')
print(baidu().decode('utf-8'))

\global、nonlocal关键字

# 互相不冲突 1是全局  10是局部
x=1
def f1():
    x=10
f1()
print(x) # 1

# global声明全局： 指定局部变量,为全局变量.
x=1
def f1():
    global x
    x=10
f1()
print(x) # 10

# nonlocal会在本函数里面找往上层找变量，一层一层找，如果函数内部所有层级都没有找到 就报错。但不会去全局找。
x=1
def f1():
    x=2 # nonlocal改的是这样的x，在函数内部一层一层找。
    def f2():
        nonlocal x
        x=111111
    f2()
    print(x) 

f1()








