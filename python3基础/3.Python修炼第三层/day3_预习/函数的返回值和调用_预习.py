
#函数的返回值和函数调用的三种形式

# def func():
#     print('from func')
#     # return 0
#
# res=func()
# print(res)

'''
大前提：return的返回值没有类型限制
    1.没有return: 返回None 等同于return None
    2.return 一个值：返回该值
    3.return val1,val2,val3: 返回：(val1,val2,val3)

返回值
　　什么时候该有？
　　　　调用函数，经过一系列的操作，最后要拿到一个明确的结果，则必须要有返回值
　　　　通常有参函数需要有返回值，输入参数，经过计算，得到一个最终的结果
　　什么时候不需要有？
　　　　调用函数，仅仅只是执行一系列的操作，最后不需要得到什么结果，则无需有返回值
　　　　通常无参函数不需要有返回值

'''

# def my_max(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# my_max(1,2) #语句形式
#
# res=my_max(1,2)*10 #表达式形式
#
# # res1=my_max(1,2)
# # res2=my_max(res1,3)
#
# res2=my_max(my_max(1,2),3) #函数调用可以当做另外一个函数的参数
# print(res2)









