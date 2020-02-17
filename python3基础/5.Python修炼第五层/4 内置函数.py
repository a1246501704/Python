#注意：内置函数id()可以返回一个对象的身份，返回值为整数。这个整数通常对应与该对象在内存中的位置，但这与python的具体实现有关，不应该作为对身份的定义，
# 即不够精准，最精准的还是以内存地址为准。is运算符用于比较两个对象的身份，等号比较两个对象的值，内置函数type()则返回一个对象的类型.

官方内置函数：https://docs.python.org/3/library/functions.html?highlight=built#ascii 

\ 优先掌握
max
min
sorted
map
from _functools import reduce
filter
sum
bool
chr
divmod
enumerate
id
input
print
isinstance
iter
len
open
pow
type
zip


\面向对象
object

classmethod
staticmethod
property

getattr
hasattr
setattr
delattr

super

isinstance
issubclass

object.__dict__

int,str,bytes,list,tuple,set,float,dict


\其他内置函数

\abc :求绝对值,负数变整数
print(abs(-1)) # 1

\all : 传给all的可迭代对象中的值都是True，最终结果就是True。如果给的可迭代对象是空的，也是True。
print(all([1,'a',[]])) # False
print(all([]))         # True

\any : 传给any的可迭代对象中的值只要有一个是True，最终结果就是True。如果给的可迭代对象是空的，也是False。
print(any([0,None,'',1])) # True
print(any([]))            # False

\bin：十进制转二进制  oct：十进制转八进制  hex：十进制转二进制
print(bin(10)) # 0b1010
print(oct(10)) # 0o12
print(hex(10)) # 0xa


# 布尔值为假：0，None,空
bool()

\bytes类型
print('hello'.encode('utf-8'))  # b'hello'
print(bytes('hello',encoding='utf-8')) # b'hello'

\callable: 判断是否可以被调用
print(callable(max)) # True

\chr是按照assic表的数字转换成字符，ord是按照assic表将大写字符转成数字。如：写验证码功能
print(chr(65))  # A
print(ord('A')) # 65


\complex复数
x=1-2j # x=complex(1-2j)
print(type(x)) # <class 'complex'>
print(x.real)  # 实步 1.0
print(x.imag)  # 虚步 -2.0

\dict,int,list,tuple,str,float,set,frozenset
s=set({1,2,3})       # 可修改的集合
s=frozenset({1,2,3}) # 不可修改的集合

\dir：如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。
import time
print(dir(time))
'''
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']
'''

\divmod：它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。
print(divmod(1001,25)) # (40, 1),1001除以25的商和余数。

\enumerate(iterable, start=0)
# 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
l=['a','b','c','d']
for x in enumerate(l):
    print(x)
