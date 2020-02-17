程序中经常会有这样场景：要求用户输入信息，然后打印成固定的格式.
    比如要求用户输入用户名和年龄，然后打印如下格式：
    My name is xxx，my age is xxx.
    很明显，用逗号进行字符串拼接，只能把用户输入的名字和年龄放到末尾，无法放到指定的xxx位置，而且数字也必须经过str(数字)的转换才能与字符串进行拼接。

\这就用到了占位符，如：
    %%	百分号标记
    %c	字符及其ASCII码
    %s	字符串
    %d	有符号整数(十进制)
    %u	无符号整数(十进制)
    %o	无符号整数(八进制)
    %x	无符号整数(十六进制)
    %X	无符号整数(十六进制大写字符)
    %e	浮点数字(科学计数法)
    %E	浮点数字(科学计数法，用E代替e)
    %f	浮点数字(用小数点符号)
    %g	浮点数字(根据值的大小采用%e或%f)
    %G	浮点数字(类似于%g)
    %p	指针(用十六进制打印值的内存地址)
    %n	存储输出字符的数量放进参数列表的下一个变量中
  
参考文档: https://www.cnblogs.com/fat39/p/7159881.html

\方法1: %-formatting
# %s字符串占位符：可以接收字符串，也可接收数字
print('My name is %s,my age is %s' %('egon',18))

# %d数字占位符：只能接收数字
print('My name is %s,my age is %d' %('egon',18))
print('My name is %s,my age is %d' %('egon','18')) #报错

#接收用户输入，打印成指定格式
name=input('your name: ')
age=input('your age: ') #用户输入18,会存成字符串18,无法传给%d

print('My name is %s,my age is %s' %(name,age))
print('My name is %s,my age is %d' %(name,int(age)))

#注意：
#print('My name is %s,my age is %d' %(name,age)) #age为字符串类型,无法传给%d,所以会报错

# 也支持字典的形式
print('User[%(id)s]: %(name)s' %{'id': 123,'name': 'xiaoming'})
Out: 'User[123]: xiaoming'

# 打印整数
print("I am %d years old." %(25))
'''
I am 25 years old.
'''

# 打印浮点数（指定保留两位小数）
print ("His height is %.2f m"%(1.70))
'''
His height is 1.70 m
'''

# 指定占位符宽度
print ("Name:%10s Age:%8d Height:%8.2f"%("Alfred",25,1.70))
'''
Name:    Alfred Age:      25 Height:    1.70
'''

# 指定占位符宽度（左对齐）
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Alfred",25,1.70))
'''
Name:Alfred     Age:25       Height:1.70
'''

# %s
# %10s——右对齐，占位符10位
# %-10s——左对齐，占位符10位
# %.2s——截取2位字符串
# %10.2s——10位占位符，截取两位字符串
print('%s' % 'hello world')       # 字符串输出
print('%20s' % 'hello world')     # 右对齐，宽度20位，不够则用空格补位
print('%-20s' % 'hello world')    # 左对齐，宽度20位，不够则用空格补位,hello world         ,前面有很多空格
print('[%-20s]' % 'hello world')  # [hello world         ]
print('%.2s' % 'hello world')     # 取2位
print('%10.2s' % 'hello world')   # 右对齐，取2位
print('%-10.2s' % 'hello world')  # 左对齐，取2位



总结:
# 这种用法一直到现在仍然被使广泛使用，但是其实它是一种不被提倡使用的语法(我初Python学习时，就提过)。主要是当要格式化的参数很多时，
# 可读性很差，还容易出错（数错占位符的数量），也不灵活，举个例子，name这个变量要在格式化时用2次，就要传入2次。

\方法2: str-format
# 从 Python 2.6开始，新增了一种格式化字符串的函数 str.format()，基本语法是通过 {}和: 来代替以前的 %。format函数支持通过位置、关键字、对象属性和下标等多种方式使用，
# 不仅参数可以不按顺序，也可以不用参数或者一个参数使用多次。并且可以通过对要转换为字符串的对象的 __format __方法进行扩展。

通过{}来代替:
In: name ='Xiaoming'
In: 'Hello {}'.format(name)
Out: 'Hello Xiaoming'

通过位置访问:
In: '{0},{1},{2}'.format('a','b','c')
Out: 'a,b,c'

In: '{2},{1},{0}'.format('a','b','c')
Out: 'c,b,a'

In: '{1},{1},{0}'.format('a','b','c')
Out: 'b, b, a'

通过关键字访问:
In: 'Hello {name}'.format(name='Xiaoming')
Out: 'Hello Xiaoming'

通过对象属性访问:
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'my name is {self.name},age is {self.age} years old'.format(self=self)

print(Person('xiaodeng',28)) # my name is xiaodeng,age is 28 old

