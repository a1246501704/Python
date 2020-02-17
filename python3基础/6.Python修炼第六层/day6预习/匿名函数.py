
#正常函数  def定义
def func(x,y,z=1):
    return x+y+z

# def func(x,y,z=1):return x+y+z
# print(func)
# print(func(1,2,3,))


#匿名函数  lambda定义 : 1.没有名字 2.函数体自带return
print(lambda x,y,z=1:x+y+z)


#匿名函数的应用场景:
#应用于一次性的场景，临时使用



