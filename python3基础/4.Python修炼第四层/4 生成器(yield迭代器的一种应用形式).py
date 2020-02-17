\生成器定义
    定义：只要函数内部出现yield关键字，那么在调用该函数，将不会立即执行函数体yield后面的代码，会得到一个结果该结果就是生成器对象。
    好处：可以被for循环统一迭代、省内存。


def func():
    print('===>first')
    yield 1  # 也可以返回其他类型的值
    print('===>second')
    yield 2
    print('====>third')
    yield 3

g=func()   # func函数不会执行里面的代码，而是会得到一个结果。这个结果就是生成器对象。
print(g)   # <generator object func at 0x0000000002184360> ，得到一个生成器
g.__iter__ # 既有__iter__方法
g.__next__ # 也有__next__方法。所以说生成器本质就是迭代器。使用yield关键字把函数执行结果制作成迭代器(自定义迭代器)。
res=next(g)# 每次next(g)都会执行到下一个yield，1、2、3是每次next后的返回值。就好比上一次执行完暂停了一样。
print(res) 
'''
===>first
1
'''
res=next(g)
print(res)  # 同等于print(next(g))
'''
===>second
2
'''

# 生成器本质就是迭代器
print(next(g))  # yield 1有return返回值功能，也可以返回多个值。return只能执行一次，而yield可以返回多次。
print(next(g))
print(next(g))
print(next(g))  # 已经取没了，会报错。


# 错误用法，这样每次得到的都是1
print(next(func()))
print(next(func()))
print(next(func()))

# 可以被for循环迭代:
for i in g: # 执行for循环会先为g执行__iter__方法变为迭代器对象。
    print(i)

for i in g: # 循环一次就取没了
    print(i)

g=func()    # 如果想要多次使用，需要再赋依次值。
for i in g:
    print(i)


\yield的功能：
    - 为我们提供了一种自定义迭代器的方式（把函数做成迭代器）
    - 对比return，可以返回多次值，可以挂起/保存函数的运行状态


# 自定义功能，可以生成无穷多个值，因为同一时间在内存中只有一个值
def my_range(start,stop,step=1):
    while start < stop:
        yield start
        start+=step

g=my_range(1,5,2) # 1到5，顾头不顾尾1-4，步长为2.取到1和3。
print(next(g))
print(next(g))
print(next(g)) # 步长为2是，就两个值。到这行就没值了。
print(next(g))
print(next(g)) # 不指定步长时是4个值，到这行就没值了。

for i in my_range(1,10000000000000000000000000,step=2):
    print(i)




\案例：使用生成器实现Linux系统中tail -f access.log | grep '404'的功能，tail及时处理过的每行的数据立即交给grep处理。

\yield用法1: 使用yield将函数的执行结果做成生成器，配合test.py测试

import time
# 自定义“查看文件最后一行”功能的生成器
def tail(filepath):
    with open(filepath,'rb') as f:
        f.seek(0,2)  # seek移动光标，倒着seek，模式为2.
        while True:
            line=f.readline()
            if line:
                yield line # 返回数据（可以返回多次），beyts类型
            else:
                time.sleep(0.2)
# 自定义“过滤”功能的生成器
def grep(pattern,lines):
    for line in lines:
        line=line.decode('utf-8')
        if pattern in line:
            yield line      # 返回多次
# 使用，结合test.py
g=grep('404',tail('access.log')) # tail函数的结果是个生成器，当作参数传给grep函数。grep的结果也是个生成器结果赋值给g。
for line in g:  # 还可以写成作用的形式 for line in grep('404',tail('access.log')):
    print(line)



四\协程函数: yield的表达式形式的应用
\yield用法2: 使用send方法从外部给函数体内的yield关键字传值，不是给yield返回值传值。

def eater(name):
    food_list=[]
    print('%s 开动啦' %name)
    while True:
        food=yield food_list # yield=‘骨头  ----> ’food=‘骨头’ ----> 返回food_list。 函数体内也出现了yield关键字。
        print('%s 开始吃 %s' %(name,food))
        food_list.append(food)

g=eater('alex')
# next(g) # 等同于 g.send(None)
g.send(None) # send有两个功能，一个是同于next(g)功能，一个是给yield传值。但是第一次必须给传个None进行初始化，停止到yeild的位置等待send给yield传值。
print(g.send('骨头')) # 从暂停的位置（yield）往后走，把“骨头”赋值给暂停位置的yield。再将yield赋值给food。print打印了本次调用yield的返回值food_list。
print(g.send('shi')) # yield接收后继续从暂停的位置（yield）往后走,多次返回yield和while循环yield 每次都会在yield关键字处等待传值，yield或while上面的代码不会被重复执行。




# 同样的例子
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('egon')
g.send(None)    # 对于表达式形式的yield，在使用时，第一次必须传None到yield处等着，g.send(None)等同于next(g)
g.send('油焖婊子')
g.send('红烧劈腿男')
g.close()       # 关闭了生成器，下面要想能send需要重新拿到生成器g（ g=eater('egon') ）
g.send('油炸卫生纸')
g.send('芬达猪蹄')



# 利用yield可以循环返回多次值
def f1():
    while True:
        x=yield
        print(x)

g=f1()
next(g)
g.send(1)
g.send(1)
g.close() # 关闭
g.send(1)
g.send(1)
g.send(1)

