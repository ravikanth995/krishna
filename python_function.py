# def even():
#     if x%2==0:
#         print("is even number")
#     else:
#         print("Odd number") 
#         return 
# x=int(input("Enter Number:"))
# even()         

# def even():
#     if x%2==0:
#         print("Even number")
#     else:
#         print("Odd number") 
#         return
# x=int(input("Enter Number:"))
# even()           

#Local Variables
# def fun():
#     a="Local"
#     print(a)
# fun()    

#error in Local Variable
# def fun():
#     a="Python"
# print(a)
# fun()    

# #Global Variables
# a="Python"
# def fun():
#     print(a)
# def fun1():
#     print(a)
# print("calling Function 1 and 2")
# fun()
# fun1()        

# a=10
# def fun():
#     a=a*10
#     print(a)
# fun()    

#Python program to modify a global value inside a function
# c=100
# print("Before calling modify function 'c' value is",c)
# def modify():
#     global c
#     c=100
#     print("Inside function 'c' value is:",c)
#     print("End Modify()")
# modify()
# print("outside function 'c' value is:",c)    

#Return statement
#Write a function to accept two numbers as input and return sum
# def add(a,b):
#     return "a is",a,",b is","a+b=",a+b
# result=add(10,15)
# print("sum of two value is:",result)
# print("Sum of two value is:",add(100,200))

# def add(a,b):
#     return "a is",a,",b is,",b,"a+b=",a+b
# result=add(10,17)
# print("Sum of two value is:",result)
# print("Sum of two value is:",add(100,150))    

#if we are not writing return statement then default retrurn value is none
# def add(a,b):
#     print("Without return statement")
# result=add(10,17)
# print("The Sum of two value is:",result)
# print("Sum of two value is:",add(800,7))    

# def calc(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     f=a/b
#     return c,d,e,f
# x=15
# y=10
# add,sub,multi,div=calc(x,y)
# print("Addition of two number is:",add)
# print("Subtraction of two number:",sub)
# print("Multiplication of two number:",multi)
# print("Division of two number is:",div)    

# def cal(a,b):
#     c=a+b
#     d=a-b
#     e=a/b
#     f=a*b
#     return c,d,e,f
# x=19
# y=100    
# add,sub,div,multi=cal(x,y)
# print("Add of two value is:",add)
# print("Sub of two value is:",sub)
# print("Div of two value is:",div)
# print("Multi of two value is:",multi)    

#Above value in different way
# def cal(a,b):
#     return a+b, a-b, a*b, a/b
# x=20
# y=19
# result=cal(x,y)
# for i in result:
#     print(i)    

# def cal(a,b):
#     return a+b, a-b, a*b,a/b
# x=8.1
# y=10
# result=cal(x,y)
# for i in result:
#     print(i)    

#Boolean function using return
# def TupleFun(*args):
#     mList=[]
#     for args in args:
#         mList.append(args*10)
#     return tuple(mList)
# t=TupleFun(1,2,3)
# print("Tuple returned by Tuple(1,2,3) is :",t)  


# def TupleFun(*args):
#     m_List=[]
#     for args in args:
#         m_List.append(args*10)
#     return tuple(m_List)
# t=TupleFun(1,2,3)
# print("Tuple returned by TupleFun is:",t)            

# def tupleFun(*args):
#     m_List=[]
#     for args in args:
#         m_List.append(args*20)
#     return tuple(m_List)
# t=tupleFun(1,2,3)
# print("tuple returned by TupleFun(1,2,3:",t)        

# def tupleFun(*args):
#     m_List=[]
#     for args in args:
#         m_List.append(args*10)
#     return tuple(m_List)
# t=tupleFun(1,2,3,4)
# print("Tuple returned by tupleFun(1,2,3:",t)        

# def tupleFun(*args):
#     m_List=[]
#     for args in args:
#         m_List.append(args*10)
#     return tuple(m_List)
# t=tupleFun(1,2,3,4,5)
# print("Tuple returned by TupleFun is:",t) 

# def tupleFun(*args):
#     my_List=[]
#     for args in args:
#         my_List.append(args*10)
#     return tuple(my_List) 
# t=tupleFun(8,5,3,1)
# print("Into Tuple is:",t)        

# def tupleFun(*args):
#     m_List=[]
#     for args in args:
#         m_List.append(args*19)
#     return tuple(m_List)
# t=tupleFun(2,4,6,10,19,16,18,19000)
# print("Into Tuple:",t)        

