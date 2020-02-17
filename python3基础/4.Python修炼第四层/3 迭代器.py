一\迭代的概念
# 迭代器即迭代的工具，那什么是迭代呢？
    # 迭代是一个重复的过程，每次重复即一次迭代，并且每次迭代的结果都是下一次迭代的初始值

while True:           # 只是单纯地重复，因而不是迭代
    print('===>') 
    
l=[1,2,3]
count=0
while count < len(l): # 这才是迭代
    print(l[count])
    count+=1

二\为何要有迭代器？什么是可迭代对象？什么是迭代器对象？
1 什么叫迭代：迭代是一个重复过程，每次重复都是基于上一次的结果来的
2 为什么要用迭代器？
    l=['a','b','c']
    n=0
    while n < len(l):
        print(l[n])
        n+=1
    - 对于序列类型：字符串，列表，元组，可以使用基于索引的迭代取值方式。
    - 而对于没有索引的类型，如字典，集合、文件，这种方式不再适用，于是我们必须找出一种能不依赖于索引的取值方式，这就是迭代器。

3 可迭代的对象：只要对象内置有__iter__方法，如 obj.__iter__ 就是可迭代对象。
4 迭代器对象：对象既内置有__iter__方法，又内置有__next__，如文件对象。就是迭代器对象。

\注意1: 可迭代对象不一定是迭代器对象，而迭代器对象一定是可迭代的对象。
\注意2: 为可迭代对象执行完__iter__方法后拿到的对象就有__next__方法了，也就变成迭代器对象了。实现了统一标准。

# 可迭代的对象（字符串、列表、元组、字典、集合），只有__iter__方法没有__next__方法。
'hello'.__iter__  
[1,2].__iter__    
(1,2).__iter__    
{'a':1}.__iter__  
{1,2,3}.__iter__  

# 既是可迭代对象，又是迭代器对象。（文件）
open('a.txt','w').__iter__
open('a.txt','w').__next__

三\迭代器对象的使用
# 迭代器对象执行__iter__得到的仍然是它本身
dic={'a':1,'b':2,'c':3}
iter_dic=dic.__iter__() # 执行可迭代对象iter方法得到迭代器对象，迭代器对象即有__iter__又有__next__，但是：迭代器.__iter__()得到的仍然是迭代器本身
iter_dic.__iter__
iter_dic.__next__       # 可迭代对象执行__iter__方法就有__next__方法了。变成了迭代器对象。
print(iter_dic.__iter__() is iter_dic) # True


f=open('a.txt','w')
print(f is f.__iter__())  # True


# 迭代器对象的用处（用处: 不依赖索引取值）
dic={'a':1,'b':2,'c':3}
iter_dic=dic.__iter__()

print(iter_dic.__next__()) # __next__一次取一个值，等同于next(iter_dic),python内置有个next函数效果一样。取a
print(next(iter_dic))      # 等同于内置方法next(iter_dic)，取b
print(next(iter_dic))      # 等同于next(iter_dic)，取c
print(next(iter_dic))      # 报错StopIteration，表示取完了。可以使用try做异常处理。

# 文件也可以
with open('a.txt','r') as f:
    print(next(f))   # 每次取一行内容
    print(next(f))
    print(next(f))


l=[1,2,3,4,5]
iter_l=l.__iter__()
print(iter_l) # 迭代器对象内存地址
print(next(iter_l))
print(next(iter_l))
print(next(iter_l))

# 有了迭代器，我们就可以不依赖索引迭代取值了
iter_dic=dic.__iter__()
while True:
    try: # 异常处理，把可能抛出异常的代码缩进到try下面。
        k=next(iter_dic)
        print(dic[k])
    except StopIteration:  # try配合except检测如果抛出StopIteration异常代码，就执行break。
        break
# 这么写太丑陋了，需要我们自己捕捉异常，控制next，python这么牛逼，能不能帮我解决呢？能，请看for循环

四\for循环
# 基于迭代器对象的迭代取值（不依赖索引）
dic={'a':1,'b':2,'c':3}
iter_dic=dic.__iter__()
# obj=range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
# range函数是可迭代对象
# l=list(obj)  # 不要执行
print(next(iter_dic)) # 取到的是key
print(next(iter_dic))
print(next(iter_dic))

for i in dic: # iter_dic=dic.__iter__()，in后面跟一个可迭代对象
    print(i)
# for循环的工作原理:
    # 1：执行in后对象的dic.__iter__()方法，得到一个迭代器对象iter_dic
    # 2: 执行next(iter_dic),将得到的值赋值给i,然后执行循环体代码
    # 3: 重复过程2，直到捕捉到异常StopIteration,自动结束循环。

五\迭代器的优缺点
迭代器的优缺点：
    - 优点：
        提供了一种统一的迭代取值方式，该方式不再依赖于索引
        更节省内存

    - 缺点：
        无法统计长度（只有在next完毕才知道到底有几个值）
        一次性的，只能往后走，不能往前退，无法获取指定位置的值


\补充
# 导入collections.abc模块下面的Iterable（是否为可迭代对象，返回True和False）
# Iterator（是否为迭代器对象，返回True和False）两个模块，可以使用isinstance方法来判断是不是可迭代对象或是不是迭代器对象。
from collections.abc import Iterable,Iterator

print(isinstance('hello',Iterable))
print(isinstance('hello',Iterator))
