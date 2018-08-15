# -*- coding: utf-8 -*-

import time

class transaction:
    def __init__(self, item, get_from, send_to, value):
        self.item = item
        self.get_from = get_from
        self.send_to = send_to
        self.value = value
        self.hash_code = ''
        self.pre_hash = ''
        return

class abc_trans(transaction):
    user = 'abc'
    txn = str(int(time.time())) + user
    pass
        
class company_trans(transaction):
    user = 'company'
    txn = str(int(time.time())) + user
    pass
    
class person_trans(transaction):
    user = 'person'
    txn = str(int(time.time())) + user
    pass