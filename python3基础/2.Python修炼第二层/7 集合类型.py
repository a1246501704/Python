pythons=['alex','wupeiqi','egon','yuanhao','gangdan','oldboy']
linuxs=['egon','oldboy','tiedan','liudan']

# 将即学python和linux的人放在一个列表中，下面用列表的方法可以实现但是太麻烦了。
l=[]
for item in pythons:
    if item in linuxs:
        l.append(item)
print(l)

\集合
# 作用: 去重，关系运算,时使用集合
# 定义:
        知识点回顾
        可变类型是不可hash类型
        不可变类型是可hash类型
# 定义集合:
        集合：可以包含多个元素，用逗号分割，无序
        集合的元素遵循三个原则：
                1：每个元素必须是不可变类型(可hash，可作为字典的key)，列表和字典是可变类型。不行
                2: 集合中没有重复的元素
                3：无序
                4：使用{}里面包含多个元素用逗号隔开
# 注意集合的目的是将不同的值存放到一起，不同的集合间用来做关系运算，无需纠结于集合中单个值.

\优先掌握的操作：
1、长度len
2、成员运算in和not in
3、| 合集（并集）
4、& 交集
5、- 差集
6、^ 对称差集
7、==
8、父集：>,>=
9、子集：<,<=

\定义一个集合
s={1,2,'a','b','c','d','e','f'} # 本质s=set({1,2,'a'})，不支持存列表，会报错。
print(type(s),s) # set类型,元素无序

# 统计长度 len
print(len(s))

# 成员运算 in 和 not in
print('a' in s)

for item in s:
    print(item)

s1={1,2,3}
s2={3,4,5}
# & 交集: 取两个集合中都有的部分
print(s1 & s2) # {3}

# - 差集: 在s1中不在s2中的、在s2中不在s1中的
print(s1 - s2) # {1, 2}
print(s2 - s1) # {4, 5}

# | 并集: 两个集合合并到一起，去掉重复。
s1={1,2,3}
s2={3,4,5}
print(s1 | s2) # {1, 2, 3, 4, 5}

# ^ 对称差集/补集: 集合间共有部分之外的部分
print(s1 ^ s2) # {1, 2, 4, 5}
\口诀: 交差并补，艾特减管尖

\练习
# 一.关系运算
# 　　如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
 　　 pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
 　　 linuxs={'wupeiqi','oldboy','gangdan'}
# 　　1. 求出即报名python又报名linux课程的学员名字集合
         print(pythons & linuxs)
# 　　2. 求出所有报名的学生名字集合
         print(pythons | linuxs)
# 　　3. 求出只报名python课程的学员名字
         print(pythons - linuxs)
# 　　4. 求出没有同时报名这两门课程的学员名字集合
         print(pythons ^ linuxs)

\集合之间的比较，返回True或False
#  ==  
# > ， >= ， <, <= 父集，子集
s1={1,2,3,4}
s2={3,4,5}
print(len(s1) > len(s2)) # 这是普通的个数比较

# s1中的值如果完全包含s2中的所有值则返回True，s1是s2的父集，s2是s1的子集。
s1={1,2,3,4}
s2={3,4}
print(s1 > s2)  # True 
print(s1 >= s2) # True

\使用方法实现，可以使用方法代替上面的符号方式。
s1={1,2,3,4}
s2={3,4,5}

# union (| 并集)
　#　一组集合的并集是这些集合的所有元素构成的集合，而不包含其他元素。
　#　使用操作符 | 执行并集操作，同样地，也可使用方法 union() 完成。
print(s1.union(s2))

# intersection、intersection_update (& 交集)
  # 两个集合 A 和 B 的交集是含有所有既属于 A 又属于 B 的元素，而没有其他元素的集合。
　#　使用 & 操作符执行交集操作，同样地，也可使用方法 intersection() 完成。
print(s1.intersection(s2))
s1.intersection_update(s2) # 完成了一个修改操作，相当于 s1=s1.intersection(s2)
print(s1)

# difference (- 差集)
  # A 与 B 的差集是所有属于 A 且不属于 B 的元素构成的集合
　#　使用操作符 - 执行差集操作，同样地，也可使用方法 difference() 完成。
print(s1.difference(s2))
s1.difference_update(s2)  # 完成了一个修改操作，相当于 s1=s1.difference(s2)

# symmetric_difference (^ 对称差集)
  # 两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合。
　# 使用 ^ 操作符执行差集操作，同样地，也可使用方法 symmetric_difference() 完成。
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)

# issuperset(父集) 、issubset（子集）
# == ,> ， >= ， <, <= 
s1={1,2,3,4}
s2={3,4}
print(s1.issuperset(s2)) # 判断s1是否是s2的父集
print(s2.issubset(s1))   # 判断s2是否是s2的子集

