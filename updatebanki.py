bank_users={'Alice' : 1233, 'Sam' : 25000,'Robert' : 30000}
print('Welcome to the bank')
while True:
    print('What do you like to do?')
    print(' ''1.View Balance')
    print(' ''2.View all bank info')
    print(' ''3.Update Balance')
    print(' ''4.Exit')
    desc= input()
    if desc == '1':
        print('Enter your name please:')
        k=input()
        if k in bank_users.keys():
            print(k+' Your bank balance is '+str(bank_users[k]))
        else:
            print('The user cant be found.Would you like to add the user to the account?')
            desc=input()
            if desc=='YES':
                k=input('Enter your name please:')
                v=input('Enter your balance:')
                bank_users.update({k:v})
            else:
                print('Would you like to exit?')
                desc=input()
                if desc=='YES':
                    break
    elif desc=='2':
        for k,v in bank_users.items():
            print('USERNAME: '+str(k)+'BALANCE '+str(v))
    elif desc=='3':
        print('Enter your name please:')
        k=input()
        if k in bank_users.keys():
            print('Do you want to add or substract from your savings?')
            desc=input()
            if desc=='ADD':
                temp_balance=bank_users[k]
                extra=input('Enter the amount you want to add: ')
                bank_users[k]=temp_balance+int(extra)
                print('Balance updated, the balance is ')
                print(bank_users[k])
            elif desc=='SUBSTRACT':
                temp_balance=bank_users[k]
                extra=input('Enter the amount you want to substract')
                bank_users[k]=temp_balance-int(extra)
                print('Balance updated, it is ')
                print(bank_users[k])
        else:
            print('There is no such acnt in the bank database')
    elif desc=='4':
        break