'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
'''

\hash：返回该对象的哈希值
print(hash('asdfasdfasdfasdfasdf'))  # -458434733274929561
print(hash(' asdfasdfasdfasdfasdf')) # 171541017366323274,改一点都不行

\help：查看函数注释信息
def func():
    '''
    xxxxxx
    :return:
    '''
    pass

print(help(func))

\isinstance : 判断一个数据的数据类型
print(isinstance(1,int))
print(type(1) is int)

\pow 
print(pow(10,2,3)) #10**2%3,10的2次方对3取余

\str
print(str({'a':1}))

\reversed ：反转
l=[1,4,2,9]
print(list(reversed(l)))

\round ：保留3位小数，后面的四舍五入。
print(round(10.55545,3))

\slice ：切片
l1=['a','b','c','d','e']
l2=['a','b','c','d','e']
print(l1[1:5:2]) #'b','d'，列表切片
print(l2[1:5:2]) #'b','d'

obj=slice(1,5,2) # 切片对象
print(l1[obj]) # ['b', 'd']
print(l2[obj]) # ['b', 'd']

\sum :求和
print(sum([1,2,3,4])) # 10 
print(sum(range(10))) # 45

\vars()不传参数和 locals()是相等的
print(vars() is locals())
vars(obj) 等同于obj.__dict__

x=111111111111111111111111111111111111111
print(locals())
'''
{'__name__': '__main__', '__doc__': '\n@File     : test.py\n@Time     : 2019/8/25 2:49 下午\n@Author   : zhanghongyang\n@Email    : chinazhanghy@gmail.com\n@Software : PyCharm\n', \
'__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x101f93ac8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, \
'__file__': '/Users/zhanghongyang/PycharmProjects/Project-python3/test.py', '__cached__': None, 'namedtuple': <function namedtuple at 0x102c0ed08>, 'wraps': <function wraps at 0x102c0ed90>, \
'json': <module 'json' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py'>, 'salaries': {'egon': 3000, 'alex': 100000000, 'wupeiqi': 10000, 'yuanhao': 2000}, \
'l1': ['a', 'b', 'c', 'd', 'e'], 'l2': ['a', 'b', 'c', 'd', 'e'], 'x': 111111111111111111111111111111111111111}
'''

\__import__ :通过字符串来导入模块
m=input('>>: ') # time
print(type(m))
obj=__import__(m)
obj.sleep(3)

# import "time" # import 不能导入字符串, 通过__import__可以针对import导入模块进行扩展。




\了解：eval,exec,compile

\eval:提取字符串内的表达式执行，然后返回执行结果。
s1="1+2+3"
l=eval(s1)
print(type(l),l) # <class 'int'> 6

s1="['a','b','c']"
l=eval(s1)
print(type(l),l) # <class 'list'> ['a', 'b', 'c']


s2="for i in range(10):print(i)"
eval(s2) # 报错

# eval函数就是实现list、dict、tuple与str之间的转化
# 字符串转换成列表
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(type(b))
print(b)
'''
<class 'str'>
<class 'list'>
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
'''
# 字符串转换成字典
a = "{1: 'a', 2: 'b'}"
print(type(a))
b = eval(a)
print(type(b))
print(b)
'''
<class 'str'>
<class 'dict'>
{1: 'a', 2: 'b'}
'''
# 字符串转换成元组
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))
b=eval(a)
print(type(b))
print(b)
'''
<class 'str'>
<class 'tuple'>
([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))
'''

\exec：仅仅只是执行字符串内的表达式或语句，没有返回值。
s1="1+2+3"
print(exec(s1)) # None

s2="for i in range(10):print(i)" # 执行字符串类型的语句
exec(s2)
'''
0
1
2
3
4
5
6
7
8
9
'''
\eval与exec的区别
#1、语法
# eval(str,[,globasl[,locals]])
# exec(str,[,globasl[,locals]])

#2、区别
#示例一：
s='1+2+3'
print(eval(s)) #eval用来执行表达式，并返回表达式执行的结果
print(exec(s)) #exec用来执行语句，不会返回任何值
'''
6
None
'''

#示例二：
print(eval('1+2+x',{'x':3},{'x':30})) #返回33
print(exec('1+2+x',{'x':3},{'x':30})) #返回None

print(eval('for i in range(10):print(i)')) # 语法错误，eval不能执行表达式
print(exec('for i in range(10):print(i)')) # exec可以执行


\compile()函数将一个字符串编译为字节代码。可以被exec和eval执行的字节码
compile(str,filename,kind)
  filename:用于追踪str来自于哪个文件，如果不想追踪就可以不定义
  kind可以是：single代表一条语句，exec代表一组语句，eval代表一个表达式
s='for i in range(10):print(i)'
code=compile(s,'','exec')
exec(code)


s='1+2+3'
code=compile(s,'','eval')
eval(code)

complie（了解即可）


\format
# 字符串可以提供的参数 's' None
>>> format('some string','s')
'some string'
>>> format('some string')
'some string'

# 整形数值可以提供的参数有 'b' 'c' 'd' 'o' 'x' 'X' 'n' None
>>> format(3,'b')  # 转换成二进制
'11'
>>> format(97,'c') # 转换unicode成字符
'a'
>>> format(11,'d') # 转换成10进制
'11'
>>> format(11,'o') # 转换成8进制
'13'
>>> format(11,'x') # 转换成16进制 小写字母表示
'b'
>>> format(11,'X') # 转换成16进制 大写字母表示
'B'
>>> format(11,'n') # 和d一样
'11'
>>> format(11)     # 默认和d一样
'11'

# 浮点数可以提供的参数有 'e' 'E' 'f' 'F' 'g' 'G' 'n' '%' None
>>> format(314159267,'e')    # 科学计数法，默认保留6位小数
'3.141593e+08'
>>> format(314159267,'0.2e') # 科学计数法，指定保留2位小数
'3.14e+08'
>>> format(314159267,'0.2E') # 科学计数法，指定保留2位小数，采用大写E表示
'3.14E+08'
>>> format(314159267,'f')    # 小数点计数法，默认保留6位小数
'314159267.000000'
>>> format(3.14159267000,'f')# 小数点计数法，默认保留6位小数
'3.141593'
>>> format(3.14159267000,'0.8f') # 小数点计数法，指定保留8位小数
'3.14159267'
>>> format(3.14159267000,'0.10f')# 小数点计数法，指定保留10位小数
'3.1415926700'
>>> format(3.14e+1000000,'F')    # 小数点计数法，无穷大转换成大小字母
'INF'

#g的格式化比较特殊，假设p为格式中指定的保留小数位数，先尝试采用科学计数法格式化，得到幂指数exp，如果-4<=exp<p，则采用小数计数法，并保留p-1-exp位小数，否则按小数计数法计数，并按p-1保留小数位数
>>> format(0.00003141566,'.1g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留0位小数点
'3e-05'
>>> format(0.00003141566,'.2g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留1位小数点
'3.1e-05'
>>> format(0.00003141566,'.3g') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留2位小数点
'3.14e-05'
>>> format(0.00003141566,'.3G') #p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留0位小数点，E使用大写
'3.14E-05'
>>> format(3.1415926777,'.1g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留0位小数点
'3'
>>> format(3.1415926777,'.2g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留1位小数点
'3.1'
>>> format(3.1415926777,'.3g') #p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留2位小数点
'3.14'
>>> format(0.00003141566,'.1n') #和g相同
'3e-05'
>>> format(0.00003141566,'.3n') #和g相同
'3.14e-05'
>>> format(0.00003141566) #和g相同
'3.141566e-05'


\lambda与内置函数结合使用
字典的运算：最小值，最大值，排序
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}

迭代字典，取得是key，因而比较的是key的最大和最小值
>>> max(salaries)
'yuanhao'
>>> min(salaries)
'alex'

可以取values，来比较
>>> max(salaries.values())
>>> min(salaries.values())
但通常我们都是想取出，工资最高的那个人名，即比较的是salaries的值，得到的是键
>>> max(salaries,key=lambda k:salary[k])
'alex'
>>> min(salaries,key=lambda k:salary[k])
'yuanhao'

也可以通过zip的方式实现
salaries_and_names=zip(salaries.values(),salaries.keys())

先比较值，值相同则比较键
>>> max(salaries_and_names)
(100000000, 'alex')


salaries_and_names是迭代器，因而只能访问一次
>>> min(salaries_and_names)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: min() arg is an empty sequence

sorted(iterable，key=None,reverse=False)

