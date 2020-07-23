\一、什么是闭包？
# 闭包函数定义：定义在函数内部的函数，
# 特点是：包含对外部作用域(局部作用域)而不是对全局作用域名字的引用，该函数就称之为闭包函数
def counter():
    n=0
    def incr():
        nonlocal n # nonlocal 表示使用外部 但非全局作用域的名字
        x=n
        n+=1
        return x
    return incr

c=counter()
print(c())
print(c())
print(c())
print(c.__closure__[0].cell_contents) # 查看闭包的元素

# 以下就是闭包函数，打印的x在函数局部作用域就可以找到，不需要去全局找。
x=1
def outter():
    x=2
    def inner():
        print(x)
    return inner # 返回inner函数是为了打破层级限制，使inner函数可以在全局调用。

f=outter() # 此时f指向的就是inner函数，还包着一层外层作用域x=2

def f1():
    x=1000000000
    f()  # 这个函数的x依然是2，函数的调用关系在定义函数时就已经固定了。

f1()

\二、闭包的意义与应用
# 闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域的名字引用
# 应用领域：延迟计算（原来我们是传参，现在我们是包起来）

from urllib.request import urlopen

# 函数体内部需要一个变量，有两种解决方案
# 一种是：以参数的形式传入，每次都要传参，太low。
def get(url):
    return urlopen(url).read()

get('http://www.baidu.com')
get('http://www.baidu.com')
get('http://www.baidu.com')

# 另外一种：用闭包的方式包起来
def get(url): # url='http://www.baidu.com'，将inner函数封装成get函数的内部函数。将get函数的url包给了inner函数使用
    # url='http://www.baidu.com'
    def inner():
        return urlopen(url).read()
    return inner  # return 将inner函数返回，在全局作用域就可以调用inner函数了，打破层级限制。

baidu=get('http://www.baidu.com')
print(baidu) # 可以看到它是get函数的内部函数
res=baidu() 
baidu()
baidu()
baidu()
baidu()



def get(x,y):
    def inner():
        print(x,y)
    return inner # 用于打破层级限制

baidu=get('a','b')

# 证明baidu函数中包了x和y
print(baidu.__closure__)                  # (<cell at 0x106433fd8: str object at 0x1030b07a0>, <cell at 0x10653a108: str object at 0x103076768>)
print(baidu.__closure__[0].cell_contents) # 取到a
print(baidu.__closure__[1].cell_contents) # 取到b



x,y=1,2
def get():
    y=111111 # 这样就是闭包函数了，只不过只包了一个值。没有y的话就不是闭包函数了，下面的__closure__就会是None。
    def inner():
        print(x,y)
    return inner # 用于打破层级限制

baidu=get()
print(baidu.__closure__) # 可以看到只有一个值，查看被闭包的参数
print(baidu.__closure__[0].cell_contents) # 111111