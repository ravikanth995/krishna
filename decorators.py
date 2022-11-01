def login(func1):
    def exec():
        print('Enter Your Amount')
        func1()
        print('Payment is Done')
    return exec    
@login
def payment():
    print('Payment is paid to Ravikanth')

payment()



@login 
def checkbal():
    print('Your Bank Balance is')

checkbal()
