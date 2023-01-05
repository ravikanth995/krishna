# Scope and Modules
#Four Types of Namespaces
#1. Bulti-in
#2. Global
#3. Enclosing
#4. Local

# pi='global pi variable'
# def inner():
#     pi='inner pi variable'
#     print(pi)
# inner()    

#Local and Global Scope
#global scope
# pi='Global pi variable'
# def inner():
#     pi='inner pi variable'
#     print(pi)
# inner()
# print(pi)    

#Local, Enclosed and Global
#Enclosed
# pi='global variable'

# def outer():
#     pi='Outer variable'
#     def inner():
#         # pi='Inner pi variable'
#         nonlocal pi
#         print(pi)
#     inner()

# outer()    
# print(pi)        

# from math import pi
# # pi='global pi variable'
# def outer():
#     # pi='outer pi variable'
#     def inner():
#         # pi='inner variable'
#         print(pi)
#     inner()
# outer()        

#Packages and Module
#Packages
#it is a directory that holds and contains modules and sub-packages
#To Create Packages

#Module Basics
# def fun():
#     if '__name__'=='__main__':
#         print("The Code Executed as a program")
#     else:
#         print("The Code Executed as a Module from some othere program")
# fun()            

# def fun():
#     if '__name__'=='__main':
#         print("Program Executed Individually")
#     else:
#         print("The Program Executed as a module from other program")
# fun()

#To print all memebers of current module and importing module
# import example
# x=20
# y=29
# def fun1():
#     print("Fun()")

# def fun2():
#     print(x+y)

# print("Current Module List:\n",dir())
# print("Example Module List:\n",dir(example))   

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Cuurent Time:",local_time)

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Time Is:",local_time)

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Time is:",local_time)

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Day:Month:Date:Time:Year:",local_time)

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Local Current Time:",local_time)

# import time
# local_time=time.asctime(time.localtime(time.time()))
# print("Local Current Time:",local_time)

#calender of the Particular Month
# import calendar
# print(calendar.month(2023,1))

# import calendar
# print(calendar.month(2023,2))

