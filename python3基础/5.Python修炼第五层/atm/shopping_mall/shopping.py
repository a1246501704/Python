#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(base_dir)
sys.path.append(base_dir)
from atm.core import accounts
from atm.core import db_handler


def shopping(acc_data):
    '''

    :param acc_data:
    :return:
    '''
    product_list = [
        ['Iphone7 Plus', 6500],
        ['Iphone8 ', 8200],
        ['MacBook Pro', 12000],
        ['Python Book', 99],
        ['Coffee', 33],
        ['Bike', 666],
        ['pen', 2]
    ]
    shopping_cart = []
    count = 0
    salary = acc_data['account_data']['balance']
    while True:
        account_data = accounts.load_current_balance(acc_data['account_id'])
        print(">> 欢迎来到电子商城 您的余额是 %s 元<<" % (salary))
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
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', total_cost)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
            break
