
#函数参数
#位置参数与关键字参数

#形参：在定义函数时，括号内的参数成为形参
#特点：形参就是变量名
# def foo(x,y): # x=1,y=2
#     print(x)
#     print(y)

#实参：在调用函数时，括号内的参数成为实参
#特点：实参就是变量值
# foo(1,2)

#在调用阶段实参（变量值）才会绑定形参（变量名）
#调用结束后，解除绑定





#参数的分类

#位置参数：按照从左到右的顺序，依次定义的参数
    #位置形参：必选被传值，多一个不行，少一个也不行
    #位置实参：与形参按照位置一一对应

# def foo(x,y):
#     print(x)
#     print(y)
#
# foo('egon',2)


#关键字实参：指的是key=value的形式，指名道姓地给name传值
# def foo(name,age):
#     print(name)
#     print(age)

# foo('egon',18) #位置实参
# foo(age=18,name='egon') #关键字实参

#关键字实参需要注意的问题是：
# def foo(name,age,sex):
#     print(name)
#     print(age)
#     print(sex)
# foo('egon',18,'male')
# print('=======>')
# foo(sex='male',age=18,name='egon')
# foo('egon',sex='male',age=18)

#问题一:语法规定 位置实参必须在关键字实参的前面
# foo('egon',sex='male',age=18)

#问题二:一定不要对同一个形参传多次值
# foo('egon',sex='male',age=18,name='egon1')

#错误，违反了规则
# foo('male',age=18,name='egon1')





#默认参数

#默认形参：在定义阶段，就已经为形参赋值，意味在调用阶段可以不用传值
# def foo(x,y=11111):
#     print(x)
#     print(y)
# foo(1)  #y形参已经被定义好，所以只传未定义形参x的实参
# foo(1,'a') #在实参调用时，会覆盖形参的定义


# 当所有调用的都是 一个值的时候 可以设置成 默认形参

# def register(name,age,sex='male'):
#     print(name,age,sex)
#
# register('asb',73)
# register('wsb',38)
# register('ysb',84)
# register('yaya',28,'female')

#默认参数需要注意的问题
#问题一：默认参数必须放在位置参数之后
# def foo(y=1,x):
#     print(x,y)

# 问题二：默认参数只在定义阶段赋值一次，而且仅一次
# x=100
# def foo(a,b=x):
#     print(a,b)
# x=11111
# foo('egon')

# 问题三：默认参数的值应该定义成不可变类型









