#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 商城购物车
product_list = [
    ['Iphone7 Plus',6500],
    ['Iphone8 ',8200],
    ['MacBook Pro',12000],
    ['Python Book',99],
    ['Coffee',33],
    ['Bike',666],
    ['pen',2]
]
shopping_cart = []
f = open('user.txt','r')
lock_file = f.readlines()
f.close()
count=0
user_list={}
while True:
    if count == 3:
        print("用户名输入次数到达3次限制")
        break
    for i in lock_file:
        i=i.strip()
        user_list[i.split('|')[0]]={'password':i.split('|')[1]}
    user_name=input("请输入您的用户名>>：")
    if user_name not in user_list:
        print("用户名错误")
        count+=1
    if user_name in lock_file:
        print("用户名已锁定，请联系管理员！")
        exit()
    if user_name in user_list:
        user_password=input("请输入您的密码>>: ")
        if user_password == user_list[user_name]['password']:
            print("欢迎登录电子商城")
            while True:
                salary = input("请输入您的工资:")  # 输入金额
                if not salary.isdigit():  # 判断输入的salary是不是数字
                    print("由于您的输入的工资不合法，请再次输入金额")  # 输入金额不合法
                    continue
                else:
                    salary = int(salary)  # 把输入的数字转成整形
                    break
            while True:
                print(">> 欢迎来到电子商城 <<")
                for index, i in enumerate(product_list):  # 循环商品列表，商品列表索引
                    print("%s.\t%s\t%s" % (index, i[0], i[1]))  # 打印商品列表，显示商品列表索引
                choice = input(">>请输入商品序号或输入 exit 退出商城>>: ").strip()
                if len(choice) == 0:  # 判断输入字符串是否为空和字符串长度
                    print('-->您没有选择商品<--')
                    continue
                if choice.isdigit():  # 判断输入的choice是不是一个数字
                    choice = int(choice)  # 把输入的字符串转成整型
                    if choice < len(product_list) and choice >= 0:  # 输入的整数必须小于商品列表的数量
                        product_item = product_list[choice]  # 获取商品
                        if salary >= product_item[1]:  # 拿现有金额跟商品对比，是否买得起
                            salary -= product_item[1]  # 扣完商品的价格
                            shopping_cart.append(product_item)  # 把选着的商品加入购物车
                            print("添加 \033[32;1m%s\033[0m 到购物车,您目前的金额是 \
            \033[31;1m%s\033[0m" % (product_item[0], salary))
                        else:
                            print("对不起，您的金额不足,还差 \033[31;1m%s\033[0m" % (product_item[1] - salary,))
                    else:
                        print("-->没有此商品<--")
                elif choice == "exit":
                    total_cost = 0
                    print("您的购物车列表:")
                    for i in shopping_cart:
                        print(i)
                        total_cost += i[1]
                    print("您的购物车总价是: \033[31;1m%s\033[0m" % (total_cost,))
                    print("您目前的余额是: \033[31;1m%s\033[0m" % (salary,))
                    break
            break
        else:
            print("密码错误")
            count += 1
        if count == 3 :
            print("您输入的密码错误次数已达3次，将锁定您的用户！")
            f = open('blacklist.txt','w')
            f.write('%s'%user_name)
            f.close()
            break

            while True:
                salary = input("请输入您的工资:")  # 输入金额
                if not salary.isdigit():  # 判断输入的salary是不是数字
                    print("由于您的输入的工资不合法，请再次输入金额")  # 输入金额不合法
                    continue
                else:
                    salary = int(salary)  # 把输入的数字转成整形
                    break
            while True:
                print(">> 欢迎来到电子商城 <<")
                for index, i in enumerate(product_list):  # 循环商品列表，商品列表索引
                    print("%s.\t%s\t%s" % (index, i[0], i[1]))  # 打印商品列表，显示商品列表索引
                choice = input(">>请输入商品序号或输入 exit 退出商城>>: ").strip()
                if len(choice) == 0:  # 判断输入字符串是否为空和字符串长度
                    print('-->您没有选择商品<--')
                    continue
                if choice.isdigit():  # 判断输入的choice是不是一个数字
                    choice = int(choice)  # 把输入的字符串转成整型
                    if choice < len(product_list) and choice >= 0:  # 输入的整数必须小于商品列表的数量
                        product_item = product_list[choice]  # 获取商品
                        if salary >= product_item[1]:  # 拿现有金额跟商品对比，是否买得起
                            salary -= product_item[1]  # 扣完商品的价格
                            shopping_cart.append(product_item)  # 把选着的商品加入购物车
                            print("添加 \033[32;1m%s\033[0m 到购物车,您目前的金额是 \
            \033[31;1m%s\033[0m" % (product_item[0], salary))
                        else:
                            print("对不起，您的金额不足,还差 \033[31;1m%s\033[0m" % (product_item[1] - salary,))
                    else:
                        print("-->没有此商品<--")
                elif choice == "exit":
                    total_cost = 0
                    print("您的购物车列表:")
                    for i in shopping_cart:
                        print(i)
                        total_cost += i[1]
                    print("您的购物车总价是: \033[31;1m%s\033[0m" % (total_cost,))
                    print("您目前的余额是: \033[31;1m%s\033[0m" % (salary,))
                    break



#
# l={}
# f = open('user.txt','r')
# for i in f:
#     i = i.strip()
#     # print(i.split('|')[0])
#     # print(i.split('|')[1])
#     l[i.split('|')[0]]={'password':i.split('|')[1]}
# print(l)














