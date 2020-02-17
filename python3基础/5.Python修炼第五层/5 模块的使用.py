\一、模块介绍
\1、什么是模块？
模块就是一组功能的集合体，我们的程序可以导入模块来复用模块里的功能。

#常见的场景：一个模块就是一个包含了一组功能的python文件,比如spam.py，模块名为spam，可以通过import spam使用。
#在python中，模块的使用方式都是一样的，但其实细说的话，模块可以分为四个通用类别：　
　　1 使用python编写的.py文件
　　2 已被编译为共享库或DLL的C或C++扩展
　　3 把一系列模块组织到一个文件夹中（注：文件夹下有一个__init__.py文件，该文件夹称之为包）
　　4 使用C编写并链接到python解释器的内置模块

\2、为何要使用模块？
#1、从文件级别组织程序，更方便管理。
随着程序的发展，功能越来越多，为了方便管理，我们通常将程序分成一个个的文件，这样做程序的结构更清晰，方便管理。
这时我们不仅仅可以把这些文件当做脚本去执行，还可以把他们当做模块来导入到其他的模块中，实现了功能的重复利用。
#2、拿来主义，提升开发效率
同样的原理，我们也可以下载别人写好的模块然后导入到自己的项目中使用，这种拿来主义，可以极大地提升我们的开发效率。
#ps：
如果你退出python解释器然后重新进入，那么你之前定义的函数或者变量都将丢失，因此我们通常将程序写到文件中以便永久保存下来，
需要时就通过python test.py方式去执行，此时test.py被称为脚本script。

\3、以spam.py为例来介绍模块的使用：文件名spam.py,模块名就是脚本名去掉.py即spam。
#spam.py
print('from the spam.py')

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0

\二、使用模块之import
\1、import的使用
#模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，它们只在模块名第一次遇到导入import语句时才执行（import语句是可以在程序中的任意位置使用的,
#且针对同一个模块很import多次,为了防止你重复导入，python的优化手段是：第一次导入后就将模块名加载到内存了，后续的import语句仅是对已经加载到内存中的模块对象增加了一次引用，不会重新执行模块内的语句），如下 

#test.py
import spam #只在第一次导入时才执行spam.py内代码,此处的显式效果是只打印一次'from the spam.py',当然其他的顶级代码也都被执行了,只不过没有显示效果.
import spam
import spam
import spam

'''
执行结果：
from the spam.py
'''
ps：我们可以从sys.module中找到当前已经加载的模块，sys.module是一个字典，内部包含模块名与模块对象的映射，该字典决定了导入模块时是否需要重新导入。

\2、在第一次导入模块时会做三件事，重复导入会直接引用内存中已经加载好的结果
    1.为源文件(spam模块)创建新的名称空间，在spam中定义的函数和方法若是使用到了global时访问的就是这个名称空间。
    2.在新创建的命名空间中执行模块中包含的代码，见初始导入import spam
    3.会在当前文件中定义一个名字，这个名字就是模块名，用来引用模块中的名字。

\3、被导入模块有独立的名称空间
每个模块都是一个独立的名称空间，定义在这个模块中的函数，把这个模块的名称空间当做全局名称空间，这样我们在编写自己的模块时，
就不用担心我们定义在自己模块中全局变量会在被导入时，与使用者的全局变量冲突.

\第一部分：import

# 导入模块，只会在第一次导入时执行源文件的代码。如果模块已经加载到内存了，下一次导入直接引用内存中导入的结果。
import spam #m1=111111
import spam #m2=m1
import spam
import spam
import spam
import spam

import sys
print('spam' in sys.modules) # 查看spam模块系统是否已经加载。

测试一: money与spam.money不冲突,各自使用各自命名空间的值。
#test.py
import spam 
money=10
print(spam.money)

'''
执行结果：
from the spam.py
1000
'''

测试二: read1与spam.read1不冲突,各自使用各自命名空间的值。
#test.py
#test.py
import spam
spam.read1() # spam模块： 1000


import spam
def read1():
    print('========')
spam.read1()

'''
执行结果:
from the spam.py
spam->read1->money 1000
'''
测试三: 执行spam.change()操作的全局变量money仍然是spam中的
#test.py
import spam
money=1
spam.change()
print(money)

'''
执行结果：
from the spam.py
1
'''
注意：上述几个测试都是明确指定了模块名，spam.xxxx  所以都是使用的spam空间的值，当直接使用from spam import read1时 直接使用read1()时就要关注本空间是否有此函数了。

