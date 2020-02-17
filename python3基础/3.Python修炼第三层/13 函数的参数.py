\一、形参与实参
#形参即变量名，实参即变量值，函数调用时，将值绑定到变量名上，函数调用结束，解除绑定。
# 形参：在函数定义阶段，括号内定义的参数的称为形参,就相当于变量名。分为：位置形参、默认参数
# 实参：在函数调用阶段，括号内定义的参数的称为实参，就相当于变量值。分为：位置实参、关键字实参
# 在调用阶段，实参的值会绑定给形参，在调用结束后，解除绑定

def foo(x,y): #x=1,y=2
    print(x,y)

foo(1,2)

\参数的分类

\一: 位置参数
'''
位置参数：按照从左到右的顺序定义的参数
        位置形参：必须被传值的参数，多一个不行，少一个也不行.
        位置实参：从左到右依次赋值给形参.
'''
def foo(x,y):
    print(x,y)

foo(1,2)

\二: 关键字参数
'''
无需按照位置为形参传值
在函数调用阶段，按照key=value的形式定义实参。可以不依赖位置而指名道姓地给形参传值。
    需要注意的问题（可以与位置实参混用，但是）：
        1. 位置实参必须在关键字实参的前面
        2. 不能为一个形参重传值
'''
def foo(x,y):
    print(x,y)

foo(1,y=20) # 输出正常

def foo(x,y):
    print(x,y)

foo(1,2,y=20) # 会报错，因为形参中只接受两个值却传了三个。


\三: 默认参数
'''
可以传值也可以不传值，经常需要变得参数定义成位置形参，变化较小的参数定义成默认参数（形参）
在定义函数阶段，已经为形参赋值了，在定义阶段已经赋值，意味着在调用阶段可以不传值。
    注意的问题：
        1 默认参数的值，在定义时就赋值了，调用时可传可不传。只在定义时赋值一次，只有调用时可以修改。
        2 位置形参应该在默认参数的前面
        3 默认参数的值应该是不可变类型，要写可变类型也可以。但是是个不好的编程习惯。
'''
def foo(x,y=10):
    print(x,y)

foo(y=11,x=1) # 可以变换位置

def foo(x,y=10):
    print(x,y)

foo(x=1,11)   # python语法不支持给关键字形参直接传值，必须指名道姓。如：y=11

# 应用场景举例
def register(name,age,sex='male'):
    print(name,age,sex)

register('egon',18)
register('wsb',18)
register('alex',38,'xxxxxx') # sex的值可传可不传，已经有默认值了。

# 默认参数的值，只在定义时赋值一次，再改也和它没关系了。
x='male'
def register(name,age,sex=x):
    print(name,age,sex)

x='female'
register('alex',18)  # x还是male

# 位置形参应该在默认参数的前面,下面语法会报错。
def register(name,sex='male',age):
    print(name,age,sex)

\四：可变长参数
'''
实参可变长度指的是：实参值的个数是不固定的，而实参的定义形式无非两种：
    1、位置实参
    2、关键字实参,针对这两种形式的实参个数不固定。

相应的，形参也要有两种解决方案，即：
    *：针对按照位置实参定义多出来的部分就被*处理了。
    **：针对按照关键字定义的实参多出来的部分就被**处理了。
    *和**即是*args，**kwargs，args和kwargs实际上可以是任意字符，只是约定俗成这样使用的。
'''

# 针对按照"位置"参数定义的溢出的那部分位置实参，形参：*args（叫什么无所谓，通常叫args）
def func(x,y,z,*args):  # args=(4,5,6)
    print(x,y,z)
    print(args)

func(1,2,3)       # 没有多出来的，args就没有值就是一个空元组。
func(1,2,3,4,5,6) # 多出来的456会被*处理成(4,5,6)元组后赋值给args。
'''
1 2 3
()
1 2 3
(4, 5, 6)   # 多出来的4、5、6被*定义成元组的形式赋值给args=(4,5,6)
'''

func(1,2,3,*[4,5,6]) # 实参中只要出现*先打散成func(1,2,3,4,5,6)的形式
func(*[1,2,3,4,5,6]) # func(1,2,3,4,5,6)
func([1,2,3,4,5,6])  # func(1,2,3,4,5,6)  # 不加*时这样就传了一个值，只有x有值，y和z没值会报错。


def func(x,y,z):
    print(x,y,z)

l=[1,2,3]
func(*l) # 正好，不多不少。所以也不需要*args

# 针对按照"关键字"参数定义的溢出的那部分位置实参，形参：**kwargs
def foo(x,y,**kwargs): # kwargs={'a':1,'z':3,'b':2} 溢出部分**会接收过来的值放在字典里赋值给kwargs。
    print(x,y)
    print(kwargs)

