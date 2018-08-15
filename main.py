from transaction import abc_trans, company_trans, person_trans
from api import user_interact as ui
import os
import getpass

print('欢迎来到‘农兴贷’！\n请输入您的账号和密码。\n')

while 1:
    logIn = False
    logInName = input('账号：')
    if logInName=="qw:":
        os._exit(0)
    logInPassWord = getpass.getpass('密码：***')
    print()

    if logInName == 'abc' or logInName == 'company' or logInName == 'person':
        if logInPassWord == '1':
            logIn = True

    if logIn == False:
        print('用户名或密码错误！请重新输入！若想退出，请输入“qw:”')
    else:
        interact = ui()
        while 1:
            if logInName == 'abc':
                print('请选择您所需要的服务：\n1.账单查看；\n2.转账业务办理；\n3.退出登录；\n4.退出系统。\n')
                chooseService = input()
                if chooseService == '1':
                    #print('\n所有账单：')  moved to chaincode 
                    interact.abc_read_trans(logInName)
                elif chooseService == '2':
                    while 1:
                        print('请选择您要转予的用户：\n1. company\n2. person\n3. 返回')
                        toObject = input()
                        if toObject == '1':
                            toObjectName = 'company'
                            break
                        elif toObject == '2':
                            toObjectName = 'person'
                            break
                        elif toObject == '3':
                            break
                        else:
                            print('您输入的格式错误，请重新输入！')
                    if toObject == '3':
                        continue
                    print('请输入您要转出的金额：')
                    value = input()
                    while 1:
                        try:
                            value = float(value)
                        except Exception as e:
                            print('您输入的格式错误，请重新输入！')
                            value = input()
                            continue
                        break
                    amount, txn = interact.abc_seed_fund(value)
                    #toObjectName = 'company'  
                    newABCTrans = abc_trans('currency', txn, toObjectName, amount)
                    interact.abc_create_trans(newABCTrans)
                elif chooseService == '3':
                    break
                else:
                    os._exit(0)

            elif logInName == 'company':
                print('请选择您所需要的服务：\n1.账单查看；\n2.转账业务办理；\n3.退出登录；\n4.退出系统。\n')
                chooseService = input()
                if chooseService == '1':
                    #print('\n所有账单：')
                    interact.company_read_trans(logInName)
                elif chooseService == '2':
                    amount, txn = interact.choose_trans('company')
                    if txn == -1:
                        print('您没有可用的账单。\n')
                    elif txn == -2:
                        continue
                    else:
                        newCompanyTrans = company_trans('currency', txn, 'person', amount)
                        interact.company_create_trans(newCompanyTrans)
                elif chooseService == '3':
                    break
                else:
                    os._exit(0)

            elif logInName == 'person':
                print('请选择您所需要的服务：\n1.账单查看；\n2.业务账单登记；\n3.退出登录；\n4.退出系统。\n')
                chooseService = input()
                if chooseService == '1':
                    #print('\n所有账单：')
                    interact.person_read_trans(logInName)
                elif chooseService == '2':
                    amount, txn = interact.choose_trans('person')
                    if txn == -1:
                        print('您没有可用的账单。\n')
                    elif txn == -2:
                        continue
                    while 1:
                        print('请选择您的交易类型：\n1. 转账\n2. 发货\n3. 返回')
                        toObject = input()
                        if toObject == '1':
                            item = 'currency'
                            break
                        elif toObject == '2':
                            print('请输入您要发货的物品：')
                            item = input()
                            break
                        elif toObject == '3':
                            break
                        else:
                            print('您输入的格式错误，请重新输入！')
                    if toObject == '3':
                        continue
                    newPersonTrans = person_trans(item, txn, 'company', amount)
                    interact.person_create_trans(newPersonTrans)
                elif chooseService == '3':
                    break
                else:
                    os._exit(0)