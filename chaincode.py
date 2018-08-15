# -*- coding: utf-8 -*-

import pandas as pd
import hashlib
import numpy as np
import shutil

class chain_func:
    
    def list_all_item(self, num, row):
        #print(str(num) + ". 单号：" + row[7], end = '')
        print('%2s. 单号: %-18s'%(str(num),row[7]), end = '|')
        #print("账单主人：" + row[0] + "", end = '')
        print('账单主人：%-8s'%(row[0]), end = '|')
        if row[2] != '-1':
            #print("来自订单：" + str(row[2]) + "", end = '')
            print('来自订单：%-18s'%(str(row[2])), end = '|')
        else:
            print('来自订单：%-18s'%('self'), end = '|')
        #print("转予：" + row[3] + "", end = '')
        print('转予：%-8s'%(row[3]), end = '|')
        if row[1] == 'currency':
            #print("金额：" + str(row[4]), end = '')
            print('金额：%-10s'%(str(row[4])), end = '')
        else:
            #print("花费：" + str(row[4]), end = '')
            print('花费：%-10s'%(row[4]), end = '|')
             #print("购买物品：" + row[1], end = '')
            print('购买物品：%-10s'%(row[1]), end = '')
        print()
        return

    def read_ledger(self, user):
        self.check_ledger_equality(user)
        print('\n所有账单：')
        filename = user + "_ledger.csv"
        data = np.array(pd.read_csv(filename))
        num = 1
        for row in data:
            self.list_all_item(num, row)
            num = num + 1
        print()
        return
    
    def write_trans(self, filename, trans):
        with open(filename, 'a') as f:
            f.write(trans.user + ',')
            f.write(trans.item + ',')
            f.write(trans.get_from + ',')
            f.write(trans.send_to + ',')
            f.write(str(trans.value) + ',')
            f.write(trans.hash_code + ',')
            f.write(str(trans.pre_hash) + ',')
            f.write(trans.txn)
            f.write('\n')
        return
    
    def write_ledger(self, trans):
        self.check_ledger_equality(trans.user)
        fileName = trans.user + '_ledger.csv'
        data = pd.read_csv(fileName)
        if len(data) == 0:
            trans.pre_hash = '-1'
        else:
            trans.pre_hash = np.array(data)[-1,5]
        abstract = trans.user + trans.item + trans.get_from + trans.send_to + str(trans.value) + str(trans.pre_hash) + str(trans.txn) 
        m = hashlib.md5()  # build md5 object
        m.update(abstract.encode()) # build encypted password
        trans.hash_code = m.hexdigest()
        self.write_trans(fileName, trans)
        print('账本写入完成\n')
        return

    def get_txn_amount(self, user, txn):
        filename = user + '_ledger.csv'
        data = np.array(pd.read_csv(filename))
        for t in data:
            if t[7] == txn:
                return t[4]
        return

    def sync_ledger(self,trans):
        fileName1 = '_ledger.csv'
        fileName2 = '_ledger.csv'
        if trans.user == 'abc':
            fileName1 = 'company'+fileName1
            fileName2 = 'person'+fileName2
        elif trans.user == 'company':
            fileName1 = 'abc'+fileName1
            fileName2 = 'person'+fileName2
        elif trans.user == 'person':
            fileName1 = 'abc'+fileName1
            fileName2 = 'company'+fileName2
        else:
            return
        self.write_trans(fileName1, trans)
        self.write_trans(fileName2, trans)
        return
    
    def get_unused_trans(self, user):
        data = []
        useful = []
        ledgerTo = []
        ledgerFrom = []
        ledger_to_table = []
        full_table = []
        filename = user + '_ledger.csv'
        data = pd.read_csv(filename)
        data_len = len(data)
        
        for index in range(data_len):
            if(np.array(data)[index,3]==user):
                ledgerTo.append(np.array(data)[index,7])
                ledger_to_table.append(np.array(data)[index])
        
        for index in range(data_len):
            if(np.array(data)[index,0]==user):
                ledgerFrom.append(np.array(data)[index,2])
        
        for i in range(len(ledgerTo)):
            if ledgerTo[i] not in ledgerFrom:
                useful.append(ledgerTo[i])
                full_table.append(ledger_to_table[i])

        num = 1
        for row in full_table:
            self.list_all_item(num, row)
            num = num + 1

        return full_table

    def is_legal(self, user):
        fileName = user + "_ledger.csv"
        data = pd.read_csv(fileName)
        count = len(data) -1
        
        while count >= 0:
            m = hashlib.md5()  #创建md5对象
            abstract = ""
            trans = np.array(data)[count]
            for x in range(len(trans)):
                if(x == 5):
                    continue
                abstract += str(trans[x])
            m.update(abstract.encode())
            hash_code = m.hexdigest()
            if(hash_code != trans[5]):
                return False
            if(count > 0):
                pre_trans_hash = np.array(data)[count-1,5]
                if(pre_trans_hash != trans[6]):
                    return False
            count = count - 1
        return True

    def check_ledger_equality(self, user):
        try:
            abc_len     = len(open('abc_ledger.csv', 'r').readlines())
            company_len = len(open('company_ledger.csv', 'r').readlines())
            person_len  = len(open('person_ledger.csv', 'r').readlines())
        except:
            print('不小心删库了！我跑路了，告辞！')

        if not self.is_legal('abc'):
            abc_len     = 0
        if not self.is_legal('company'):
            company_len = 0
        if not self.is_legal('person'):
            person_len  = 0

        if abc_len > company_len and abc_len > person_len:
            std_file = 'abc_ledger.csv'
        elif company_len > abc_len and company_len > person_len:
            std_file = 'company_ledger.csv'
        elif person_len == 0:
            print('不小心删库了！我跑路了，告辞！')
        else:
            std_file = 'person_ledger.csv'
        
        if abc_len == company_len and company_len == person_len:
            print('三方数据验证完毕！')
        else:
            for i in ['abc_ledger.csv', 'company_ledger.csv', 'person_ledger.csv']:
                try:
                    shutil.copyfile(std_file, i)
                except:
                    print('数据有误，已更新！')