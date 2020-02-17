# 既然我们编程的目的是为了控制计算机能够像人脑一样工作，那么人脑能做什么，就需要程序中有相应的机制去模拟。
# 人脑无非是数学运算和逻辑运算，对于数学运算在上一节我们已经说过了。对于逻辑运算，即人根据外部条件的变化而做出不同的反映。

\比如
# 1、if——>如果：女人的年龄>30岁，那么：叫阿姨
age=input('>>: ')  # 可以缩减为一行 age=int(input('>>: '))
age=int(age)
if age > 30:
    print('叫阿姨')

# 2、if...else——>如果：女人的年龄>30岁，那么：叫阿姨，否则：叫妹妹
age=input('>>: ')
age=int(age)
if age > 30:
    print('叫阿姨')
else:
    print('叫妹妹')

# 3、如果：女人的年龄>=18并且<22岁并且身高>170并且体重<100并且是漂亮的，那么：表白，否则：叫阿姨
sex = input('sex>>: ')
age = int(input('age>>: '))
is_pretty = bool(input('is_pretty>>: ')) # 转换成波尔值
if sex == 'female' and age > 18 and age < 30 and is_pretty == True:
    print('去表白')
else:
    print('叫阿姨')

# 4、if嵌套——>在表白的基础上继续：如果表白成功，那么：在一起，否则：打印。。。
sex = input('sex>>: ')
age = int(input('age>>: '))
is_pretty = bool(input('is_pretty>>: '))
success = True
if sex == 'female' and age > 18 and age < 30 and is_pretty == True:
    if success:
        print('在一起')
    else:
        print('什么尼玛的爱情')
else:
    print('叫阿姨')

# 5、if多分支——>如果：成绩>=90，那么：优秀
            #  如果成绩>=80且<90,那么：良好
            #  如果成绩>=70且<80,那么：普通
            #  其他情况：很差
'''
if 条件1:
　　缩进的代码块
elif 条件2:
　　缩进的代码块
elif 条件3:
　　缩进的代码块
......
else:　　
　　缩进的代码块
'''
score=int(input("your score>>: "))

if score >90:
    print('优秀')
elif score >=80:  # 能走到这个肯定是不满足第一个条件，所以不用< 90。
    print('良好')
elif score >=70:
    print('及格')
else:
    print('太差了')


\练习
# 练习一: 用户验证登陆
name=input('请输入用户名字：')
password=input('请输入密码：')
if name == 'egon' and password == '123':
    print('egon login success')
else:
    print('用户名或密码错误')

# 练习二: 根据用书输入的内容输出其权限
'''
egon --> 超级管理员
tom  --> 普通管理员
jack,rain --> 业务主管
其他 --> 普通用户
'''
name=input('请输入用户名字：')
if name == 'egon':
    print('超级管理员')
elif name == 'tom':
    print('普通管理员')
elif name == 'jack' or name == 'rain':
    print('业务主管')
else:
    print('普通用户')

# 练习三: 今天上不上班？
    # 如果:今天是Monday,那么:上班
    # 如果:今天是Tuesday,那么:上班
    # 如果:今天是Wednesday,那么:上班
    # 如果:今天是Thursday,那么:上班
    # 如果:今天是Friday,那么:上班
    # 如果:今天是Saturday,那么:出去浪
    # 如果:今天是Sunday,那么:出去浪

#方式一:
today=input('>>: ')
if today == 'Monday':
    print('上班')
elif today == 'Tuesday':
    print('上班')
elif today == 'Wednesday':
    print('上班')
elif today == 'Thursday':
    print('上班')
elif today == 'Friday':
    print('上班')
elif today == 'Saturday':
    print('出去浪')
elif today == 'Sunday':
    print('出去浪')
else:
    print('''必须输入其中一种:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    ''')
# 方式二:
today=input('>>: ')
if today == 'Saturday' or today == 'Sunday':
    print('出去浪')
elif today == 'Monday' or today == 'Tuesday' or today == 'Wednesday' \
    or today == 'Thursday' or today == 'Friday':
    print('上班')
else:
    print('''必须输入其中一种:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    ''')
# 方式三:
today=input('>>: ')
if today in ['Saturday','Sunday']:
    print('出去浪')
elif today in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
    print('上班')
else:
    print('''必须输入其中一种:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    ''')






