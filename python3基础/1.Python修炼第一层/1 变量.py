\什么是变量
# 变量即变化的量，核心是“变”与“量”二字，变即变化，量即衡量状态。

\为什么要有变量
# 程序执行的本质就是一系列状态的变化，变是程序执行的直接体现，所以我们需要有一种机制能够反映或者说是保存下来程序执行时状态以及状态的变化。
# 比如：
    英雄的等级为1，打怪升级(变)为10
    僵尸的存活状态True，被植物打死了，于是变为False
    人的名字为egon，也可以修改为Egon

age=10
\定义一个变量，会有三个特征：
    # id：反应在内存里的值
    # type：变量类型
    # value：值本身

print(id(age),type(age),age)

name='egon'
name = 'egon'
print(id(name),type(name),name)

\变量命名的方式
    # 1.驼峰体
        # AgeOfOldboy=73
    # 2.下划线(推荐)
        # age_of_oldboy=73

# 常量,变量名全用大些。
AGE_OF_OLDBOY=73
AGE_OF_OLDBOY=72
print(AGE_OF_OLDBOY)

\如何定义变量
# 变量名(相当于门牌号，指向值所在的空间)，等号，变量值。
name='Egon'
sex='male'  # 单引号双引号没区别
sex="male"
age=18
age = 18
level=10
aaa=level # 10
level2=10+age # 28

x,y=1,2   # 多元赋值
print(x,y)
name,age = 'zhy',18
print(name)
print(age)

# 多行注释也可以赋值给变量
name1='''
aaaaaaaaa
bbbbbbbbb
'''
name2="""
aaaaaaaaa

bbbbbbbbb
"""
print(name1,name2)

\变量的定义规范
    # 1. 变量名只能是 字母、数字或下划线的任意组合
    # 2. 变量名的第一个字符不能是数字
    # 3. 关键字不能声明为变量名['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
    #  'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
    #  'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
    # 例如:如下执行会报错
    # print=123
    # print(print)

\定义方式
    #驼峰体
    AgeOfOldboy = 56  # 大驼峰
    ageOfOldboy = 56  # 小驼峰
    NumberOfStudents = 80

    #下划线(推荐使用)
    age_of_oldboy = 56 
    number_of_students = 80

\定义变量名不好的方式
    #1. 变量名为中文、拼音
    #2. 变量名过长
    #3. 变量名词不达意

\定义变量会有：id，type，value
    #1 等号比较的是value，
    #2 is比较的是id
\强调：
    #1. id相同，type和value肯定相同。
    #2. value相同type肯定相同，但id可能不同,如下
x='Info Egon:18'
y='Info Egon:18'
print(id(x))
print(id(y))
print(x == y)
print(x is y)
'''
4514759408
4514759408
True
True
'''

\手动删除变量，无需del python有自动垃圾回收机制。
del x
print(x) # NameError: name 'x' is not defined

\常量
常量即指不变的量，如pai 3.141592653..., 或在程序运行过程中不会改变的量
举例，假如老男孩老师的年龄会变，那这就是个变量，但在一些情况下，他的年龄不会变了，那就是常量。

在Python中没有一个专门的语法代表常量，程序员约定俗成用变量名全部大写代表常量。
AGE_OF_OLDBOY = 56 # 常量规范都用大写，编程规范。

\内存空间绑定与解绑（python提供了垃圾回收机制）
# key不同value相同使用的是同一块内存空间，只是为不同的key值添加一个绑定关系。
name='egon'
print(id(name),type(name),name)  
name1='egon'
print(id(name1),type(name1),name1)
print(name)
print(name+name1)
print(name is name1)
print(name == name1)
'''
4560749880 <class 'str'> egon
4560749880 <class 'str'> egon
egon
egonegon
True
True
'''

\python中检测某个变量是否有定义
testvar=1

第一种方法使用内置函数locals()：
print(locals().keys())
print('testvar' in locals().keys())
# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'os', 'testvar'])
# True

第二种方法使用内置函数dir()： 列出一个对象的所有属性和方法
print(dir())
print('testvar' in dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'testvar', 'os']
# True

第三种方法使用内置函数vars()：
print('testvar' in vars().keys())

# 对于 x = 1，这样的一个赋值语句，我们在执行后，名称 x 引用到值 1。这就像字典一样，键引用值，当然，变量和所对应的值用的是个"不可见"的字典。我们可以使用 vars 函数来返回这个字典：
aaa = vars()
print(aaa["testvar"]) #  1

#测试如下:
#testvar未定义
In [1]: 'testvar' in locals().keys()
Out[1]: False
 
In [2]: 'testvar' in dir()
Out[2]: False
 
In [3]: 'testvar' in vars().keys()
Out[3]: False
 
#定义testvar
In [4]: testvar=1
 
In [5]: 'testvar' in locals().keys()
Out[5]: True
 
In [6]: 'testvar' in dir()
Out[6]: True
 
In [7]: 'testvar' in vars().keys()
Out[7]: True
# 还有使用try...except...自己定义的,总之方法很多

\四个个内置函数的区别
print(locals().keys())
print(vars().keys())
print(globals().keys())
print(dir())
"""
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'testvar'])
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'testvar'])
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'testvar'])
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'testvar']
"""

\变量运算
# 字符串和数字不能相加，如果想相加需要转换类型。可以相乘。
n1 = 'aaa'
n2 = 10
n3 = '10'
print(str(n1) + str(n2) + 'bbb')
print(n1 *  n2)
print(n1 + n2) # 报错