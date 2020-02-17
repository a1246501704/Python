\数字
# int整型
    # 定义：age=10 # 实质age=int(10)
    # 用于标识：年龄，等级，身份证号，qq号，个数

# float浮点型
    # 定义：salary=3.1 # 实质salary=float(3.1)
    # 用于标识：工资，身高，体重
height=1.81
height=float(1.81)
print(type(height),height)

\字符串类型：把一堆字符放入到单引号、双引号、三引号中
#在python中，加了引号的字符就是字符串类型，python并没有字符类型。
#定义：name='egon' #name=str('egon') 

# 字符串：表示一些描述性状态，人的名字，人的性别
name="egon" # 实质name=str("egon")
print(type(name))

comment='''
哇哈哈，哦也！
'''

msg="i'm is ok"

# 字符串拼接
    # 1 只能字符串之间拼接
    # 2 字符串之间只能用+或*
name='egon'
msg='hello'
age=18
print(name+msg+str(age))  # 使用str将age变量的值转换成字符串
print(name*10)  # 重复10次
数字可以进行加减乘除等运算，字符串呢？让我大声告诉你，也能？what ?是的，但只能进行"相加"和"相乘"运算。
>>> name='egon'
>>> age='18'
>>> name+age #相加其实就是简单拼接
'egon18'
>>> name*5 
'egonegonegonegonegon'
#注意1：字符串相加的效率不高
字符串1+字符串3，并不会在字符串1的基础上加字符串2，而是申请一个全新的内存空间存入字符串1和字符串3，相当字符串1与字符串3的空间被复制了一次.
#注意2：只能字符串加字符串，不能字符串加其他类型

\列表：
用字符串也能存多个值，但是不好取。
# hobbies='play read music movie'   
# print(hobbies)
列表：定义在[]内，用逗号分隔开的多个元素，每个元素可以是任意类型。
定义：students=['egon','alex','wupeiqi',] # students=list(['egon','alex','wupeiqi',]) 
表示：存取放多个值，比如存放人的爱好，人的信息，

hobbies=['play','read','music','movie']  # hobbies=list(['play','read','music','movie'])
print(type(hobbies))
print(hobbies[3])
print(hobbies[0])   # 正着取
print(hobbies[-1])  # 倒着取

print(hobbies[10])  # 超出范围会报错
# IndexError: list index out of range

# 更新列表元素,更改的是原始列表。
hobbies[0]="wan"
# 删除列表元素
del hobbies[0] # 删除第0个后，原来索引位置为1的会为0，以此类推。
# 列表脚本操作符
print(len([1, 2, 3]))        # 3,和把列表赋值给一个变量是同样的结果。
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]，和把列表赋值给一个变量是同样的结果。
print(['Hi!'] * 4)           # ['Hi!', 'Hi!', 'Hi!', 'Hi!'],和把列表赋值给一个变量是同样的结果。
print(3 in [1, 2, 3])        # True ,和把列表赋值给一个变量是同样的结果。
for x in [1, 2, 3]: print(x) # 输出多行，和把列表赋值给一个变量是同样的结果。
'''
1
2
3
'''
# 列表截取
L=['spam', 'Spam', 'SPAM!'];
print(L[2])  #'SPAM!'
print(L[-2]) #'Spam'
print(L[1:]) #['Spam', 'SPAM!']

# 列表函数&方法,obj为元素名。
len(list) # 列表元素个数
max(list) # 返回列表元素最大值
min(list) # 返回列表元素最小值
list(seq) # 将元组转换为列表
list.append(obj) # 在列表末尾添加新的对象
list.count(obj)  # 统计某个元素在列表中出现的次数
list.extend(seq) # 在列表末尾一次性追加另一个序列中的多个值到列表中(用新列表扩展原来的列表)
list.index(obj)  # 从列表中找出某个值第一个匹配项的索引位置，索引从0开始。
list.insert(index, obj)  # 将对象插入列表，index为要插入到的索引位置。
list.pop(obj=list[-1])   # 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值。
list.remove(obj) # 移除列表中某个值的第一个匹配项（从左到右）。
list.reverse()   # 反向列表中元素，倒转。
list.clear()     # 清空列表
list.copy()      # 复制列表
list.sort([func]) # 对原列表进行排序。reverse 排序规则，reverse = True 降序，reverse = False 升序（默认）。
'''
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort(reverse = False) # 不可以和print写在一起，也不能直接赋值
print(aList)
'''

# 列表切片
a = [1,2,3,4]
print(a[:])
print(a[::])
print(a[:3])
print(a[1:3:2])
print(a[3])
'''
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3]
[2]
4
注意，这里只有最后一个输出是不带[]的，表明只有最后一个输出的是元素，其他在切片中只用了:符号的输出均为list，不论是输出是只有一个元素还是多个元素.
'''

# 下面考虑嵌套list的情况：
a = [[1,2],[3,4]]
print(a[:][0])
print(a[0][:])
print(a[:-1])
print(a[0][0])
'''
[1,2]
[1,2]
[[1,2]]
1
可以看到实际上每个[]相对于对对应层次的list进行操作，总体规则与单个list一致。
'''