\常用操作
s1={1,2,3,'a',4}

# 删除
print(s1.pop())        # 随机删，并返回删除的结果。原集合元素减少。
print(s1.remove('a'))  # 单纯地删指定的元素，不会返回删除的结果，并且如果删除的元素不存在则报错。
s1.remove('asdfasdfa') # 单纯地删不存在的元素会报错，不会返回删除的结果。
print(s1)              # 原集合值减少
print(s1.discard('a')) # 单纯地删，不会返回删除的结果，并且如果删除的元素不存在返回None，不会报错。
print(s1)

# 判断
s1={1,2,3}
s2={4,5}
print(s1.isdisjoint(s2)) # 如果s1和s2没有交集则返回True

# 清空集合
s1.clear()

# 添加
s1.add('b') # 无顺序添加
print(s1)

# 去重: set
l=['a','b',1,'a','a']
print(list(set(l))) # [1, 'b', 'a'] ，使用集合去重后用list再转换成列表，转换后列表顺序会变。

# 保持顺序不变去重后放入列表(列表去重)
l=['a','b',1,'a','a']
l_new=list()
s=set()
for item in l:
    if item not in s:
        s.add(item) # 元组中已有的重复的就添加不了了。
        l_new.append(item) # 只要元组添加成功了，就说明元组中没有这个数据。顺带着就把列表的也添加了。实现了列表去重。

# 可变类型去重，列表和字典都是可变类型。用集合的特性去重，但是集合又不能添加可变类型。(字典去重)
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
] # 解决思路：key都一样，如果value都是一样的，就证明列表里的两个字典是一样的
l_new=list()
s=set()
for item in l:
    res = (item['name'], item['age'], item['sex']) # 设置判断依据，获取每个字典的所有value,把列表中的每个字典的value变成了集合。
        # print(res)
        # ('egon', 18, 'male')
        # ('alex', 73, 'male')
        # ('egon', 20, 'female')
        # ('egon', 18, 'male')
        # ('egon', 18, 'male')
    if res not in s:
        s.add(res)
        l_new.append(item) # 还是保持字典格式

print(l_new) # [{'name': 'egon', 'age': 18, 'sex': 'male'}, {'name': 'alex', 'age': 73, 'sex': 'male'}, {'name': 'egon', 'age': 20, 'sex': 'female'}]


# 去重,无需保持原来的顺序
l=['a','b',1,'a','a']
print(set(l))           # {1, 'a', 'b'}
print(list(set(l)))     # [1, 'a', 'b']

# 去重,并保持原来的顺序
# 方法一: 不用集合
l=[1,'a','b',1,'a']

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

# 方法二: 借助集合
l1=[]
s=set()
for i in l:
    if i not in s:
        s.add(i)
        l1.append(i)

print(l1)

# 同上方法二,去除文件中重复的行
import os
with open('db.txt','r',encoding='utf-8') as read_f,\
        open('.db.txt.swap','w',encoding='utf-8') as write_f:
    s=set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)
os.remove('db.txt')
os.rename('.db.txt.swap','db.txt')

# 列表中元素为可变类型时,去重,并且保持原来顺序
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
# print(set(l)) #报错:unhashable type: 'dict'
s=set()
l1=[]
for item in l:
    val=(item['name'],item['age'],item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)

print(l1)

#定义函数,既可以针对可以hash类型又可以针对不可hash类型
def func(items,key=None):
    s=set()
    for item in items:
        val=item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l,key=lambda dic:(dic['name'],dic['age'],dic['sex']))))


\集合方法
1.add 向集合中添加元素
>>> s = {1, 2, 3, 4, 5, 6}
>>> s.add("s")
>>> s # {1, 2, 3, 4, 5, 6, 's'}

2.clear 清空集合
>>> s = {1, 2, 3, 4, 5, 6}
>>> s.clear()
>>> s # set()

3.copy 返回集合的浅拷贝
>>> s = {1, 2, 3, 4, 5, 6}
>>> new_s = s.copy()
>>> new_s # {1, 2, 3, 4, 5, 6}

4.pop 删除并返回任意的集合元素（如果集合为空，会引发 KeyError）
>>> s = {1, 2, 3, 4, 5, 6}
>>> s.pop()　　# pop删除时是无序的随机删除
1
>>> s # {2, 3, 4, 5, 6}

5.remove 删除集合中的一个元素（如果元素不存在，会引发 KeyError）
>>> s = {1, 2, 3, 4, 5, 6}
>>> s.remove(3)
>>> s # {1, 2, 4, 5, 6}

6.discard 删除集合中的一个元素（如果元素不存在，则不执行任何操作）
>>> s = {1, 2, 3, 4, 5, 6}
>>> s.discard("sb")
>>> s # {1, 2, 3, 4, 5, 6}

