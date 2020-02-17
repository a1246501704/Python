# import sys
# print(sys.path)
#
#凡是在导入时带点的，点的左边都必须是一个包
#只有在导入包的时候才能在文件名后面加. 导入模块时不能用.
import aaa

# print(aaa)
# print(aaa.x)
# print(aaa.y)

# print(aaa.m1)
# aaa.m1.func1()

# print(aaa.bbb.m3)
# aaa.bbb.m3.func3()

# aaa.func1()
# aaa.func2()
# aaa.func3()

# import aaa.bbb.m3 as abm
# abm.func3()

import sys
sys.path.append(r'D:\python编码\py_s19\day5\day5预习\a')
import glance_v1

glance_v1.get()
# glance_v1.create_resource('test.conf')
# glance_v1.main()
# glance_v1.register_models('mysql')