# 列表可存放多中类型的值，下面是一个列表嵌套、取值操作
l=[1,1.3,'egon',['a','b']]  
print(l[3][1])   #取里面列表中的b

#存放多个学生的信息：姓名，年龄，爱好
students_info=[['egon',18,['play',]],['alex',18,['play','sleep']]]
print(students_info[0][2][0]) #取出第一个学生的第一个爱好
'play'

# 要知道每个索引位置的值是什么才知道怎么取。用字典则不需要知道索引位置。
#       id         name   sex     hobbies
info=[12312312312,'egon','male',['read','music']]
print(info[3][1])
print(info[1])

# 列表嵌套多种实现方式
list=[]
for i in range(1,101):
    list.append(i)

# print(list)

tempList=[]
newList=[]

while True:
    num=0
    for temp in list:
        tempList.append(temp)
        num+=1
        if num==3:
            newList.append(tempList)
            tempList=[]
            num=0
            continue
    if temp==100:
        newList.append(tempList)
        break

print(newList)
'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24],.......[100]]
'''

oldList=[x for x in range(1,101)]
newList=[oldList[x:x+3] for x in range(0,len(oldList),3)]
print(newList)
'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24],.......[100]]
'''

def f(x,y,z):
    return x,y,z

m = list(map(f, [x for x in range(1,101,3)], [y for y in range(2,101,3)], [z for z in range(3,101,3)]))
print(list(m))
'''
[(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),......(100)]
'''




\字典：
#为何还要用字典？
存放一个人的信息：姓名，性别，年龄，很明显是多个值，既然是存多个值，我们完全可以基于刚刚学习的列表去存放，如下
nfo=['egon','male',18]
定义列表的目的不单单是为了存，还要考虑取值，如果我想取出这个人的年龄，可以用
print(info[2])
18
但这是基于我们已经知道在第3个位置存放的是年龄的前提下，我们才知道索引2对应的是年龄
即：
     # name, sex, age
info=['egon','male',18]
而这完全只是一种假设，并没有真正意义上规定第三个位置存放的是年龄，于是我们需要寻求一种，即可以存放多个任意类型的值，又可以硬性规定值的映射关系的类型，比如key=value，这就用到了字典

# 定义的{}内，用key=value形式表示一个元素，用逗号分隔开。
# 定义：info={'name':'egon','age':18,'sex':18} #info=dict({'name':'egon','age':18,'sex':18})
# 用于标识：存储多个值的情况，每个值都有唯一一个对应的key，可以更为方便高效地取值
info={'name':'egon','id':'1232143423','sex':'male','hobbies':['read','music',]}
print(info['name'])
print(info['hobbies'][1])  # 取第二个爱好

# 字典嵌套
info={
    'name':'egon',
    'hobbies':['play','sleep'],
    'company_info':{
        'name':'Oldboy',
        'type':'education',
        'emp_num':40,
    }
}
print(info['company_info']['name']) # 取公司名

