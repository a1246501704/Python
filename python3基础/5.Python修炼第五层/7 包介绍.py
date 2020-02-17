\1、什么是包？
#官网解释
Packages are a way of structuring Python’s module namespace by using “dotted module names”
包是一种通过使用“.模块名”来组织python模块名称空间的方式。
#具体的：包就是一个包含有__init__.py文件的文件夹，所以其实我们创建包的目的就是为了用文件夹将文件/模块组织起来

#需要强调的是：
　　1. 在python3中，即使包下没有__init__.py文件，import 包仍然不会报错，而在python2中，包下一定要有该文件，否则import包会报错。
　　2. 创建包的目的不是为了运行，而是被导入使用，记住，包只是模块的一种形式而已，包的本质就是一种模块。

\2、为何要使用包
包的本质就是一个文件夹，那么文件夹唯一的功能就是将文件组织起来.随着功能越写越多，我们无法将所以功能都放到一个文件中，于是我们使用模块去组织功能，
而随着模块越来越多，我们就需要用文件夹将模块文件组织起来，以此来提高程序的结构性和可维护性。

\3、注意事项
# 1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：凡是在导入时带点的，
#   点的左边都必须是一个包，否则非法。可以带有一连串的点，如item.subitem.subsubitem,但都必须遵循这个原则。但对于导入后，在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
# 2、import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件。
# 3、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间

\案例文件：“7 包的使用，test.py是执行文件，aaa是包。”

有点像俄罗斯套娃,也和linux路径的绝对路径一个意思。

\4、上课流程
# 1 实验一
    准备：
        执行文件为test.py，内容
        #test.py
        import aaa
        同级目录下创建目录aaa,然后自建空__init__.py(或者干脆建包)

    需求：验证导入包就是在导入包下的__init__.py

    解决：
        先执行看结果
        再在__init__.py添加打印信息后，重新执行.导入aaa会出发__init__的执行。

# 2、实验二
    准备：基于上面的结果

    需求：
        aaa.x
        aaa.y
    解决：在__init__.py中定义名字x和y

# 3、实验三
    准备：在aaa下建立m1.py和m2.py
        #m1.py
        def f1():
            print('from 1')
        #m2.py
        def f2():
            print('from 2')
    需求：
        aaa.m1 #进而aaa.m1.f1()
        aaa.m2 #进而aaa.m2.f2()

    解决：在__init__.py中from aaa import m1,m2,强调: 环境变量(模块搜索路径)是以执行文件为准.
    # from aaa import m1
    # from aaa import m2
    # __init__相当于是执行文件和包之间的桥梁，执行文件执行会触发__init__文件执行，__init__文件中去导入包。
    需求
        aaa.f1 #进而aaa.f1()
        aaa.f2 #进而aaa.f2()
    # from aaa.m1 import f1
    # from aaa.m2 import f2
    
# 4、实验四
    准备：在aaa下新建包bbb

    需求：
        aaa.bbb

    解决：在aaa的__init__.py内导入名字bbb
    # from aaa import bbb

# 5、实验五
    准备：
        在bbb下建立模块m3.py
        #m3.py
        def f3():
            print('from 3')
    需求：
        aaa.bbb.m3 #进而aaa.bbb.m3.f3()

    解决：是bbb下的名字m3，因而要在bbb的__init__.py文件中导入名字m3
    # from aaa.bbb import m3


# 6、实验六
    准备：基于上面的结果

    需求:
        aaa.m1()
        aaa.m2()
        aaa.m3()
        进而实现
        aaa.f1()
        aaa.f2()
        aaa.f3()
        先用绝对导入，再用相对导入
        
    解决：在aaa的__init__.py中拿到名字m1、m2、m3
    # from aaa.m1 import f1
    # from aaa.m2 import f2
    # from aaa.bbb.m3 import f3
    包内模块直接的相对导入，强调包的本质：包内的模块是用来被导入的，而不是被执行的
    用户无法区分模块是文件还是一个包，我们定义包是为了方便开发者维护

# 7、实验七
    将包整理当做一个模块，移动到别的目录下xxx/yyy下，保证不影响使用。就好像包移动了位置或者是下载别人的包。
    操作sys.path
    import sys
    sys.path.append(r'/Users/zhanghongyang/Documents/软通动力/Github/python3基础/5.Python修炼第五层/7 包的使用/xxx/yyy') # 将test.py执行文件平级的yyy加入到环境变量即可。

