# -*- coding: utf-8 -*-

from chaincode import chain_func as cf

class user_interact:

    def abc_seed_fund(self, amount):
        return amount, '-1'

    def choose_trans(self, user):
        chain_func = cf()
        trans_table = chain_func.get_unused_trans(user)
        if len(trans_table) == 0:
            return -1, -1
        else:
            while 1:
                print('请选择txn号：')
                print('若想退出，请输入“qw:”')
                txn_option = input()
                if txn_option == 'qw:':
                    return -2, -2
                elif int(txn_option) > len(trans_table) or int(txn_option) <= 0:
                    print('请选择正确的txn号！')
                    continue
                else:
                    amount = chain_func.get_txn_amount(user, trans_table[int(txn_option) - 1][7])
                    break
            return amount, trans_table[int(txn_option) - 1][7]
    
    def abc_create_trans(self, trans):
        chain_func = cf()
        chain_func.write_ledger(trans)
        chain_func.sync_ledger(trans)
        return
    
    def abc_read_trans(self, user):
        chain_func = cf()
        chain_func.read_ledger(user)
        return
    
    def company_create_trans(self,trans):
        chain_func = cf()
        chain_func.write_ledger(trans)
        chain_func.sync_ledger(trans)
        return
    
    def company_read_trans(self, user):
        chain_func = cf()
        chain_func.read_ledger(user)
        return
    
    def person_create_trans(self,trans):
        chain_func = cf()
        chain_func.write_ledger(trans)
        chain_func.sync_ledger(trans)
        return
    
    def person_read_trans(self, user):
        chain_func = cf()
        chain_func.read_ledger(user)
        return