7.intersection 将两个集合的交集作为一个新集合返回
>>> s = {1, 2, 3, 4, 5, 6}
>>> s2 = {3, 4, 5, 6, 7, 8}
>>> s.intersection(s2)  # {3, 4, 5, 6}
>>> s&s2　　# {3, 4, 5, 6}，可以达到相同的效果

8.union 将集合的并集作为一个新集合返回
>>> s = {1, 2, 3, 4, 5, 6}
>>> s2 = {3, 4, 5, 6, 7, 8}
>>> print(s.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
>>> print(s|s2)    # {1, 2, 3, 4, 5, 6, 7, 8}，用 | 可以达到相同效果

9.difference 将两个或多个集合的差集作为一个新集合返回　
>>> s = {1, 2, 3, 4, 5, 6}
>>> s2 = {3, 4, 5, 6, 7, 8}
>>> print("差集:",s.difference(s2)) # 去除s和s2中相同元素，删除s2 保留s中剩余元素
差集: {1, 2}
>>> print("差集:",s2.difference(s))　　# 去除s和s2中相同元素，删除s2 保留s2中剩余元素<br>
差集: {8, 7}
>>> print("差集:",s - s2)    # 符号 - 可以达到相同结果
差集: {1, 2}
>>> print("差集:",s2 - s)    # 符号 - 可以达到相同结果
差集: {8, 7}

10.　symmetric_difference 将两个集合的对称差作为一个新集合返回(两个集合合并删除相同部分，其余保留)　
>>> s = {1, 2, 3, 4, 5, 6}
>>> s2 = {3, 4, 5, 6, 7, 8}
>>> s.symmetric_difference(s2) # {1, 2, 7, 8}

11.update 用自己和另一个的并集来更新这个集合 
>>> s = {'p', 'y'}
>>> s.update(['t', 'h', 'o', 'n'])    # 添加多个元素
>>> s # {'p', 't', 'o', 'y', 'h', 'n'}
>>> s.update(['H', 'e'], {'l', 'l', 'o'})    # 添加列表和集合
>>> s # {'p', 'H', 't', 'l', 'o', 'y', 'e', 'h', 'n'}

12.intersection_update()  用自己和另一个的交集来更新这个集合
>>> s = {'a', 'b', 'c', 'd', 'q'}
>>> s2 = {'c', 'd', 'e', 'f'}
>>> s.intersection_update(s2)   # 相当于s = s - s2
>>> s # {'c', 'd'}

13.isdisjoint() 　如果两个集合有一个空交集，返回 True
>>> s = {1, 2}
>>> s1 = {3, 4}
>>> s2 = {2, 3}
>>> s.isdisjoint(s1)   
True                               # s  和 s1 两个集合的交集为空返回 True
>>> s.isdisjoint(s2)
False                             # s  和 s2 两个集合的交集为 2 不是空 所有返回False

14.issubset()　如果另一个集合包含这个集合，返回 True
>>> s = {1, 2, 3}
>>> s1 = {1, 2, 3, 4}
>>> s2 = {2, 3}
>>> s.issubset(s1)
True                            # 因为 s1 集合 包含 s 集合
>>> s.issubset(s2)
False                           # s2 集合 不包含 s 集合

15.issuperset() 　如果这个集合包含另一个集合，返回 True
>>> s = {1, 2, 3}
>>> s1 = {1, 2, 3, 4}
>>> s2 = {2, 3}
>>> s.issuperset(s1)
False                                        # s 集合不包含 s1 集合
>>> s.issuperset(s2)
True                                         # s 集合包含 s2 集合                                     

16.difference_update() 从这个集合中删除另一个集合的所有元素
>>> s = {1, 2, 3}
>>> s1 = {1, 2, 3, 4}
>>> s2 = {2, 3}
>>> s.difference_update(s2)
>>> s # {1} ，s2中的2,3   s集合中也有2,3  所以保留1
>>> s1.difference_update(s2)
>>> s1 # {1, 4}

\集合与内置函数
all()	# 如果集合中的所有元素都是 True（或者集合为空），则返回 True。
any()	# 如果集合中的所有元素都是 True，则返回 True；如果集合为空，则返回 False。
len()	# 返回集合的长度（元素个数）
max()	# 返回集合中的最大项
min()	# 返回集合中的最小项
sum()	# 返回集合的所有元素之和
sorted()    # 从集合中的元素返回新的排序列表（不排序集合本身）
enumerate() # 返回一个枚举对象，其中包含了集合中所有元素的索引和值（配对）。

\不可变集合
fs=frozenset({1,2,3,4})
fs.xxx # 没有添加方法