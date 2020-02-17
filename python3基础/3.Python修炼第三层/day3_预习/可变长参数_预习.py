
# 可变长参数与命名关键字参数

# 可变长参数: 指的是实参的个数多了
# 实参无非位实参和关键字实参两种

# 形参必须要有两种机制分别处理按照位置定义的实参溢出的情况
# 跟按照关键字定义的实参溢出的情况：****

#*args 潜规则写法
# def foo(x,y,*args): # *会把多出来的位置实参 交给(存成元组) args=(3,4,5,6,7)
#     print(x)
#     print(y)
#     print(args)

# foo(1,2,3,4,5,6,7) # *args 潜规则写法
# foo(1,2) #*



# *args 的扩展用法
# def foo(x,y,*args): # *args=*(3,4,5,6,7)
#     print(x)
#     print(y)
#     print(args)
#
# # foo(1,2,3,4,5,6,7) #*
#
# foo(1,2,*(3,4,5,6,7)) #foo(1,2,3,4,5,6,7))

# def foo(x,y): #
#     print(x)
#     print(y)
# foo(1,*(3,)) #
# foo(*(3,2)) #

# def foo(x,y=1,*args): #
#     print(x)
#     print(y)
# # foo('a','b',*(1,2,3,4,5,6,7)) #foo('a','b',1,2,3,4,5,6,7)
# ##foo('egon',10,2,3,4,5,6,9,y=2) #报错 不能赋予值两次
# foo('egon',10,2,3,4,5,6,9)



# *kwargs 潜规则写法
# def foo(x,y,**kwargs): # **会把多出来的定义实参 交给(存成字典) kwargs={'z': 3, 'a': 1, 'b': 2}
#     print(x)
#     print(y)
#     print(kwargs)
# foo(1,2,'z'=3,'a'=1,'b'=2) #** kwargs 潜规则写法

# def foo(x,y,**kwargs): # kwargs={'z': 3, 'a': 1, 'b': 2}
#     print(x)
#     print(y)
#     print(kwargs)
# foo(1,2,**{'z':3,'a':1,'b':2}) #foo(1,2,'z':3,'a':1,'b':2)

# def foo(x,y,): #
#     print(x)
#     print(y)
# foo(**{'y':1,'x':2}) #foo('a':1,'b':2)


# def foo(x,*args,**kwargs): #args=(2,3,4,5) kwargs=('b':1,'a':2)
#     print(x)
#     print(args)
#     print(kwargs)
#
# foo(1,2,3,4,5,b=1,a=2)


#这俩东西*args,**kwargs 干什么用
# def register(name,age,sex='male'):
#     print(name)
#     print(age)
#     print(sex)

# def wrapper(*args,**kwargs): #args=(1, 2, 3, 4) kwargs={'a': 1, 'b': 2}
#     # print(args)
#     # print(kwargs)
#     register(*args,**kwargs)
#     #register(*(1, 2, 3),**{'a': 1, 'b': 2})
#     #register(1,23,a=1,b=2)
#
# wrapper(1,2,3,a=1,b=2)


# import time
#
# def register(name,age,sex='male'):
#     # start_time=time.time()
#     print(name)
#     print(age)
#     print(sex)
#     time.sleep(3)
#     # stpo_time=time.time()
#     # print('run time is %s' %(stpo_time-start_time))
# def wrapper(*args,**kwargs): # 收  args=('egon') kwargs={'age':18}
#     start_time=time.time()
#     register(*args,**kwargs) # 给  # register('egon',age=18)
#     stpo_time=time.time()
#     print('run time is %s' %(stpo_time-start_time))
#
# wrapper('egon',age=18)
#
# # register('egon',18)



#命名关键字参数：在*后面定义的形参称为命名关键字参数，必须是被以关键字实参的形式传值
# def foo(name,age,*args,sex='male',group):
#     print(name)
#     print(age)
#     print(args)
#     print(sex)
#     print(group)
#
# foo('alex',18,19,20,300,group='group1',sex='male')


# 场景很少  全部放一起
# def foo(name,age=18,*args,sex='male',group,**kwargs):
#     pass





















