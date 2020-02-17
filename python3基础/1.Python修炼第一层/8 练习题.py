#while循环练习题
#1. 使用while循环输出1 2 3 4 5 6     8 9 10
#2. 求1-100的所有数的和
#3. 输出 1-100 内的所有奇数
#4. 输出 1-100 内的所有偶数
#5. 求1-2+3-4+5 ... 99的所有数的和
#6. 用户登陆（三次机会重试）
#7：猜年龄游戏
# 要求：
#     允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
#8：猜年龄游戏升级版
# 要求：
#     允许用户最多尝试3次
#     每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
#     如何猜对了，就直接退出


# 题一
# count=1
# while count <= 10:
#     if count != 7:
#         print(count)
#     count+=1

# count=1
# while count <= 10:
#     if count == 7:
#         count+=1
#         continue
#     print(count)
#     count+=1


# 题二
# res=0
# count=1
# while count <= 100:
#     res+=count
#     count += 1
# print(res)


# 题三
# count=1
# while count <= 100:
#     if count%2 == 1:
#         print(count)
#     count+=1

# 题四
# count=1
# while count <= 100:
#     if count%2 == 0:
#         print(count)
#     count+=1

# 题五
# res=0
# count=1
# while count <= 5:
#     if count%2 == 0:
#         res-=count
#     else:
#         res+=count
#     count+=1
# print(res)

# 题六
# count=0
# while count < 3:
#     name = input('请输入用户名 >>:')
#     password = input('请输入密码 >>:')
#     if name == 'egon' and password == '123':
#         print('login success')
#         break
#     else:
#         print('用户名或者密码错误')
#         count+=1

# 题七
# age=73
# count=0
# while count < 3:
#     u_age = int(input('猜猜猜>> '))
#     if u_age > age:
#         print('猜大了')
#     elif u_age < age:
#         print('猜小了')
#     else:
#         print('懵对了')
#         break
#     count += 1

# age_of_oldboy=73
# count=0
# while count < 3:
#     guess=int(input('>>: '))
#     if guess == age_of_oldboy:
#         print('you got it')
#         break
#     count+=1

# 题八
# age_of_olfboy=73
# count=0
# while True:
#     if count == 3:
#         choice=input('继续（Y/N?）>>: ')
#         if choice == 'Y' or choice == 'y':
#             count=0
#         else:
#             break
#     guess=int(input('>>: '))
#     if guess == age_of_olfboy:
#         print('you got it')
#         break
#     count+=1


# 用户登录验证
#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# name=input('请输入用户名： ')
# password=input('请输入密码：')
# if name == 'egon' and password == '123':
#     print('egon login success')
# else:
#     print('用户名或密码错误')

# 根据用户输入内容输出其权限
#！ /usr/bin/env python
# -*- coding: utf-8 -*-
#根据用户输入内容打印其权限
'''
egon --> 超级管理员
tom --> 普通管理员
jack,rain --> 业务主管
其他 --> 普通用户
'''
# name=input('请输入用户名字：')
# if name == 'egon':
#     print('超级管理员')
# elif name == 'tom':
#     print('普通管理员')
# elif name == 'jack' or name == 'rain':
#     print('业务主管')
# else:
#     print('普通用户')

#多条件用户
# 如果:今天是Monday,那么:上班
# 如果:今天是Tuesday,那么:上班
# 如果:今天是Wednesday,那么:上班
# 如果:今天是Thursday,那么:上班
# 如果:今天是Friday,那么:上班
# 如果:今天是Saturday,那么:出去浪
# 如果:今天是Sunday,那么:出去浪
#
#方式一
# today=input('>>: ')
# if today == 'Monday':
#     print('上班')
# elif today == 'Tuesday':
#     print('上班')
# elif today == 'Wednesday':
#     print('上班')
# elif today == 'Thursday':
#     print('上班')
# elif today == 'Friday':
#     print('上班')
# elif today == 'Saturday':
#     print('出去浪')
# elif today == 'Sunday':
#     print('出去浪')
# else:
#     print('''必须输入其中一种:
#     Monday
#     Tuesday
#     Wednesday
#     Thursday
#     Friday
#     Saturday
#     Sunday
#     ''')

