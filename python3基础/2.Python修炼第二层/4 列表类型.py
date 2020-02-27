列表是Python中最基本的数据结构，列表是最常用的Python数据类型，列表的数据项不需要具有相同的类型。
列表中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

# 作用：多个装备，多个爱好，多门课程，多个女朋友等
# 定义：[]内可以有多个任意类型的值，逗号分隔
# 可以存多个值、值可以是任意类型、有序（索引）、可变（id不变的情况下值可变）

\列表方法
list.append # 追加
list.insert # 插入
list.extend # 追加列表
list.count  # 统计个数
list.pop    # 从末尾删除，返回值。
list.remove # 按值删除，无返回值。
list.reverse # 列表值反转
list.index  # 查找索引
list.sort   # 排序
list.clear  # 清除列表


#       索引        0        1         2     3 4                   
my_girl_friends=['alex','wupeiqi','yuanhao',4,5] # 本质 my_girl_friends=list([...])

\优先掌握的操作：
# 按索引存取值(正向存取+反向存取): 即可存也可以取
print(my_girl_friends[2])  # 正取
print(my_girl_friends[-1]) # 反取
print(id(my_girl_friends))

# 修改
print(id(my_girl_friends))
my_girl_friends[0]='SB' # 用字符串或变量修改,修改的就是原始列表
print(my_girl_friends[0])
print(id(my_girl_friends))  # 值变id不变，说明列表属于可变类型。
print(my_girl_friends)

# 切片(顾头不顾尾，步长)
print(my_girl_friends[0:2])
print(my_girl_friends[0:4:2])
a=[1,2,3,4,5,6]
print(a[0:-1:2]) # 输出 [1, 3, 5]，索引位置（121212，把1的都取出来。）

# 成员运算 in 和 not in: 返回True和False
print('alex' in my_girl_friends)
print(5 in my_girl_friends)

# 追加: append,默认追加到最后
my_girl_friends.append('6号')
print(my_girl_friends)

# 扩展，extend: 以列表的形式一次添加多个值到原始列表的最后面。
my_girl_friends.extend([1,2,3,4])
print(my_girl_friends)
'''
['alex', 'wepeiqi', 'yuanhao', 4, 5,'6号', 1, 2, 3, 4]
'''

# 插入，insert: 指定索引位置插入
my_girl_friends.insert(0,'sb_alex')
my_girl_friends.insert(2,'yh')
'''
['sb_alex', 'alex', 'wepeiqi', 'yuanhao', 4, 5]
['sb_alex', 'alex', 'yh', 'wepeiqi', 'yuanhao', 4, 5]
'''

# 删除: del，通用方法，和列表无关。可以删列表也可以删字符串。按照索引删除。
del my_girl_friends[2]
print(my_girl_friends)
del my_girl_friends[0:2]
print(my_girl_friends)

# remove: 按照值删除（没有返回值）
my_girl_friends.remove('yuanhao')
print(my_girl_friends)
print(my_girl_friends.remove('yuanhao')) # remove是单纯的删除，并且是按照值去删，不会返回删除的值。

# pop: 按索引删除（返回删除的值）
res=my_girl_friends.pop(1)     # 按照索引取删，不指定索引默认从末尾开始删,print可以返回取走的值。
print(res)
print(my_girl_friends.pop())   # 按照索引取删，默认从末尾开始删.
print(my_girl_friends)

# 统计长度: 按照列表值个数计算长度
print(len(my_girl_friends))

# count: 统计个数
print(my_girl_friends.count('alex'))
print(my_girl_friends)

# clear: 清空列表
my_girl_friends.clear()
print(my_girl_friends)

# copy: 复制一个新列表
l=my_girl_friends.copy()
print(l)

# index: 用于从列表中找出某个值第一个匹配项的索引位置。
print(my_girl_friends.index('wepeiqi')) # 1

# reverse: 列表内容反转（前后顺序颠倒）
my_girl_friends.reverse()
print(my_girl_friends)
'''
[5, 4, 'yuanhao', 'wupeiqi', 'alex']
'''
l=[3,4,-1,2]
l.sort
print(l)

# sort: 排序
l=[3,4,-1,2]
l.sort() # 从小到大,不能和print放在一行写
print(l)
l.sort(reverse = True)  # 将排序后的结果反转
print(l)
'''
[-1, 2, 3, 4]
[4, 3, 2, -1]
'''
# 有如下列表，请按照年龄排序（涉及到匿名函数）
l=[
    {'name':'alex','age':84},
    {'name':'oldboy','age':73},
    {'name':'egon','age':18},
]
l.sort(key=lambda item:item['age']) # 
print(l)
'''
[{'name': 'egon', 'age': 18}, {'name': 'oldboy', 'age': 73}, {'name': 'alex', 'age': 84}]
'''

