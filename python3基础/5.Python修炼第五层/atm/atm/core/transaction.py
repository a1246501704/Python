#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conf import settings
from core import accounts
from core import logger
import json,os
#transaction logger



def make_transaction(log_obj,account_data,tran_type,amount,*args,**kwargs): #**others
    '''
    deal all the user transactions
    :param account_data: user account data
    :param tran_type: transaction type
    :param amount: transaction amount
    :param others: mainly for logging usage
    :return:
    '''
    amount = float(amount)
    if tran_type in  settings.TRANSACTION_TYPE:

        interest =  amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            #check credit
            if  new_balance <0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))
                return

        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'transfer':
            new_balance = old_balance - amount - interest
            if  new_balance <0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))
                return
            transfer_test(amount,*args)

        account_data['balance'] = new_balance
        accounts.dump_account(account_data) #save the new balance back to file
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %
                          (account_data['id'], tran_type, amount,interest) )
        return account_data
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)

def transfer_test(amount,t_acc):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])
    # print(db_path)
    account_file = "%s/%s.json" % (db_path,t_acc)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
        # account_data = account_data.get("account_data")
            account_data['balance'] += amount
        with open(account_file, 'w') as f:
            json.dump(account_data, f)


