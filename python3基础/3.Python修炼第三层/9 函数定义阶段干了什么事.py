\函数在定义阶段，只检测语法，不执行代码
# 也就说，语法错误在函数定义阶段就会检测出来，而代码的逻辑错误只有在执行时才会知道
def func():
    print('aaaaaa')
    xxxxx
    yyyy
    zzssaa
    asdfasdfasdfasdf
    # if # 打开这两行时下面不用func()调用，检测语法就会报错。
    # print('asdfasdfasfd'

# func() # 开始调用函数，执行代码