def login(func1):
    def exec():
        print('Enter your amount here')
        func1()
        print('your payment is done')
    return exec

@login 
def payment():
    print('paid the amount')

payment()

@login
def remain_bal():
    print('your remained balance is')
remain_bal

