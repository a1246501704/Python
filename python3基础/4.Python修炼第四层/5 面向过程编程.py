'''
1、首先强调：面向过程编程绝对不是用函数编程这么简单，面向过程是一种编程思路、思想，而编程思路是不依赖于具体的语言或语法的。
言外之意是即使我们不依赖于函数，也可以基于面向过程的思想编写程序

2、定义
面向过程的编程思想：核心是过程二字，过程即解决问题的步骤，即先干什么再干什么.
基于该思想去编写程序就好比在设计一条流水线，是一种机械式的编程思想.

3、优点：复杂的问题流程化，进而简单化
4、缺点：可扩展性差,修改流水线的任意一个阶段，都会牵连而动全身
5、应用场景：扩展性要求不高的场景，典型案例如linux内核、shell脚本、git、httpd
'''

import os
g=os.walk(r'C:\Users\zhanghongyang\Documents\软通动力\Github\python3基础\4.Python修炼第四层\a') # r代表原生字符串，意思是字符串中没有转译的意思,\就没有意义了。os.walk的结果就是一个生成器。
# print(next(g)) # 得到一个元组，内容是a目录下包含的目录和文件
# print(next(g)) # 得到一个元组，内容是a\b\目录下包含的目录和文件
# print(next(g)) # 得到一个元组，内容是a\b\d\目录下包含的目录和文件
# print(next(g)) # 得到一个元组，内容是a\c\目录下包含的目录和文件
# os.walk可以把a目录下的所有目录递归的找出来，要把每个文件的绝对路径都拼接出来，如下。
for dirname,_,files in g: # g元组中包含三个值，父目录名、子目录名、文件名。第二个子目录名没有，因为每next一次后在父目录中就包含了。
    for file in files:
        abs_file_path=r'%s\%s' %(dirname,file) # 拼接出a目录下所有文件的绝对路径（windows），linux系统不需要加反斜杠。
        print(abs_file_path) 


\练习题: grep -rl 'root' /etc  # 递归的形式在etc目录下所有目录中的所有文件中包含root的文件名打印出来

# 设计：
def search(): # 拿到文件绝对路径功能
    pass

def opener(): # 打开文件功能
    pass

def cat():    # 读取上个阶段打开的文件的文件内容功能
    pass

def grep():   # 将上个阶段读到的内容进行过滤
    pass

def printer(): # 打印
    pass

# 开始实现: 整个过程是函数的高级用法
import os

# 初始化函数装饰器，就是为了每个函数执行后得到的生成器执行一下next(g)操作.
def init(func):
    def inner(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)  # 主要功能
        return g # 返回的是初始化的g
    return inner

# 得到文件绝对路径
# 注意：target.send(...)在拿到target的返回值后才算执行结束
def search(filepath,target): # 找到一个文件路径就往下个阶段传一次,此处的target是opener函数
    g = os.walk(filepath)    # walk功能可接受一个文件路径，然后生成一个生成器。
    for dirname,_,files in g:
        for file in files:
            abs_file_path = r'%s\%s' % (dirname, file)
            target.send(abs_file_path) # 将文件绝对路径传给下个阶段

@init
def opener(target): # 此处的target是cat函数
    while True:
        abs_file_path=yield # 接收search函数send过来的值
        with open(abs_file_path,'rb') as f:
            target.send((f,abs_file_path)) # 把打开的文件和文件路径一起传给下个阶段，send传多个值要用列表或元组的形式。

@init
def cat(target): # 此处的target是grep函数
    while True:
        f,abs_file_path=yield # 收两个值
        for line in f:
            res=target.send((line,abs_file_path)) # 发了一个元组两个值，将内行内容和文件的绝对路径传给下个阶段，res的结果是grep的yield返回的值
            if res:
                break # 实现当匹配到文件中第一个要匹配的值时就不在读其他行了，结束循环。

@init
def grep(pattern,target): # 此处的target是printer函数
    tag=False
    pattern = pattern.encode('utf-8')
    while True:
        line,abs_file_path=yield tag # 收一个元组两个值，并将tag的值返回给cat函数作为res的调用结果。
        tag=False  # 返回完在修改成False，否则以后都是True了。
        if pattern in line:
            target.send(abs_file_path) # 将过滤出的包含“你好”的文件路径传给下个阶段
            tag=True

@init
def printer():
    while True:
        abs_file_path=yield  # 接收
        print(abs_file_path) # 打印文件绝对路径

# 使用时传参数，一个套一个使用。
search(r'C:\Users\Administrator\PycharmProjects\19期\day4\a',opener(cat(grep('你好',printer()))))



# 6、举例
流水线1：
用户输入用户名、密码--->用户验证--->欢迎界面

流水线2：
用户输入sql--->sql解析--->执行功能

ps：函数的参数传入，是函数吃进去的食物，而函数return的返回值，是函数拉出来的结果。面向过程的思路就是，把程序的执行当
做一串首尾相连的功能（类似与电影《人体蜈蚣》），该功能可以是函数的形式，然后一个函数吃，拉出的东西给另外一个函数吃，另外一个函数吃了再继续拉给下一个函数吃。。。

#=============复杂的问题变得简单
#注册功能:
#阶段1: 接收用户输入账号与密码,完成合法性校验
def talk():
    while True:
        username=input('请输入你的用户名: ').strip()
        if username.isalpha():
            break
        else:
            print('用户必须为字母')

    while True:
        password1=input('请输入你的密码: ').strip()
        password2=input('请再次输入你的密码: ').strip()
        if password1 == password2:
            break
        else:
            print('两次输入的密码不一致')
            
    return username,password1

#阶段2: 将账号密码拼成固定的格式
def register_interface(username,password):
    format_str='%s:%s\n' %(username,password)
    return format_str

#阶段3: 将拼好的格式写入文件
def handle_file(format_str,filepath):
    with open(r'%s' %filepath,'at',encoding='utf-8') as f:
        f.write(format_str)


def register():
    user,pwd=talk()
    format_str=register_interface(user,pwd)
    handle_file(format_str,'user.txt')

register()


#=============牵一发而动全身,扩展功能麻烦
#阶段1: 接收用户输入账号与密码,完成合法性校验
def talk():
    while True:
        username=input('请输入你的用户名: ').strip()
        if username.isalpha():
            break
        else:
            print('用户必须为字母')

    while True:
        password1=input('请输入你的密码: ').strip()
        password2=input('请再次输入你的密码: ').strip()
        if password1 == password2:
            break
        else:
            print('两次输入的密码不一致')


    role_dic={
        '1':'user',
        '2':'admin'
    }
    while True:
        for k in role_dic:
            print(k,role_dic[k])

        choice=input('请输入您的身份>>: ').strip()
        if choice not in role_dic:
            print('输入的身份不存在')
            continue
        role=role_dic[choice]

    return username,password1,role

#阶段2: 将账号密码拼成固定的格式
def register_interface(username,password,role):
    format_str='%s:%s:%s\n' %(username,password,role)
    return format_str

#阶段3: 将拼好的格式写入文件
def handle_file(format_str,filepath):
    with open(r'%s' %filepath,'at',encoding='utf-8') as f:
        f.write(format_str)


def register():
    user,pwd,role=talk()
    format_str=register_interface(user,pwd,role)
    handle_file(format_str,'user.txt')


register()
#ps:talk内对用户名\密码\角色的合法性校验也可以摘出来做成单独的功能,但本例就写到一个函数内了,力求用更少的逻辑来为大家说明过程式编程的思路