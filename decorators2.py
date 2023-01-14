# def shout(text):
#     return text.upper()
# print(shout("Hello")) 
# yell=shout
# print(yell("Hellos"))

# def shout(txt):
#     return txt.upper()
# def whisper(txt):
#     return txt.lower()
# def greet(func):
#     greeting=func("Hi, I am created by an function passed as an argument")
#     print(greeting)
# print(shout)
# print(whisper)           

# def creat_adder(x):
#     def adder(y):
#         return x+y
#     return adder
# add_15=creat_adder(15)
# print(add_15(10))        

# def create_adder(x):
#     def inner(y):
#         return x+y
#     return inner
# add_15=create_adder(17)
# print(add_15(10))        

# def creator(x):
#     def inner(y):
#         return x+y
#     return inner
# add_15=creator(12)
# print(add_15(10))        

# def creator_adder(x):
#     def inner(y):
#         return x+y
#     return inner
# add_15=creator_adder(18)
# print(add_15(19))        

# def creator_add(x):
#     def inner(y):
#         return x+y
#     return inner
# add=creator_add(17)
# print(add(100))        

# def creator_adder(x):
#     def inner(y):
#         return x+y
#     return inner
# add_no=creator_adder(198)
# # print(add_no(89))    

# def hello_decorator(func):
#     def inner(*args,**kwargs):
#         print("Before Execution")
#         return_value=func(*args,**kwargs)
#         return return_value
#     return inner
# @hello_decorator
# def sum_of_number(a,b):
#     print("inside the Function")
#     return a+b
# a,b=90,1 
# print("Sum is:",sum_of_number(a,b))       

# def decor1(func1):
#     def exec():
#         # name=input("Enter Your Name:")
#         print("Enter Your Name is:")
#         func1()
#         print("Your Payment is Done:")
#     return exec

# @decor1
# def payment():
#     print("Payment 100Rupees is Transfered to Ravikanth")

# payment()

# @decor1
# def checkBal():
#     print("Your Balance left is:")
# checkBal()    

# def login(func):
#     def exec():
#         print("Enter Your Name:")
#         func()
#         print("Your Payment is Done")
#     return exec
# @login
# def payment():
#     print("Rupee 50 is Paid")
# payment()

# @login
# def checkBal():
#     print("Balance Left is:")
# checkBal()    

# def login(func):
#     def exec():
#         print("Enter Your Name")
#         func()
#         print("Your Payment is Done")
#     return exec
# @login
# def Payment():
#     print("Your have paid 1000rupee")
# Payment()
# @login
# def checkBal():
#     print("Balance left is:")
# checkBal()                

# def login(func):
#     def exec():
#         print("Your Name :")
#         func()
#         print("Amount Payment is Done")
#     return exec
# @login
# def Payment():
#     print("1,00,000 is paid")
# Payment()
# @login
# def checkBalance():
#     print("Balance left is:")
# checkBalance()    

# def login(func):
#     def exec():
#         print("Please, Enter Your Name:")
#         func()
#         print("Payment is being done")
#     return exec
# @login
# def Payment():
#     print("100 is Paid:") 
# Payment()
# @login
# def checkBal():
#     print("Remaining Balance is:")
# checkBal()               

# def login(func):
#     def exec():
#         # name=input("Enter Your Name:")
#         print("Please, Enter Name")
#         func()
#         print("Your Payment is Done")
#     return exec
# @login
# def payment():
#     print("You paid 1 rupees")
# payment()
# @login
# def checkBalance():
#     print("Balance is")
# checkBalance()        

#Chaining the Decorators
def decor(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor2(func1):
    def inner1():
      x=func1()
    return 2*x
@decor
# @decor2
def num():
    return 10
num()     