# 去除重复、去重
比较容易记忆的是用内置的set
l1 = ['b','c','d','b','c','a','a'] 
l2 = list(set(l1)) 
print(l2)

还有一种据说速度更快的，没测试过两者的速度差别
l1 = ['b','c','d','b','c','a','a'] 
l2 = {}.fromkeys(l1).keys() 
print(l2)

这两种都有个缺点,去除重复元素后排序变了：
['a', 'c', 'b', 'd']

如果想要保持他们原来的排序：
用list类的sort方法
l1 = ['b','c','d','b','c','a','a'] 
l2 = list(set(l1)) 
l2.sort(key=l1.index) 
print(l2)

也可以这样写
l1 = ['b','c','d','b','c','a','a'] 
l2 = sorted(set(l1),key=l1.index) 
print(l2)

也可以用遍历
l1 = ['b','c','d','b','c','a','a'] 
l2 = [] 
for i in l1: 
if not i in l2: 
        l2.append(i) 
print(l2)

上面的代码也可以这样写

l1 = ['b','c','d','b','c','a','a'] 
l2 = [] 
[l2.append(i) for i in l1 if not i in l2] 
print(l2)
这样就可以保证排序不变了：['b', 'c', 'd', 'a']

\循环
方法一：最简单常用的，用for遍历列表
list = [2, 3, 4]
for num in list:
    print (num)

方法二：利用python内置函数enumerate（）列举出list中的数
enumerate(sequence, [start=0])，返回枚举对象

参数
    sequence -- 一个序列、迭代器或其他支持迭代对象。
    start -- 下标起始位置。

list = [2, 3, 4]
for i in enumerate(list):
    print （i）

方法三：使用iter（）迭代器
iter(object[, sentinel]) 函数用来生成迭代器，返回迭代对象。
参数
    object -- 支持迭代的集合对象。
    sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。

用法实例
list = [2, 3, 4]
for i in iter(list):
    print (i)

方法四：使用range（）函数
pytho range(start, stop[, step]) 函数返回类型是ndarray，可用list（）返回一个整数列表，一般用在 for 循环中。

参数
    start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
    end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
    step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
用法实例
list = [2, 3, 4]
for i in range(len(list)):
    print i,list[i]
    
\练习:
# 队列（吃了拉）：先进先出,用列表模拟队列
append，pop
l1=[]
l1.append('1')
l1.append('2')
l1.append('3')
print(l1)
print(l1.pop(0)) # 如果不指定第0个，就是先进后出了。
print(l1.pop(0))
print(l1.pop(0))
'''
['1', '2', '3']
1
2
3
'''
l1=[]
l1.insert(0,'1') 
l1.insert(0,'2')
l1.insert(0,'3')
print(l1)
print(l1.pop())
print(l1.pop())
print(l1.pop())
'''
['3', '2', '1']
3
2
1
'''
# 堆栈（吃了吐）：先进后出,用列表模拟堆栈
l1=[]
l1.append('1')
l1.append('2')
l1.append('3')
print(l1)
print(l1.pop())
print(l1.pop())
print(l1.pop())
'''
['1', '2', '3']
3
2
1
'''
l1=['a']
l1.insert(0,'1')
l1.insert(0,'2')
l1.insert(0,'3')
print(l1)
print(l1.pop(0))
print(l1.pop(0))
print(l1.pop(0))
print(l1.pop(0))
'''
['3', '2', '1', 'a']
3
2
1
a
'''

\列表推导式
#用循环生成列表
values = [10, 21, 4, 7, 12]
squares = []

for x in values:
    squares.append(x**2)
print(squares)     # [100, 441, 16, 49, 144]

#简化
values = [10, 21, 4, 7, 12]
squares = [x**2 for x in values]
print(squares)     # [100, 441, 16, 49, 144]

#还可以在列表推导式中加入条件进行筛选。
squares = [x**2 for x in values if x <= 10] 
print(squares)     # [100, 16, 49]

#也可以使用推导式生成集合和字典：
square_set = {x**2 for x in values if x <= 10}
print(square_set)           
set([16, 49, 100])
square_dict = {x: x**2 for x in values if x <= 10}
print(square_dict)  # {10: 100, 4: 16, 7: 49}

#求和
total = sum([x**2 for x in values if x <= 10])
#但是，Python会生成这个列表，然后在将它放到垃圾回收机制中（因为没有变量指向它），这毫无疑问是种浪费。
#为了解决这种问题，与xrange()类似，Python使用产生式表达式来解决这个问题：
total = sum(x**2 for x in values if x <= 10)
#只是去掉了括号，但这里并不会一次性的生成这个列表。
dataa = [(f, os.stat(f)) for f in glob.glob('*test*.py')]



