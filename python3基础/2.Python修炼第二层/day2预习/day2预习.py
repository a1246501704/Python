
# 多版本共存问题

# 1.数字类型
# 2.字符编码
# 3.文件处理

# age=10 #age=int(10)
# print(bin(age)) #10->2
# #1010  1*(2**3）+1*2=10
# print(oct(age)) #10->8
# print(hex(age)) #10->16
#     # 0b1010
#     # 0o12
#     # 0xa

# name='egon' #name=str('egon')
# name=str('egon')
# print(type(name))
# print(name)

#优先掌握
#索引
# name='egon' #name=str('egon')
# print(name[0])
# print(name[1000])

#移除空白
# name=input('username: ')
# # print(name)
# name=name.strip()
# print(name)
# name=input('username: ').strip()
# print(name)
# name=input('username: ')
# print(name.strip())

# name='***egon****'
# print(name.strip('*')) #去掉指定字符串
# print(name.lstrip('*')) #去掉左边指定字符串
# print(name.rstrip('*')) #去掉右边指定字符串

#切分
# user_info='root:x:0:0::/root:/bin/bash'
# print(user_info.split(':')[5]) #指定分隔符切分，取5下标

# cmd_info='get|a.txt|333333333'
# print(cmd_info.split('|')[0]) #指定分隔符切分，取0下标
# print(cmd_info.split('|',1)[0]) #指定分隔符切分，切一次，取0下标

# msg='name     egon age 18'
# print(msg.split()) #默认以空格和多个空格为分隔符

#取长度
# name='egon'
# print(name.__len__()) #计算字符串长度  下划线 内置方法
# print(len(name)) #name.__len__()

#切出子字符串
# name='hello world'
# print(name[1:5]) # 切片 可以指定步长 顾头不顾尾
# print(name[1:7])
# print(name[1:7:2]) # 切片 指定步长2 每2个取一次 顾头不顾尾

#字符其他方法(掌握)
# name='alex_SB'
# print(name.endswith('SB'))  #以什么结尾
# print(name.startswith('alex'))  #以什么开头

# name='alex say :i have one tesla,my name is alex'
# print(name.replace('alex','SB',)) #指定替换所有的字符串
# print(name.replace('alex','SB',1)) #指定替换第一个字符串

#字符串format格式化
# '{} {} {}'.format('egon',18,'male')   #格式化字符串 按{}
# print('{} {} {}'.format('egon',18,'male'))   #格式化字符串 按{}
# print('{0} {1} {0}'.format('egon',18,'male'))   #格式化字符串 在可以在{}中填入下标
# print('NAME:{name} AGE:{age} SEX:{sex}'.format(name='egon',sex='male',age=18)) #可以指定变量名格式化

# num='123'
# print(num.isdigit()) #判断字符串是不是数字

# oldboy_age=73
# while True:
#     age=input('>>: ').strip()
#     if len(age) == 0:continue
#     if age.isdigit():
#         age=int(age)
#         print(age,type(age))


#字符串其他需要了解的方法

name='egon hello'
# print(name.find('o'))  #查找字符 返回下标
# print(name.find('x'))  #查找字符 没有找到 提示 -1
# print(name.find('o',3,6))  #查找字符 指定查找范围

# print(name.index('o')) #按索引查找
# print(name.index('x')) #按索引查找 没有这个索引会报错 ValueError: substring not found

# print(name.count('o'))  #统计字符有多少个
# print(name.count('o',1,3)) #指定范围 统计字符有多少个

l=['egin','say','hello','world']


