\4、为模块起别名
# 为已经导入的模块起别名的方式对编写可扩展的代码很有用
import spam as sm
print(sm.money) # 1000

# 利用别名的机制实现一些可扩展的功能
例如：当有多种数据库引擎时，可以用if判断的方式来import不同的引擎模块。而代码却不需要改动。
#mysql.py
def sqlparse():
    print('from mysql sqlparse')
#oracle.py
def sqlparse():
    print('from oracle sqlparse')

#test.py
db_type=input('>>: ')
if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db

db.sqlparse()
# 假设有两个模块xmlreader.py和csvreader.py，它们都定义了函数read_data(filename):用来从文件中读取一些数据，但采用不同的输入格式。可以编写代码来选择性地挑选读取模块
if file_format == 'xml':
    import xmlreader as reader
elif file_format == 'csv':
    import csvreader as reader
data=reader.read_date(filename)

\5、在一行导入多个模块
import spam
import time
或者
import spam,time


\三、使用模块之from ... import...

\1、第二部分：from...import...
from spam import read1,read2 # 导入模块的部分功能使用

\2、from...import 与import的对比
# 唯一的区别就是：使用from...import...则是将spam中的名字直接导入到当前的名称空间中，所以在当前名称空间中，直接使用名字就可以了、无需加前缀：spam.
# from...import...的方式有好处也有坏处
    好处：使用起来方便了
    坏处：容易与当前执行文件中的名字冲突


# 测试一：导入的函数read1，执行时仍然回到spam.py中寻找全局变量money
#test.py
from spam import read1
money=1
print(money) 
read1()
'''
执行结果:
from the spam.py
1
spam->read1->money 1000
'''
验证一：当前位置直接使用read1和read2就好了，执行时，仍然以spam.py文件全局名称空间

# 测试二:导入的函数read2，执行时需要调用read1(),仍然回到spam.py中找read1()
#test.py
from spam import read2
def read1():
    print('==========')
read2()
'''
执行结果:
from the spam.py
spam->read2 calling read
spam->read1->money 1000
'''
验证二：如果当前有重名read1或者read2，那么会有覆盖效果。

# 测试三:导入的函数read1，被当前位置定义的read1覆盖掉了
#test.py
from spam import read1
def read1():
    print('==========')
read1()
'''
执行结果:
from the spam.py
==========
'''
验证三：导入的方法在执行时，始终是以源文件为准的。
from spam import money,read1
money=100    # 将当前位置的名字money绑定到了100
print(money) # 打印当前的名字
read1()      # 读取spam.py中的名字money,仍然为1000

'''
from the spam.py
100
spam->read1->money 1000
'''


\3、也支持as
from spam import read1 as read

\4、一行导入多个名字
from spam import read1,read2,money

\5、from...import *  函数内部不能使用带 * 的语法，不带*的可以。
#from spam import * 把spam中所有的不是以下划线(_)开头的名字都导入到当前位置。
#大部分情况下我们的python程序不应该使用这种导入方式，因为*你不知道你导入什么名字，很有可能会覆盖掉你之前已经定义的名字。而且可读性极其的差，在交互式环境中导入时没有问题。
from spam import * # 将模块spam中所有的名字都导入到当前名称空间
print(money)
print(read1)
print(read2)
print(change)

'''
执行结果:
from the spam.py
1000
<function read1 at 0x1012e8158>
<function read2 at 0x1012e81e0>
<function change at 0x1012e8268>
'''
可以使用__all__来控制*（用来发布新版本），在spam.py中新增这一行。__all__仅用于*的控制。
__all__=['money','read1'] #这样在另外一个文件中用from spam import * 就只能导入列表中规定的两个模块中的方法名字。

\from glance.api import *
在讲模块时，我们已经讨论过了从一个模块内导入所有*，此处我们研究从一个包导入所有*。
此处是想从包api中导入所有，实际上该语句只会导入包api下__init__.py文件中定义的名字，我们可以在这个文件中定义__all___:

\6、模块循环导入问题
模块循环/嵌套导入抛出异常的根本原因是由于在python中模块被导入一次之后，就不会重新导入，只会在第一次导入时执行模块内代码。
在我们的项目中应该尽量避免出现循环/嵌套导入，如果出现多个模块都需要共享的数据，可以将共享的数据集中存放到某一个地方。

