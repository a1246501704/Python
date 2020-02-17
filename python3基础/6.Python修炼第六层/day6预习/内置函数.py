
#取绝对值  负得正
# print(abs(-1))

#需要传入 可迭代对象，当all里面的所有值都为True才返回true
# print(all([1,2,'a',None]))

#如果可迭代对象为空 返回True
# print(all([]))

#如果可迭代对象为空 返回False
#bool值为假的情况：None,空，0，False
# print(any([])) #False
# print(any([' ',None,False])) #True
# print(any(['',None,False,1])) #False

#bin,oct,hex
# print(bin(10))
# print(oct(10))
# print(hex(10))

#bytes 字节
#unicode---->encode---->bytes
# print('hello'.encode('utf-8'))
# print(bytes('hello',encoding='utf-8'))

#callable  是否能被调用
#变量是引用，函数才是调用，加括号执行的才是调用
# print(callable(bytes))
# print(callable(abs))

#chr,ord  对应ASCII表
# print(chr(65))
# print(chr(90))
#
# print(ord('#'))











#
# int
# x=1 #x=int(1)
# print(type(x))
#
# x=int(2)

# complex
# float
#
# str
# list
# tuple
# dict
#
# set  #可变集合
# frozenset #不可变集合

# s={1,2,3,4} #s=set({1,2,3,4})
# print(type(s))
#
# s1=frozenset({1,2,3,4})
# print(type(s1))


#
# import sys
# sys.path
# sys.argv
# print(dir(sys))

#divmod
# print(divmod(10,3))  #(3,1)
# print(divmod(102,20))  #(5,2)


# #enumerate  取出元素加索引
# l=['a','b','c']
# res=enumerate(l)
# for i in res:
#     print(i)



#globals,locals #查看全局作用与局部作用域
# print(globals())



#bash
# print(hash('abcdefg123'))
# print(hash('abcdefg123'))
# print(hash('abcdefg123'))


# #给函数加文档解释，用到单引号，双引号，三引号
# def func():
#     '''
#     test funcion
#     :return:
#     '''
#     pass
#
# print(help(func))


# #id :只是python解释器实现的功能，只是反映了变量在内存的地址
# #    但并不是真实的内存地址
# x=1
# print(id(x))
#
# def func():pass
# print(id(func))
# print(func)



# isinstance  判断一个变量的类型
# x=1
# print(type(x) is int)
# print(isinstance(x,int)) #x=int(1)




#迭代器
# iter
# next


#len
#max
# print(max([1,2,3,10]))
# print(max(['a','b','c']))
# print(min([1,2,3,10]))

#pow
# print(pow(3,2))    #3**2
# print(pow(3,2,2))  #3**2%2

#tange

#repr(解释器内部用的转换),str(用户看的)
# print(type(str(1)))
# print(type(repr(1)))

#reversed  #反转
# l=[1,'a',2,'c']
# print(list(reversed(l)))  #反转成新列表，对原列表不修改
# print(l)

# slice  #切片
# l=[1,2,3,4,5,6]
# print(l[0:4:2])
#
# s=slice(0,4,2)
# print(l[s])

#sorted  #排序
# l=[1,10,4,3,-1]
# print(sorted(l))  #排序 升序
# print(sorted(l,reverse=True)) #降序

#sum  #求和
# print(sum([1,2,3]))
#
# print(sum(i for i in range(10)))


#round  #保留几位小数，四舍五入
# print(round(3.567,2))
# print(round(3.565,2))  #有坑，结果是3.56，并不是3.57
# print(round(3.564,2))


#filer,map,reduce  重点
#max min sorted


#vars   #没有参数与locals()相等，有参数与object.__dict__相等
# import m1  #自定义函数
# print(m1.__dict__)
# print(vars(m1))
# print(vars(m1) == m1.__dict__)

#zip :拉链
# s='hello'
# l=[1,2,3,4,5]
# # res=zip(s,l)
# # print(list(res))
# print(list(zip(s,l)))


# __import__
# import sys
#
# m_name=input('module>>: ')
# if m_name == 'sys':
#     m=__import__(m_name)
#     print(m)
#     print(m.path)



#面向对象
# object

# super

# __dict__

# isinstance

# issubclass

# classmethod
# staticmethod
# property


# delattr
# hasattr
# setattr
# getattr




# #了解
# compile
# eval
# exec





