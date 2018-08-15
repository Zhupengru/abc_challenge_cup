# -*- coding: utf-8 -*-


from transaction import company_trans
from chaincode import chain_func as cf
from api import user_interact as ui


# 选择物品  没有可用txn  转账过程退出 输入bug

# create abc transaction
demo_company_trans = company_trans('currency', '-1', 'company', 100)

print(demo_company_trans)

#demo user interact
ui = ui()
#input balance, get_from, send_to, value
ui.company_create_trans(demo_company_trans)

chain_func = cf()
#chain_func.write_ledger()
#chain_func.read_ledger('abc')

#chain_func.get_unused_trans('company')