#DocString
# def power(a,b):
#     """returns arg1 raised to power arg2"""
#     return a**b

# def sample_func():
#     '''this functions prints hello World!'''
#     print("Hello World!")
#     return 
# print("Method-1:-")
# help(sample_func)
# print("method-2-:") 
# print(sample_func.__doc__)   

# y,z=1,2
# def all_global():
#     global x
#     x=y+z
#     print(x)
# all_global()    
# print(x)

#OneLine Docstring
# def power(a,b):
#     """returns arg1 raised to power arg2"""
#     return a**b

#Multi-Line Docstring
# def my_function(arg1):
#     """
#     Summary Line.
#     Extended description of function.
#     parameters:
#     arg1(int): description of arg1
    
#     returns :
#     int: description of return value

#     """
#     return arg1

#Accessing DocString
# def sample_func():
#     '''this function prints Hello World!'''
#     print("Hello World!")
#     return
# print("Method 1:-")
# help(sample_func)
# print("Method 2:-")
# print(sample_func.__doc__)

# def sample_func():
#     '''this function prints Hello World!'''
#     print("Hello World!")
#     return
# print("Method 1:-")
# print(sample_func)
# print("Method 2-:") 
# print(sample_func.__doc__)       

# z,y=1,2
# def all_global():
#     global x
#     x=y+z
#     print(x)
# all_global()
# print(x)    

# z,y=1,2
# def all_global():
#     global x
#     x=z+y
#     print(x)
# all_global()
# print(x)    

# z,y=1,2
# def all_global():
#     global x
#     x=z+1
#     print(x)
# all_global()
# print(x)    

# #Functions Parameters and Arguments
# def fun(a,b):# Fomal argument
#     print("First Value:",a)
#     print("Second Value:",b)
#     return a+b
# x=fun(10,20) #Actual argument
# print("Addition of two number is:",x)

# def func(a,b):
#     print("First Value:",a)
#     print("Second Value:",b)
#     return a+b
# x=func(10,40)
# print(x)    

#A function that accepts a string as the parameters and prints it
# def fun(name):
#     print("Hello",name)
# fun(input("Enter your name:"))    

# def func(name):
#     print("Hello !",name)
# func(input("Enter your name:"))   

# def func(name):
#     print("hello !",name)
# func(input("Enter name:"))     

# def func(name):
#     print("Hi..",name)
# func(input("Enter Name:"))    

# def func(name):
#     print("Hi...",name)
# func(input("Enter Name:"))    

# def fun(name):
#     print("Hi...",name)
# fun(input("Enter Name:")) 

#Find out Passing argument is an odd or even 
# def funEO(x):
#     if x%2==0:
#         print("Even Number:")
#     else:
#         print("odd Number")
# funEO(1)
# funEO(2)
# funEO(3)          

# def funEO(x):
#     if x%2==0:
#         print("Even Number:")
#     else:
#         print("odd Number:")
# funEO(1)
# funEO(2)
# funEO(8)              

#Create a Small calculator(Addition, Subtraction, multiplication, division) program by using function
# def add(a,b):
#     print("Addition of Two Values:",a+b)
# def Sub(a,b):
#     print("Subtraction of Two Values:",a-b)
# def Multi(a,b):
#     print("Multiplication of Two Number:",a*b)
# def Div(a,b):
#     print("Division of Two Values:",a/b)

# x=int(input("Enter X Value:"))
# y=int(input("Enter Y Value:"))

# add(x,y)
# Sub(x,y)
# Multi(x,y)
# Div(x,y)

# def Add(a,b):
#     print("Addition of Two Values:",a+b)
# def Sub(a,b):
#     print("Subtraction of Two Values:",a-b)
# def Multi(a,b):
#     print("Multiplication of Two Values:",a*b)
# def Div(a,b):
#     print("Division of Two Value:",a/b)

# x=int(input("Enter X Value:"))
# y=int(input("Enter Y Value:"))
# Add(x,y)
# Sub(x,y)
# Multi(x,y)
# Div(x,y)

def Add(a,b):
    print("Addition:",a+b)
def Sub(a,b):
    print("Subtraction:",a-b)
def Multi(a,b):
    print("Multiplication:",a*b)
def Div(a,b):
    print("Division:",a/b) 

x=int(input("Enter X Value:"))
y=int(input("Enter Y Value:"))
Add(x,y)
Sub(x,y)
Multi(x,y)
Div(x,y)               

