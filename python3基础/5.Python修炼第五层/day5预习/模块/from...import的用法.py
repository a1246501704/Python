# 优点：使用源文件内的名字时无需加前缀，使用方便
# 缺点：容易与当前文件的名称空间内的名字混淆

# from spam import money,read1,read2,change
# money=0
# print(money)
# print(read1)
#
# read1()

# def read1():print('ok')
# read2()

# money=10
# change()
# print(money)


# from spam import money as m
#
# print(m)


# 不推荐使用 *  只有在源文件里面的名字太多了，而且调用的也多的情况下才使用
# * 表示 除了 _ 下滑线开头名字 以外的名字
from spam import *

# print(money)
# read1()






