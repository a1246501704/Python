\1、示范文件
glance/                   #Top-level package

├── __init__.py           #Initialize the glance package

├── api                   #Subpackage for api

    ├── __init__.py

    ├── policy.py

    └── versions.py

├── cmd                #Subpackage for cmd

    ├── __init__.py

    └── manage.py

└── db                  #Subpackage for db

    ├── __init__.py

    └── models.py

#文件内容

#policy.py
def get():
    print('from policy.py')

#versions.py
def create_resource(conf):
    print('from version.py: ',conf)

#manage.py
def main():
    print('from manage.py')

#models.py
def register_models(engine):
    print('from models.py: ',engine)

包所包含的文件内容

执行文件与示范文件在同级目录下

\2、包的使用之import 
import glance.db.models
glance.db.models.register_models('mysql') 

单独导入包名称时不会导入包中所有包含的所有子模块，如
#在与glance同级的test.py中
import glance
glance.cmd.manage.main()

'''
执行结果：
AttributeError: module 'glance' has no attribute 'cmd'

'''

解决方法：
#glance/__init__.py
from . import cmd
 
#glance/cmd/__init__.py
from . import manage
执行：
#在于glance同级的test.py中
import glance
glance.cmd.manage.main()

\3、包的使用之from ... import ...

需要注意的是from后import导入的模块，必须是明确的一个不能带点，否则会有语法错误，如：from a import b.c是错误语法
from glance.db import models
models.register_models('mysql')
 
from glance.db.models import register_models
register_models('mysql')

\4、from glance.api import *
在讲模块时，我们已经讨论过了从一个模块内导入所有*，此处我们研究从一个包导入所有*。
此处是想从包api中导入所有，实际上该语句只会导入包api下__init__.py文件中定义的名字，我们可以在这个文件中定义__all___:
#在__init__.py中定义
x=10

def func():
    print('from api.__init.py')

__all__=['x','func','policy']

此时我们在于glance同级的文件中执行from glance.api import *就导入__all__中的内容（versions仍然不能导入）。

练习：
#执行文件中的使用效果如下，请处理好包的导入
from glance import *

get()
create_resource('a.conf')
main()
register_models('mysql')

#在glance.__init__.py中
from .api.policy import get
from .api.versions import create_resource

from .cmd.manage import main
from .db.models import  register_models

__all__=['get','create_resource','main','register_models']

\5、绝对导入和相对导入
我们的最顶级包glance是写给别人用的，然后在glance包内部也会有彼此之间互相导入的需求，这时候就有绝对导入和相对导入两种方式：
绝对导入：以glance作为起始
相对导入：用.或者..的方式最为起始（只能在一个包中使用，不能用于不同目录内）
例如：我们在glance/api/version.py中想要导入glance/cmd/manage.py

在glance/api/version.py

#绝对导入
from glance.cmd import manage
manage.main()

#相对导入
from ..cmd import manage
manage.main()

测试结果：注意一定要在于glance同级的文件中测试
from glance.api import versions 

\6、包以及包所包含的模块都是用来被导入的，而不是被直接执行的。而环境变量都是以执行文件为准的
比如我们想在glance/api/versions.py中导入glance/api/policy.py，有的同学一抽这俩模块是在同一个目录下，十分开心的就去做了，它直接这么做.
#在version.py中 
import policy
policy.get()
没错，我们单独运行version.py是一点问题没有的，运行version.py的路径搜索就是从当前路径开始的，于是在导入policy时能在当前目录下找到
但是你想啊，你子包中的模块version.py极有可能是被一个glance包同一级别的其他文件导入，比如我们在于glance同级下的一个test.py文件中导入version.py，如下
from glance.api import versions

'''
执行结果:
ImportError: No module named 'policy'
'''

'''
分析:
此时我们导入versions在versions.py中执行import policy需要找从sys.path也就是从当前目录找policy.py,这必然是找不到的
所以在version.py导入policy就要使用绝对路径，from glance.api import policy
'''

\7、 绝对导入与相对导入总结
绝对导入与相对导入

# 绝对导入: 以执行文件的sys.path为起始点开始导入,称之为绝对导入
#        优点: 执行文件与被导入的模块中都可以使用
#        缺点: 所有导入都是以sys.path为起始点,导入麻烦

# 相对导入: 参照当前所在文件的文件夹为起始开始查找,称之为相对导入
#        符号: .代表当前所在文件的文件加,..代表上一级文件夹,...代表上一级的上一级文件夹
#        优点: 导入更加简单
#        缺点: 只能在导入包中的模块时才能使用
　　　　  #注意:
　　　　　　　　1. 相对导入只能用于包内部模块之间的相互导入,导入者与被导入者都必须存在于一个包内
　　　　　　　　2. attempted relative import beyond top-level package # 试图在顶级包之外使用相对导入是错误的,言外之意,必须在顶级包内使用相对导入,每增加一个.代表跳到上一级文件夹,而上一级不应该超出顶级包

