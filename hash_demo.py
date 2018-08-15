#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:19:08 2018

@author: fury
"""

import hashlib

m = hashlib.md5()  #创建md5对象
m.update('abcdefg'.encode()) #生成加密串，其中password是要加密的字符串
print (m.hexdigest())
m1 = hashlib.md5()
m1.update('abcdefg'.encode()) #生成加密串，其中password是要加密的字符串
print (m1.hexdigest())

#import os,sys  
#reload(sys)  
#sys.setdefaultencoding('utf8') 
#import string
 
def suanfa(key):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    jiami_key = {}
    jiemi_key = {}
 
    list0 = list(alp)
    list1 = list(key)
    list2 = list(alp)
    for n in list1:
        for m in list2:
            if m == n:
                list2.remove(m)
 
    alp1 = ''.join(list2)
    key1 = key + alp1
    list3 = list(key1)
 
    a = 0
    if a < len(list0):
        for m in list0:
            jiami_key[m] = list3[a]
            a = a + 1
    
    b = 0
    if b < len(list3):
        for n in list3:
            jiemi_key[n] = list0[b]
            b = b + 1
    
    #print jiami_key
    #print jiemi_key
    return jiami_key, jiemi_key  
 
def bianma(key_dic, data):
    list_data = list(data)
    data1 = []
    for a in list_data:
         if a == ' ':
             data1.append(a)
 
         elif a.islower():
             a = a.upper()
             if a in key_dic:
                 x = key_dic[a]
                 data1.append(x.lower())
 
         elif a.isupper():
             if a in key_dic:
                 x = key_dic[a]
                 data1.append(x)
         else:
             data1.append(a)
 
    data2 = ''.join(data1)
    #print data2
    return data2
 
def main():
    key = 'ZDFKJMNX'
    data = 'a bdcd sFDGDSGFDG113243 3'
    print ("秘钥：" + key)
    print ("明文：" + data)
 
    jiami_key, jiemi_key = suanfa(key)
    miwen = bianma(jiami_key, data)
    mingwen = bianma(jiemi_key, miwen)
 
    print ("加密明文所得的密文：" + miwen)
    print ("解密密文所得的明文：" + mingwen)
    return True
 
if __name__ == "__main__":
    main()