在程序出现了循环/嵌套导入后的异常分析、解决方法如下。
#示范文件内容如下
#m1.py
print('正在导入m1')
from m2 import y

x='m1'

#m2.py
print('正在导入m2')
from m1 import x

y='m2'

#run.py
import m1

#测试一
执行run.py会抛出异常
正在导入m1
正在导入m2
Traceback (most recent call last):
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/aa.py", line 1, in <module>
    import m1
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/m1.py", line 2, in <module>
    from m2 import y
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/m2.py", line 2, in <module>
    from m1 import x
ImportError: cannot import name 'x'

#测试一结果分析
先执行run.py--->执行import m1，开始导入m1并运行其内部代码--->打印内容"正在导入m1"--->执行from m2 import y 开始导入m2并运行其内部代码
--->打印内容“正在导入m2”--->执行from m1 import x,由于m1已经被导入过了，所以不会重新导入，所以直接去m1中拿x，然而x此时并没有存在于m1中，所以报错


#测试二:执行文件不等于导入文件，比如执行m1.py不等于导入了m1
直接执行m1.py抛出异常
正在导入m1
正在导入m2
正在导入m1
Traceback (most recent call last):
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/m1.py", line 2, in <module>
    from m2 import y
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/m2.py", line 2, in <module>
    from m1 import x
  File "/Users/linhaifeng/PycharmProjects/pro01/1 aaaa练习目录/m1.py", line 2, in <module>
    from m2 import y
ImportError: cannot import name 'y'


#测试二分析
执行m1.py，打印“正在导入m1”，执行from m2 import y ，导入m2进而执行m2.py内部代码--->打印"正在导入m2"，执行from m1 import x，
此时m1是第一次被导入，执行m1.py并不等于导入了m1，于是开始导入m1并执行其内部代码--->打印"正在导入m1"，执行from m1 import y，由于m1已经被导入过了，所以无需继续导入而直接问m2要y，然而y此时并没有存在于m2中所以报错



# 解决方法:
方法一:导入语句放到最后
#m1.py
print('正在导入m1')

x='m1'

from m2 import y

#m2.py
print('正在导入m2')
y='m2'

from m1 import x

方法二:导入语句放到函数中
#m1.py
print('正在导入m1')

def f1():
    from m2 import y
    print(x,y)

x = 'm1'

# f1()

#m2.py
print('正在导入m2')

def f2():
    from m1 import x
    print(x,y)

y = 'm2'

#run.py
import m1

m1.f1()

思考：
#m1.py
f1()
print('正在导入m1')
import m2

x='m1'

print(m2.y)


#m2.py
print('正在导入m2')
import m1

y='m2'

#run.py
import m1

\四、模块的重载 (了解)
考虑到性能的原因，每个模块只被导入一次,放入字典sys.module中，如果你改变了模块的内容，你必须重启程序，python不支持重新加载或卸载之前导入的模块，
有的同学可能会想到直接从sys.module中删除一个模块不就可以卸载了吗，注意了，你删了sys.module中的模块对象仍然可能被其他程序的组件所引用，因而不会被清除。
特别对于我们引用了这个模块中的一个类，用这个类产生了很多对象，因而这些对象都有关于这个模块的引用。

如果只是你想交互测试的一个模块，使用 importlib.reload()重新加载模块, import importlib; importlib.reload(modulename)，这只能用于测试环境。

aa.py的初始内容：
def func1():
    print('func1')

执行test.py：
import time,importlib
import aa
 
time.sleep(20)
# importlib.reload(aa)
aa.func1()

在20秒的等待时间里，修改aa.py中func1的内容，等待test.py的结果。打开importlib注释，重新测试。

\五、py文件区分两种用途:模块与脚本
#编写好的一个python文件可以有两种用途：
    一：脚本，一个文件就是整个程序，用来被执行
    二：模块，文件中存放着一堆功能，用来被导入使用

#python为我们内置了全局变量__name__，
    当文件被当做脚本执行时：__name__ 等于'__main__'。在执行文件内print(__name__)结果是执行文件自己的名字。
    当文件被当做模块导入时：__name__等于模块名（文件名）。在被导入模块内print(__name__)，在执行文件内导入后执行。

#作用：用来控制.py文件在不同的应用场景下执行不同的逻辑
    if __name__ == '__main__':

#fib.py
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))


#执行：python fib.py <arguments>
python fib.py 50 #在命令行