foo(y=2,x=1,z=3,a=1,b=2)
'''
1 2
{'z': 3, 'a': 1, 'b': 2}
'''
foo(1,2,3,z=3,a=1,b=2) # 3没有地方放，会报错。可以在函数定义阶段再加个*agrs来接收益处的位置实参。

foo(y=1,x=2,**{'a':1,'b':2,'c':3}) # foo(x=2,y=1,c=3,b=2,a=1)
'''
2 1
{'a': 1, 'b': 2, 'c': 3}
'''
foo(**{'x':1,'a':1,'b':2,'c':3})   # foo(x=1,c=3,b=2,a=1),y没值会报错


def foo(x,y,z):
    print(x,y,z)

dic={'x':1,'y':3,'z':1}
foo(**dic)  # foo(x=1,y=3,z=1) ，字典里的key要符合函数接收的值。
'''
1 3 1
'''


# 装饰器时会用到这样的方法 *args  **kwargs 
def home(name,age,sex):
    print('from home====>',name,age,sex)

def wrapper(*args,**kwargs): # 被*接收赋值给 args=(1,2,3,4,5,6,7),被**接收赋值给kwargs={'c':2,'b':2,'a':1}
    home(*args,**kwargs)     # 本质还是在调home函数
    # home(*(1,2,3,4,5,6,7),**{'c':2,'b':2,'a':1}) # 上一行home(*args,**kwargs)翻译成
    # home(1,2,3,4,5,6,7,a=1,b=2,c=3)              # 从上一行可以看出在实参中出现了*和**，打散。

wrapper(1,2,3,4,5,6,7,a=1,b=2,c=3)  
# 实际上就是把wrapper接收的所有参数原封不动的给home函数使用。执行会报错，传参时要遵循home函数的接参。

# 修改传参
def home(name,age,sex):
    print('from home====>',name,age,sex)

def wrapper(*args,**kwargs): # args=(egon),kwargs={sex:'male',age:19}，*args,**kwargs表示接收任意长度、任意形式的实参。
    home(*args,**kwargs)

wrapper('egon',sex='male',age=19)


\五: 命名关键字参数(了解)
'''
# 形参中，在*后定义的参数称之为命名关键字参数，
# 它的特性是；传值时，必须被传值（有默认值的除外），且必须按照关键字实参的形式传递
'''
def foo(x,y,*,a,b):  # *也可以不加args使用
    print(x,y,a,b)

foo(1,2,b=3,a=4)
'''
1 2 4 3
'''

def foo(x,y,*args,a,b): 
    print(args)
    print(x,y,a,b)

foo(1,2,3,4,5,b=3,a=4)
'''
(3, 4, 5)
1 2 4 3
'''

def foo(x,y=20,*args,a=1,b):  # 有人会误认为位置形参跑到了关键字形参前面了，肯定得报错。但是这前面有*args，就意味这后面的都是命名关键字参数，只是有个默认值而已。
    print(args)
    print(x,y,a,b)

foo(1,2,3,4,5,b=3,a=4)

\传参顺序
# 位置参数,默认参数,*args,命名关键字参数,**kwargs


\练习题
1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表

#题目一
def modify_file(filename,old,new):
    import os
    with open(filename,'r',encoding='utf-8') as read_f,\
        open('.bak.swap','w',encoding='utf-8') as write_f:
        for line in read_f:
            if old in line:
                line=line.replace(old,new)
            write_f.write(line)
    os.remove(filename)
    os.rename('.bak.swap',filename)

modify_file('/Users/jieli/PycharmProjects/爬虫/a.txt','alex','SB')

#题目二
def check_str(msg):
    res={
        'num':0,
        'string':0,
        'space':0,
        'other':0,
    }
    for s in msg:
        if s.isdigit():
            res['num']+=1
        elif s.isalpha():
            res['string']+=1
        elif s.isspace():
            res['space']+=1
        else:
            res['other']+=1
    return res

res=check_str('hello name:aSB passowrd:alex3714')
print(res)


#题目三：略

#题目四
def func1(seq):
    if len(seq) > 2:
        seq=seq[0:2]
    return seq
print(func1([1,2,3,4]))


#题目五
def func2(seq):
    return seq[::2]
print(func2([1,2,3,4,5,6,7]))


#题目六
def func3(dic):
    d={}
    for k,v in dic.items():
        if len(v) > 2:
            d[k]=v[0:2]
    return d
print(func3({'k1':'abcdef','k2':[1,2,3,4],'k3':('a','b','c')}))

