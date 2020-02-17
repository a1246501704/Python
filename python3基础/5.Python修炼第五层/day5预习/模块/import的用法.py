#导入模块干了哪些事：
#1 执行源文件
#2 以一个源文件的全局名称空间
#3 在当前位置拿到一个模块名，指向2创建的名称空间


# import spam
# money=1000000000000
# def read1():
#     print('from test')
# # print(spam.money)
# # print(spam.read1)
# # spam.read1()
#
# # spam.read2()
# spam.change()
# print(money)
# spam.read1()


# as 两个应用场景
# 1 给一些长的模块名 起个简单的别名
# import spam as s1
# print(s1.money)

# 根据模块的功能不同 起相同名字 最后调用结果也不同
# sql_type=input('sql_type:')
# if sql_type == 'mysql':
#     import mysql as sql
#
# elif sql_type == 'oracle':
#     import oracle as sql
#
# sql.sqlparse()


import sys
print(sys)
import spam
print(spam)



