
\六、模块的查找顺序是：内存中已经加载的模块->内置模块->sys.path路径中包含的模块
#模块的查找顺序
1、在第一次导入某个模块时（比如spam），会先检查该模块是否已经被加载到内存中（当前执行文件的名称空间对应的内存），如果有则直接引用。
    ps：python解释器在启动时会自动加载一些模块到内存中，可以使用sys.modules查看。
2、如果没有，解释器则会查找同名的内建模块。
3、如果还没有找到就从sys.path（当前执行文件的路径）给出的目录列表中依次寻找spam.py文件。


#sys.path的初始化的值来自于：
The directory containing the input script (or the current directory when no file is specified).
PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
The installation-dependent default.

\需要特别注意的是：我们自定义的模块名不应该与系统内置模块重名。虽然每次都说，但是仍然会有人不停的犯错。 

#在初始化后，python程序可以修改sys.path,路径放到前面的优先于标准库被加载。
1 >>> import sys
2 >>> sys.path.append('/a/b/c/d')  # 添加搜索路径
3 >>> sys.path.insert(0,'/x/y/z')  # 插入到最前面，排在前的目录，优先被搜索。

注意：搜索时按照sys.path中从左到右的顺序查找，位于前的优先被查找，sys.path中还可能包含.zip归档文件和.egg文件，python会把.zip归档文件当成一个目录去处理。
#首先制作归档文件：zip module.zip foo.py bar.py 
import sys
sys.path.append('module.zip')
import foo,bar

#也可以使用zip中目录结构的具体位置
sys.path.append('module.zip/lib/python')


#windows下的路径不加r开头，会语法错误
sys.path.insert(0,r'C:\Users\Administrator\PycharmProjects\a')
 

#至于.egg文件是由setuptools创建的包，这是按照第三方python库和扩展时使用的一种常见格式，.egg文件实际上只是添加了额外元数据(如版本号，依赖项等)的.zip文件。
#需要强调的一点是：只能从.zip文件中导入.py，.pyc等文件。使用C编写的共享库和扩展块无法直接从.zip文件中加载（此时setuptools等打包系统有时能提供一种规避方法），且从.zip中加载文件不会创建.pyc或者.pyo文件，因此一定要事先创建他们，来避免加载模块是性能下降。


import time,sys
print(sys)

import time
time.sleep(3)

import sys
print(sys.path)

import xxx
import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\python19期\day5\a')


# import m
from a import m  # 因为a目录和当前执行文件就在同一级目录下，所以不sys.path.append也能直接找到。

