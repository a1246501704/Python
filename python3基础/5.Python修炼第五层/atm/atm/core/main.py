#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
main program handle module , handle all the user interaction stuff

'''

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required

import time
# import os
# import sys
# base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(base_dir)
# sys.path.append(base_dir)
# from shopping_mall.shopping import shopping


#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

def account_info(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    data_info = u'''
    \033[34;1m 账号ID：%s
    余额：  %s
    信用度：%s
    账号注册时间：%s
    账号过期时间：%s
    工资天数：%s
    \033[0m'''%(acc_data['account_id'],
                account_data['balance'],
                account_data['credit'],
                account_data['enroll_date'],
                account_data['expire_date'],
                account_data['pay_day'],)
    print(data_info)


@login_required
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #再从硬盘加载一次数据， 为了确保数据是最新的
    #for k,v in account_data.items():
    #    print(k,v )
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            #print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

        if repay_amount == 'b':
            back_flag = True
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True

def transfer(acc_data):
    '''

    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        t_acc = input("\033[33;1mInput transfer account<输入转账户'1234 or 4321'>:\033[0m").strip()
        transfer_amount = input("\033[33;1mInput transfer amount<输入转数量>:\033[0m").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            # print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount, t_acc)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)

        if transfer_amount == 'b':
            back_flag = True

def pay_check(acc_data):
    with open(r'D:\python编码\py_s19\day5\atm\atm\log\transactions.log',mode='r',encoding='utf-8') as f:
        print(f.read())
def logout(acc_data):
    exit()


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


def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- hehe Bank ---------
    \033[32;1m
    1.  账户信息(实现)
    2.  还款(实现)
    3.  取款(实现)
    4.  转账(实现)
    5.  账单(实现)
    6.  商城(实现)
    7.  退出(实现)
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': shopping,
        '7': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            #print('accdata',acc_data)
            #acc_data['is_authenticated'] =False
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)