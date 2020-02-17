\1 什么是异常：程序运行时发生错误的信号（一旦出错，就会产生一个异常，
# 如果该异常没有被应用程序处理，那么该异常才会抛出来，程序也随之终止）
print('=====>')
print('=====>')
print('=====>')
aaa
print('=====>')
print('=====>')
print('=====>')


\2 异常分类
#分类一：针对语法上的异常，应该在程序执行前就解决掉
try:
    print('asdfasdf'
except Exception:
    pass

#分类二：逻辑异常，try...except
xxx #NameError

int('xxxxxxx') #valueError

l=[]
l[111111] #IndexError

d={}
d['a'] #keyError

1/0 #ZeroDivisionError:

import os
os.xxxxxxxxxxx #AttributeError:


\处理异常的方式：try 。。。except
import os
try:
    print('===>1')
    print('===>2')
    l=[]
    # l[123] # IndexError
    print('===>3')
    d={}
    # d['a'] # KeyError
    # aaa
    # os.xxxx
except AttributeError as x:
    import os
    os.xxx
    pass
except IndexError as y:
    print(x)
    l[0]
    pass
except Exception as z:  # 万能异常
    print('Ex',z)
else:
    print('被检测的代码块没有发生异常时执行else的代码')

print('====>4')
'''
===>1
===>2
===>3
被检测的代码块没有发生异常时执行else的代码
====>4
'''

# if 异常 == AttributeError:
#     x=异常值
# elif 异常 == IndexError:
#     x = 异常值


\处理异常的方式：try 。。。except。。。finally
try:
    print('===>1')
    print('===>2')
    cursor= connect(数据) # 伪代码
    cursor.excute(sql)
    cursor.excute(sql)
    cursor.excute(sql)
    cursor.excute(sql)

    print('===>3')
    d = {}

except Exception:
    print('异常发生时执行的代码')
    # cursor.close()
else:
    print('被检测的代码块没有发生异常时执行else的代码')
finally:
    print('不管程序是否出错，都会执行finally的代码')
    cursor.close()



\自定义异常
class MySQL_CONN_ERROR(BaseException): # 继承异常的父类 BaseException
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return '出错啦老铁：%s' %self.value

if 2 > 1:
    # raise TypeError('类型错误')
    # raise MyException('类型错误')
    raise MySQL_CONN_ERROR('数据库连接错误') # 在满足某种情况下 可以使用  raise 主动触发异常，使用raise和自定义异常类时要配合__str__一起使用。



\断言 （判定否个条件成立）
# assert 条1成立
# 通常在调试程序时使用
res=[]
if len(res) > 0:
    res[0]
    res[1]
else:
    # print('上一部分的代码有问题')
    raise PermissionError('xxxxx') 
'''
PermissionError: xxxxx
'''



res=[]
assert len(res) > 0  # 调试代码时比if判断好用，断定程序运行到这里条件是否成立。成立会继续运行下面的代码。
res[0]
res[1]  # AssertionError