#方式二：
# today=input('>>: ')
# if today == 'Saturday' or today == 'Sunday':
#     print('出去浪')
#
# elif today == 'Monday' or today == 'Tuesday' or today == 'Wednesday' \
#     or today == 'Thursday' or today == 'Friday':
#     print('上班')
#
# else:
#     print('''必须输入其中一种:
#     Monday
#     Tuesday
#     Wednesday
#     Thursday
#     Friday
#     Saturday
#     Sunday
#     ''')

#方式三：
# today=input('>>: ')
# if today in ['Saturday','Sunday']:
#     print('出去浪')
# elif today in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
#     print('上班')
# else:
#     print('''必须输入其中一种:
#     Monday
#     Tuesday
#     Wednesday
#     Thursday
#     Friday
#     Saturday
#     Sunday
#     ''')

# 1 练习题
#
#     简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
#     执行 Python 脚本的两种方式是什么
#     Pyhton 单行注释和多行注释分别用什么?
#     布尔值分别有什么?
#     声明变量注意事项有那些?
#     如何查看变量在内存中的地址?
#     写代码
#         实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
#         实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
#         实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
#
#     写代码
#     a. 使用while循环实现输出2-3+4-5+6...+100 的和
#     b. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12 使用 while 循环实现输出 1-100 内的所有奇数
#
#     e. 使用 while 循环实现输出 1-100 内的所有偶数
#
#     现有如下两个变量,请简述 n1 和 n2 是什么关系?
#
#       n1 = 123456
#       n2 = n1
# n1=123456
# n2=n1
# print(id(n1),type(n1),n1)
# print(id(n2),type(n2),n2)
# n1=123
# print(id(n1),type(n1),n1)
# print(id(n2),type(n2),n2)

# 2 作业：编写登陆接口
#
# 基础需求：
#
#     让用户输入用户名密码
#     认证成功后显示欢迎信息
#     输错三次后退出程序

# dic={
#     'egon1':{'password':'123','count':0},
#     'egon2':{'password':'123','count':0},
#     'egon3':{'password':'123','count':0},
# }
# while True:
#     name=input('username>>: ')
#     if not name in dic:
#         print('用户不存在')
#         continue
#     if dic[name]['count'] > 2:
#         print('尝试次数过多，锁定')
#         continue
#     password=input('password>>: ')
#     if password == dic[name]['password']:
#         print('登录成功')
#         break
#     else:
#         print('用户名或密码错误')
#     dic[name]['count']+=1

# 升级需求：
#
#     可以支持多个用户登录 (提示，通过列表存多个账户信息)
#     用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

#db.txt内容：egon1|egon2|
# dic={
#     'egon1':{'password':'123','count':0},
#     'egon2':{'password':'123','count':0},
#     'egon3':{'password':'123','count':0},
# }
# count=0
# while True:
#     name=input('u>>: ')
#     if name not in dic:
#         print('用户不存在')
#         continue
#     with open('db.txt','r') as f:
#         lock_users=f.read().split('|')
#         if name  in lock_users:
#             print('用户%s已经被锁定' %name)
#             break
#     if dic[name]['count'] > 2:
#         print('尝试次数过多,锁定')
#         with open('db.txt','a') as f:
#             f.write('%s|' %name)
#         break
#     password=input('p>>: ')
#     if password == dic[name]:
#         print('登录成功')
#         break
#     else:
#         print('用户名或密码错误')
#         dic[name]['count']+=1


#多用户
# div={
# 'list1':{'password':'123456'},
# 'list2':{'password':'123456'},
# 'list3':{'password':'123456'},
# }
# f = open('black_user','r')
# lock_file = f.readlines()
# f.close()
# count=0
# count1=0
# while True:
#     name_input=input("please input name:")
#     if count == 3:
#         print("用户名输入次数到达限制")
#         break
#     if  not name_input in div:
#             print("用户名错误")
#             count +=1
#     if  name_input in lock_file:
#         print("户名已锁定，暂停使用！")
#         exit()
#
#     if name_input in div:
#         count -=2
#         password_input=str(input("please input password:"))
#         if password_input == div[name_input]['password']:
#             print ("密码成功")
#             break
#         else:
#             print("密码错误")
#             count1 +=1
#         if count1 == 2:
#             print("您输入的密码错误次数已达3次，将锁定您的账户!")
#             f = open('black_user', 'w')
#             f.write('%s'%name_input)
#             f.close()
#             break

