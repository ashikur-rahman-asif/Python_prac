#the program simulated the passsword protected apps

password_bank={'Asif':19714,'Alice':28756,'Robert':74878}
matched=False
x=0 #loop control
print('Enter your name')
while x<5:
    name=input()
    if name in password_bank:
        for i in range(0,3):
            print('Enter your password:')
            password=input()
            if int(password) in password_bank.values():
                matched=True
                print('access granted')
                break
            else:
                print('Wrong password!! entered again'+ 'You have ' +str(2-i)+ ' tries left')
    else:
            print('there is no such name in the password bank!,try again')
    #x=x+1
    if matched:
        break

