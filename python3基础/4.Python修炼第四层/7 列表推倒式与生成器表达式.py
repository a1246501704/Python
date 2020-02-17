\列表解析，也叫列表推到式
# 1、语法
[expression for item1 in iterable1 if condition1
for item2 in iterable2 if condition2
...
for itemN in iterableN if conditionN
]

类似于
res=[]
for item1 in iterable1:
    if condition1:
        for item2 in iterable2:
            if condition2
                ...
                for itemN in iterableN:
                    if conditionN:
                        res.append(expression)

# 2、案例：下10个鸡蛋,将大于等于3的放入列表中
egg_list=[]
for i in range(10):
    if i >= 3:
        res='egg%s' %i
        egg_list.append(res
print(egg_list)

# 3、优点：方便，改变了编程习惯，可称之为声明式编程
\使用列表推倒式实现: 
# 将上述的for循环方在中括号中使用列表解析的方式实现
l=['egg%s' %i for i in range(10) if i >= 3] # for循环结果方左边，其他判断放右边。可以写的更复杂。(针对range比较小的时候使用)
print(l) # 以列表的形式保存

# 多个for
one = ['A']
two = ['a','b','c']

def aaa():
	print([i + y for i in one for y in two])  # 每个for取一个值，两只值相加。for循环的次数是以最长的列表为依据。

aaa() # ['Aa', 'Ab', 'Ac']

\使用生成器表达式实现:
# 1、把列表推导式的[]换成()就是生成器表达式
# 2、示例：上面是给了一筐鸡蛋，而这个是给你一只老母鸡，用的时候就下蛋，这也是生成器的特性
# 放在小括号中，变成一个生成器，然后一个一个下。
chicken=('egg%s' %i for i in range(10) if i >= 3) # 使用圆括号、结果是个生成器（生成器本身就是迭代器），(针对range比较大的时候可以这么使用)。
print(next(chicken)) # 每next一次取一个值
print(list(chicken)) # 因chicken可迭代，因而可以转成列表。

# 可以写多层，但是不太易于理解。
for i in ...:
    if ...:
        for i in ...:
            if ...:
                for ...
# 3、优点：省内存，一次只产生一个值在内存中.



练习题:
1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
5、思考题
        with open('a.txt') as f:
        g=(len(line) for line in f)
        print(sum(g)) #为何报错？
6、文件shopping.txt内容如下
        mac,20000,3
        lenovo,3000,10
        tesla,1000000,10
        chicken,200,1
        求总共花了多少钱？
        打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
        求单价大于10000的商品信息,格式同上

#题目一
names=['egon','alex_sb','wupeiqi','yuanhao']
names=[name.upper() for name in names]

#题目二
names=['egon','alex_sb','wupeiqi','yuanhao']
names=[len(name) for name in names if not name.endswith('sb')] # upper变成大写，endswith过滤掉结尾包含sb的。

#题目三
with open('a.txt',encoding='utf-8') as f:
    print(max(len(line) for line in f))

#题目四
with open('a.txt', encoding='utf-8') as f:
    print(sum(len(line) for line in f))
    print(sum(len(line) for line in f)) # 求包换换行符在内的文件所有的字符数，为何得到的值为0?
    print(sum(len(line) for line in f)) # 求包换换行符在内的文件所有的字符数，为何得到的值为0?

#题目五（略）

#题目六：每次必须重新打开文件或seek到文件开头，因为迭代完一次就结束了
with open('a.txt',encoding='utf-8') as f:
    info=[line.split() for line in f]
    cost=sum(float(unit_price)*int(count) for _,unit_price,count in info)
    print(cost)


with open('a.txt',encoding='utf-8') as f:
    info=[{
        'name': line.split()[0],
        'price': float(line.split()[1]),
        'count': int(line.split()[2]),
    } for line in f]
    print(info)


with open('a.txt',encoding='utf-8') as f:
    info=[{
        'name': line.split()[0],
        'price': float(line.split()[1]),
        'count': int(line.split()[2]),
    } for line in f if float(line.split()[1]) > 10000]
    print(info)





