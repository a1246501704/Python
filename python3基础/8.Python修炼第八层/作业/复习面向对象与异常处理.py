#!/usr/bin/env python
#_*_coding:utf-8_*_


#抽象方法
@staticmethod 不能访问类的任何属性
@classmethod  类方法 只能访问公有属性
@property 属性方法,把一个方法变成静态属性

def sayhi()
    pass

@sayhi.setter
def sayhi(k):

@sayhi.deleter
def sayhi():

__call__()  : 实例 + () 会触发 call method

__dict__ 打印实例中所有属性

__getitem__ 以字典的形式操作实例

__new__ 先于 __init__ 执行,可以在 __new__ 中自定义类的实例化过程

__str__ 返回实例的字符串形式

__metaclass__ 元类

type() 可以动态创建一个类
    python 里面一切皆对象
    类本身就是一个对象,类就是type生成的对象

    类是怎么实例化的?
    类实例化时 加() 就是触发 __call__ 方法
    __call__ 方法就是生成 你想要的实例


# 异常抓取
try ... except
    IOError
    ValueError
    IndexError
    IndentationError
    TypeError

    解释器语法解析都无法通过 所以无法抓取
        IndentationError
        SyntaxError

try

except IndexError as e:
    pass
except (IndexError,IndentationError) as e:
    print(e)

else: #当前面的try 没有错误 才执行这个else

raise: 手动触发异常


assert 判断后面的结果必须为 True


#动态导入模块
__import__('day9.testmod')


#反射：通过字符串的形式 获取这个指定数据的属性
hasattr
getattr
setattr
delattr

# socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
conn,clientaddr = s.accept

conn.send
















