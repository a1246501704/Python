#导入包实际上就是在导入包下面的__init__.py文件

# import sys
# print(sys.path)

# import aaa


# print(aaa.x)
# print(aaa.y)

# print(aaa.m1)
# aaa.m1.f1()
# aaa.m2.f2()

# print(aaa.f1)
# aaa.f1() # 在__init__.py中先导入aaa包的f1功能，from aaa.m1 import f1。
# aaa.f2()


# import aaa
# print(aaa.bbb.x)

# aaa.bbb.m3.f3()

# print(aaa.f3)
# aaa.f3()

# 把包的路径添加到环境变量中
import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\python19期\day5\7 包的使用\xxx\yyy')

# import aaa
#
# aaa.f1()
# aaa.f2()
# aaa.f3()


# from aaa.ccc.m4 import f4
# f4()

import aaa.ccc.m4
aaa.ccc.m4.f4()











