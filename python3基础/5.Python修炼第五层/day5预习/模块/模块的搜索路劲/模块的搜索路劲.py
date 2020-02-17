# import time
# import importlib
# import spam
# time.sleep(10)
# # import spam
# # print(spam.money)
#
# importlib.reload(spam)
# print(spam.money)



# import sys
#
# print('time' in sys.modules)
# import time
# print('time' in sys.modules)
# # print(time)


# import sys
# import sys

#结论：
#注意： 自定义的模块名一定不要与Python自带的模块重名
# 内存中 --> 内置模块 --> 硬盘中
# 内存中 --> 内置模块 --> sys.path

import sys
# print(sys.path)
sys.path.append(r'D:\python编码\py_s19\day5\day5预习\模块\模块的搜索路劲\aaa')
import spam





