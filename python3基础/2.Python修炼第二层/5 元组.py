# 作用：存多个值，对比列表来说，元组不可变（是可以当做字典的key的），主要是用来读。
# 定义方式：与列表类型比，只不过[]换成()，如果只是用来读就用元组。
# 可存多个值、任意类型、有序、不可变

ages=(11,22,33,44,55) # 本质 age=tuple((11,22,33,44,55)),逗号’,’起决定性作用。只含有单个元素的元组容易和表达式混淆 。 a = (10,)
print(id(ages),type(ages),ages)

优先掌握的操作：
1、按索引取值(正向取+反向取)：只能取   
2、切片(顾头不顾尾，步长)
3、长度
4、成员运算 in 和 not in
5、循环


# 按索引取值(正向取+反向取)：只能取

# 切片(顾头不顾尾，步长)
print(age[0:2])  # (11, 22),产生新的元组
print(age)       # (11, 22, 33, 44, 55)

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素。
L = ('Google', 'Taobao', 'Runoob')
L[2]	# 读取第三个元素
L[-2]	# 反向读取；读取倒数第二个元素
L[1:]	# 截取元素，从第二个开始后的所有元素。
>>> L[2]
'Runoob'
>>> L[-2]
'Taobao'
>>> L[1:]
('Taobao', 'Runoob')


# 长度
print(len(ages))

# 成员运算in和not in
print(10 in ages)

# index: 元素索引
print(ages.index(22))            # 存在就返回索引位
print(ages.index(123123123123))  # 不存在就报错

# conut: 统计元素个数
print(ages.count(22))

# 元组的构造函数
    # tuple()          # 生成一个空的元组，等同于() 
    # tuple(iteranle)  # 用于可迭代对象生成一个元组 
t = tuple()          # 创建空元组，等于t =()
t = tuple('ABC')     # t = ('A', 'B', 'C')
t = tuple(range(5))  # t = (0, 1, 2, 3, 4)

# 元组的运算： 
    # + 拼接方式创建一个新的元组（id变） 
    # * 生成新的重复的元组
t = (1,2,3) + (4,5,6)  # t = (1,2,3,4,5,6 )(id变)
t += (7,8,9)           # t = (1,2,3,4,5,6,7,8,9) (id 再次变)

t = (1,2) * 2  # t = (1,2,1,2)
t *= 2         # t = (1,2,1,2,1,2,1,2)

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
>>>tup1 = (50)
>>> type(tup1)     # 不加逗号，类型为整型
<class 'int'>
 
>>> tup1 = (50,)
>>> type(tup1)     # 加上逗号，类型为元组
<class 'tuple'>

# 元组内置函数
len(tuple) # 计算元组元素个数。	
>>> tuple1 = ('Google', 'Runoob', 'Taobao')
>>> len(tuple1)
3

max(tuple) # 返回元组中元素最大值。	
>>> tuple2 = ('5', '4', '8')
>>> max(tuple2)
'8'

min(tuple) # 返回元组中元素最小值。	
>>> tuple2 = ('5', '4', '8')
>>> min(tuple2)
'4'

tuple(seq) # 将列表转换为元组。	
>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')

# 元组比较大小
t1=(3333,'a')
t2=(2,'a','b','c')
print(t1 < t2) # False，两个元组比较比的不是长度。依次比较每个个元素大小，如果第一个就分胜负了，就没比较比后面的了。


\循环
# whlie循环: 字符串、列表、元组 都可以依赖索引取值
l=['a','b','c','d','e']
# l='abcde'
#l=('a','b','c','d','e')
index=0
while index < len(l):
    print(l[index]) # 打印索引的值
    index+=1

# for循环: 不依赖索引取值
l1=['a','b','c','d','e']
for item in l1:
    print(item)

l2='abcde'
for item in l2:
    print(item)

# for循环+range方式模拟索引
for i in range(1,10,2): # 1是起始位置，10是结束位置，2为步长。只写个10就一个一个来。
    print(i)
'''
1
3
5
7
9
'''

l1=['a','b','c','d','e']
for i in range(len(l1)): # 以l1的长度做为range的范围
    print(i,l1[i])

# 循环: 字典，不依赖索引.循环字典的key。
# 简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入。
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

# while循环可以遍历字典里的值
goods_l=[]
while True:
    for key in msg_dic: # 取字典的key名循环，顺序不固定。
        print(key, msg_dic[key])   # 循环打印商品名和价格

    choice = input('购买的商品名>>: ').strip()
    if choice not in msg_dic:
        print('你购买的商品不存在，请重新输入。')
        continue

    count = input('购买个数>>: ').strip()
    if count.isdigit():
        goods_l.append((choice,msg_dic[choice],int(count))) # 把每个商品信息以元组的方式存入列表中
        print(goods_l)

# 改进
# for循环也可以遍历字典里的值
goods_l=[]
err_choice=0
while err_choice <= 2:
    for key in msg_dic:
        print(key,msg_dic[key])    # 循环打印商品名和价格
    choice = input('购买的商品名>>: ').strip()
    if choice == 'quit':
       print('您想要购买的商品是>>: ',goods_l)
       break
    if choice not in msg_dic:
        print(choice,'此商品不存在,请重新输入'.center(30,'-'))
        err_choice+=1              # 用户不按照列表输入3次商品名就结束循环
        continue
    count = input('购买的个数>>: ').strip()
    if count.isdigit():
        goods_l.append((choice,msg_dic[choice],int(count)))
        print(goods_l)
    else:
        print('请输入正确的购买数量')
else:
	print('你TM到底想买啥？')