通过下标访问:
In: coord = (3, 5)
In: 'X: {0[0]};Y:{0[1]}'.format(coord)
Out: 'X: 3;Y: 5

# 左中右对齐及位数补全
（1）< （默认）左对齐、
    > 右对齐、
    ^ 中间对齐、
    = （只用于数字）在小数点后进行补齐
（2）取位数“{:4s}”、"{:.2f}"等

print('{} and {}'.format('hello','world'))           # 默认左对齐
hello and world
print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
hello      and      world
print('{:^10s} and {:^10s}'.format('hello','world')) # 取10位中间对齐
  hello    and   world   
print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数
1.123 is 1.12
print('{0} is {0:>10.2f}'.format(1.123))   # 取2位小数，右对齐，取10位
1.123 is       1.12
>>> '{:<30}'.format('left aligned')   # 左对齐
'left aligned                  '
>>> '{:>30}'.format('right aligned')  # 右对齐
'                 right aligned'
>>> '{:^30}'.format('centered')   # 中间对齐
'           centered           '
>>> '{:*^30}'.format('centered')  # 使用“*”填充
'***********centered***********'
>>>'{:0=30}'.format(11)  # 还有“=”只能应用于数字，这种方法可用“>”代替
'000000000000000000000000000011'

总结:
# 可以感受到format函数极大的扩展了格式化功能。但是当处理多个参数和更长的字符串时，str.format() 的内容仍然可能非常冗长，除了定义参数变量，需要把这些变量写进format方法里面。


\方法3: f-Strings 
# 现在好了，Python 3.6新增了f-strings，这个特性叫做 字面量格式化字符串，F字符串是开头有一个f的字符串文字，Python会计算其中的用大括号包起来的表达式，并将计算后的值替换进去。
In: name='Xiaoming'

In: f'Hello {name}'
Out: 'Hello Xiaoming'

In: f'Hello {name.upper()}'
Out: 'Hello XIAOMING'

In: d={'id':123,'name':'Xiaoming'}

In: f'User[{d["id"]}]: {d["name"]}'
Out: 'User[123]: Xiaoming'

\和format用法比：

1、通过位置
data = ['data1', 'data2']
# format
print("data1: {0}, data2: {1}".format(*data))
# f-strings
print(f"data1: {data[0]}, data2: {data[1]}")

2、通过关键字
personal = {"name": "Json", "age": 12, "sex": "M"}
# format
print("Name: {name}, age: {age}, sex: {sex}".format(**personal))
# f-strings
print(f"Name: {personal['name']}, age: {personal['age']}, sex: {personal['sex']}")

3、数据精度和类型
num = 23234.76686566
# 保留两位小数
print(f"{num:.2f}")
# 保留两位小数，十个占位符，不足的使用0补充
prinf(f"{num:010.2f}")

4、填充和对齐经常是一起使用的
^、<、>: 分别是居中、左对齐、右对齐，后面带宽度。
:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充（一般不指定）。
personal = {"name": "Json", "age": 12, "sex": "M"}
# format
print("Name: {name:>5}, age: {age:>5}, sex: {sex:>5}".format(**personal))
# f-strings
print(f"Name: {personal['name']:^10}, age: {personal['age']:^10}, sex: {personal['sex']:^10}")

5、使用 !r可以给字符串添加引号
a = "abc"
b = "hjk"
# format
c = "{!r} -- {!r}".format(a, b) # "'abc' -- 'hjk'"
# f-string
c = f"{a!r} -- {b!r}" # "'abc' -- 'hjk'"


# 如果你学过Ruby，ES6，你会非常容易接受这样的语法。另外在速度上，f-strings是三种方案中最快的：
In: import timeit

In: timeit.timeit("""name = "Xiaoming"...: 'Hello is %s.' % name""",number =10000)
Out: 0.0023188740001387487

In: 'Hello is %s.'%name
Out: 'Hello is Xiaoming.'

In: timeit.timeit("""name = "Xiaoming"...: 'Hello is {}.'.format(name)""",number=10000)
Out: 0.0038487229999191186

In: timeit.timeit("""name = "Xiaoming"...: f'Hello is {name}.'""",number=10000)
Out: 0.0011758640002881293

# 可以侧面感受到，str.format最慢，%s的稍快一点，F-string是最快的！
# f-string是格式化字符串的新语法。与其他格式化方式相比，它们不仅更易读，更简洁，不易出错，而且速度更快！

\注意事项
1、{}内不能包含反斜杠\，但可以使用不同的引号，或使用三引号。使用引号是将不再表示一个变量，而是当作了字符串来处理。
2、如何插入大括号？
print(f"{{ 10 * 8 }}")
'{ 10 * 8 }'
print(f"{{ {10 * 8} }}")
'{ 80 }'




