一\什么是匿名函数？
# 匿名就是没有名字

# 有名函数
def func(x,y,z=1):
    return x+y+z

# 匿名函数
lambda x,y,z=1:x+y+z #与函数有相同的作用域，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字.
func=lambda x,y,z=1:x+y+z 
func(1,2,3)
#让其有名字就没有意义了，还不如直接写有名函数。要的就是没名字的。

二\有名字的函数与匿名函数的对比
# 有名函数与匿名函数的对比
    # 有名函数：循环使用，保存了名字，通过名字就可以重复引用函数功能
    # 匿名函数：一次性使用，随时随时定义。自带return。仅仅只能取代简单的函数场景。

def f1(n):
    return n**2

# f1(3)
print(f1)


f2=lambda n:n**2 # 给了名字就多此一举了
print(f2) # <function <lambda> at 0x101f2c1e0>
print(f2(3))

lambda n:n**2  # 匿名还输自带return

\匿名函数即没有绑定名字的函数，没有绑定名字，意味着只能用一次就会被回收，所以说匿名函数的应用场景就是：某个功能只用一次就结束了。

\应用：max，min，sorted,map,reduce,filter
案例：取出工资最高的人名，下面是几种实现方式。
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
\max ：光凭 max 无法实现
print(max(salaries))          # yuanhao ，max默认比较的是字典的key，从首字母依次对比。
print(max(salaries.values())) # 100000000， 取value来比较工资

\拉链函数（zip=拉锁）+ max实现
l1=[1,2,3]
s1='hello'

res=zip(l1,s1)   # 遵循迭代器规则，1和h一组，2和e，3和l。剩下的丢弃。
print(list(res)) # [(1, 'h'), (2, 'e'), (3, 'l')]，多余的就丢弃了。

# 用拉链来处理工资对比
res=zip(salaries.values(),salaries.keys())  # 元组比较，把key和value颠倒后对比数字后打印人名。
# res=list(zip(salaries.values(),salaries.keys())) # 列表比较
print(max(res)[1]) # alex

\补充：两个元组比较大小（t1是否小于t2）
t1=(3333,'a')
t2=(2,'a','b','c')
print(t1 < t2) # False，两个元组比较比的不是长度。依次比较每个个元素大小，如果第一个就分胜负了，就没比较比后面的了。

\max与lambda的结合实现
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# def f1(k):
#     return salaries[k]
#
# print(max(salaries,key=f1)) # 此处的key并不是字典的key，而是max功能中的关键字key。将每次从salaries中迭代出来的值当作参数传给key后面指定的功能函数。
#                             # 函数中的功能来改变max的比较依据。只是比较依据变了，最终的结果还是字典的key，因为迭代是什么最终的结果就是什么。

\使用max结合lambda结合实现
print(max(salaries,key=lambda k:salaries[k])) # alex ,max每迭代一次后得到的值给key后面的一个函数或方法，然后取值来比较。
print(min(salaries,key=lambda k:salaries[k])) # yuanhao
\排序
print(sorted(salaries,key=lambda k:salaries[k])) # ['yuanhao', 'egon', 'wupeiqi', 'alex']
print(sorted(salaries,key=lambda k:salaries[k],reverse=True)) # reverse：反转结果 , ['alex', 'wupeiqi', 'egon', 'yuanhao']


\map(映射),reduce（合并）,filter(过滤器)（都遵循迭代器协议、把可以迭代对象放在最后面，就是l。）

\map :map()它接收一个函数 l 和一个 可迭代对象(这里理解成 list)，并通过把函数 l 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
l=['alex','wupeiqi','yuanhao','huanghongwei']
map(lambda x:x+'_SB',l)
print(list(map(lambda x:x+'_SB',l))) # ['alex_SB', 'wupeiqi_SB', 'yuanhao_SB', 'huanghongwei_SB']

\reduce :reduce()函数作用是先取两个值做运算，然后把结果继续和序列的下一个元素做累积计算。
from functools import reduce
print(reduce(lambda x,y:x+y,range(1,101),100)) # 结果：5150。100是随便写的初始值，可以没有。

\filter : filter()函数用于过滤序列,和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
l=['alex_SB','wupeiqi_SB','yuuanhao_SB','hhw','egon']
res=filter(lambda name:name.endswith('SB'),l) # 过滤结尾包含SB，匹配到的保留。
print(list(res)) # ['alex_SB', 'wupeiqi_SB', 'yuuanhao_SB']

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

\四个用法
由于lambda语法是固定的，其本质上只有一种用法，那就是定义一个lambda函数。在实际中，根据这个lambda函数应用场景的不同，可以将lambda函数的用法扩展为以下几种：

# 将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1,2)，输出为3。

# 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：
time.sleep=lambda x:None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。

# 将lambda函数作为其他函数的返回值，返回给调用者。
函数的返回值也可以是函数。例如return lambda x, y: x+y返回一个加法函数。
这时，lambda函数实际上是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量，这个特性是闭包(Closure)编程的基础，在这里我们不展开。

# 将lambda函数作为参数传递给其他函数。
部分Python内置函数接收函数作为参数。典型的此类内置函数有这些。
filter函数。此时lambda函数用于指定过滤列表元素的条件。
    例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。
sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。
    例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。
map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。
    例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。
reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。
    例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。