students=[
    {'name':'alex','age':38,'hobbies':['play','sleep']},
    {'name':'egon','age':18,'hobbies':['read','sleep']},
    {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
]
print(students[1]['hobbies'][1]) #取第二个学生的第二个爱好

# 创建字典 
dict1={'a':2,'b':3,'c':8,'d':4}

# 排序
dict2 = sorted(dict1)              # sorted()默认是对字典的键，从小到大进行排序。
print(dict2)                       # ['a', 'd', 'e', 'f']

dict2 = sorted(dict1,reverse=True) # 对键值进行反向（从大到小）排序
print(dict2)                       # ['f', 'e', 'd', 'a']
# 像这种对键进行排序，往往是为了得到 值（value），拿到键最大，对应的值，如：
print(dict1[dict2[0]])             # 结果为8

list1= sorted(dict1.keys(),reverse=True) # 也可以先拿到所有的key，然后再对key排序。
print(list1)                       # 结果：['f', 'e', 'd', 'a']
 
list1= sorted(dict1.values())      # 对value进行排序，用dict1.values()得到所有的values，然后对value排序。
print(list1)                       # 结果：[2, 3, 4, 8]

# 设值reverse=True 进行反向排序，也可以用dict1.items()，得到包含键，值的元组。由于迭代对象是元组，返回值自然是元组组成的列表。这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键。
list1= sorted(dict1.items(),key=lambda x:x[1]) 
print(list1)                       # [('a', 2), ('e', 3), ('d', 4), ('f', 8)]

list1= sorted(dict1.items(),key=lambda x:x[0]) # 对键进行排序
print(list1)                       # [('a', 2), ('d', 4), ('e', 3), ('f', 8)]

# 遍历
    a={'a': '1', 'b': '2', 'c': '3'}
    # (1)遍历key值
    for key in a:
        print(key+':'+a[key])
    '''
    a:1
    b:2
    c:3
    '''
    for key in a.keys():
        print(key+':'+a[key])
    '''
    a:1
    b:2
    c:3
    '''
    # 在使用上，for key in a和 for key in a.keys():完全等价。
    # (2)遍历value值
    for value in a.values():
        print(value)
    '''
    1
    2
    3
    '''
    # (3)遍历字典项
    for kv in a.items():
        print(kv)
    ''' 
    ('a', '1')
    ('b', '2')
    ('c', '3')
    '''
    # (4)遍历字典健值
    for key,value in a.items():
        print(key+':'+value)
    '''
    a:1
    b:2
    c:3
    '''
    for (key,value) in a.items():
        print(key+':'+value)
    '''
    a:1
    b:2
    c:3
    '''
    # 在使用上for key,value in a.items()与for (key,value) in a.items()完全等价

# 增删改查
info = {
    "stull01":"alen zhang",
    "stull02":"si li",
    "stull03":"san zhang",
}

    #查
    print(info)
    print(info["stull01"])
    print(info.get("stull04"))      #有就返回它的值，没有就为None
    print("stull03" in info)        #判断一个键是否在一个字典里面，有就True没有就False

    #改
    info["stull02"] = "李四"
    print(info)

    #增
    info["stull04"] = "小王"
    print(info)

    #删
    del info["stull04"]     #注意永久性的删除
    info.pop("stull03")     #弹出，跟列表里面的pop用法一样，可以去参考一下
    test1 = info.popitem()          #随机弹出
    print(info)
    print(test1)


# 操作
# 1、取字典的所有键，所有的值，利用dict1.keys()，dict1.vaules()，由于键，值有很多个，所以要加s，另外注意这里要加括号，这样的小细节不注意，很容易犯错。
print(dict1.values(),dict1.keys())
'''
dict_values([4, 2, 8, 3]) dict_keys(['d', 'a', 'c', 'b'])
'''
# 2、同时取字典的键、值，dict1.items()，这里同样加s和括号。通过dict1.items()这个函数，把字典形式的键、值，存在了一个元组内。
print(dict1.items())
'''
dict_items([('d', 4), ('a', 2), ('c', 8), ('b', 3)])
'''

# 字典中常见方法
    # 方法                                  #描述  
    -------------------------------------------------------------------------------------------------  
    D.clear()                              #移除D中的所有项  
    D.copy()                               #返回D的副本  
    D.fromkeys(seq[,val])                  #返回从seq中获得的键和被设置为val的值的字典。可做类方法调用  
    D.get(key[,default])                   #如果D[key]存在，将其返回；否则返回给定的默认值None  
    D.has_key(key)                         #检查D是否有给定键key  
    D.items()                              #返回表示D项的(键，值)对列表  
    D.iteritems()                          #从D.items()返回的(键，值)对中返回一个可迭代的对象  
    D.iterkeys()                           #从D的键中返回一个可迭代对象  
    D.itervalues()                         #从D的值中返回一个可迭代对象  
    D.keys()                               #返回D键的列表  
    D.pop(key[,d])                         #移除并且返回对应给定键key或给定的默认值D的值  
    D.popitem()                            #从D中移除任意一项，并将其作为(键，值)对返回  
    D.setdefault(key[,default])            #如果D[key]存在则将其返回；否则返回默认值None  
    D.update(other)                        #将other中的每一项加入到D中。  
    D.values()                             #返回D中值的列表

\布尔类型
# 布尔值，一个True 一个False
# 所有数据类型都自带布尔值
布尔类型的重点知识！！！：
    1、None，0，空（空字符串，空列表，空字典等）三种情况下布尔值为False。
    2、其余均为True 
#计算机俗称电脑，即我们编写程序让计算机运行时，应该是让计算机无限接近人脑，或者说人脑能干什么，计算机就应该能干什么，
#人脑的主要作用是数据运行与逻辑运算，此处的布尔类型就模拟人的逻辑运行，即判断一个条件成立时，用True标识，不成立则用False标识。

print(type(True))
AGE=73
age=18
print(age > AGE)
print(age < AGE)

接下来就可以根据条件结果来干不同的事情了：
if a > b: 
   print(a is bigger than b )
else 
   print(a is smaller than b )
# 上面是伪代码，但意味着，计算机已经可以像人脑一样根据判断结果不同，来执行不同的动作。 


重点：
#1.可变类型：在id不变的情况下，value可以变，则称为可变类型，如列表，字典。
#2.不可变类型：value一旦改变，id也改变，则称为不可变类型（id变，意味着创建了新的内存空间），如一个相同的变量赋值两次不同的值。


\数字类型转换
str(x) 将对象x转换为字符串 
tuple(s) 将序列s转换为一个元组 
list(s) 将序列s转换为一个列表 
int(x [,base]) 将x转换为一个整数 
float(x ) 将x转换到一个浮点数 
complex(real [,imag]) 创建一个复数 
repr(x) 将对象x转换为表达式字符串 
eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象 
    x='2 + 4'
    print(eval(x))
chr(x) 将一个整数转换为一个字符 
unichr(x) 将一个整数转换为Unicode字符 
ord(x) 将一个字符转换为它的整数值 
hex(x) 将一个整数转换为一个十六进制字符串 
oct(x) 将一个整数转换为一个八进制字符串

