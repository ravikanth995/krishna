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

# def Add(a,b):
#     print("Addition:",a+b)
# def Sub(a,b):
#     print("Subtraction:",a-b)
# def Multi(a,b):
#     print("Multiplication:",a*b)
# def Div(a,b):
#     print("Division:",a/b) 

# x=int(input("Enter X Value:"))
# y=int(input("Enter Y Value:"))
# Add(x,y)
# Sub(x,y)
# Multi(x,y)
# Div(x,y)               

#Types of Parameters and Formal Arguments
#1.Positional argument or required argument
#2.default argument
#3.Keyward Argument
#4.Variable Length Arguments
#5. Keyword Variable Length Argument


# def reqArgfun(a,b):
#     print(a,b)
# reqArgfun(12,100)
# reqArgfun(100,12)    

# def argfun(a,b):
#     print(a,b)
# argfun(100,12)
# argfun(12,100)    

# def reqArgfun(num,str):
#     print(num,str)
# reqArgfun(12,"apple")
# reqArgfun("apple",12)    

#Default Argument
# def myfun(name="Balaji argument"):
#     print("Hello",name,"Thank You")
# myfun()
# myfun("Pawan Argument")    

# def myFun(name="Advait Vedant"):
#     print("Hello",name,"Rakshak")
# myFun()
# myFun("Dhoka Diya bro")    

# def myFun(name="Conciousness"):
#     print("Hi..",name,"meet you")
# myFun()
# myFun("Upanishads")    

# def Turbine(name="Default Arg"):
#     print("Hello..",name,"Okay")
# Turbine()
# Turbine("Fun")

# def wish(name="guest", msg="good morning"):
#        print("Hi.",name,msg,"welcome") 
# wish()
# wish("Not come")          

# def wish(name="guest", msg="good morning"):
#     print("hello..",name,msg)
# wish()
# wish("Good after")    

# def myFun(name="Balaji Publication", name1="ABC"):
#     print("Hello",name,"Thank You",name1)
# myFun()
# myFun("Ravikanth")    

# def reqArgFun(name,msg):
#     print(name,msg)
# reqArgFun(name="Tbalaji", msg="Computer Book")
# reqArgFun(msg="Computer Book",name="Tbalaji")    

# def myFun(name,msg):
#     print("hello", name,msg)
# myFun("Banana","Indian fruit")    
# myFun("mango",msg="yummy")
# myFun(name="Appke","awesome")

# def sum(*n):
#     total =0
#     for a in n:
#         total+=a
#     print("The Sum is=",total)
# sum()
# sum(10)
# sum(1,2,3)
# sum(1,2,3,4,5,6,7,8)    

# def sum(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("the Sum is=",total)
# sum()
# sum(10)
# sum(1,2,3)
# sum(1,2,3,4,5,6)        

# def multi(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("The Sum is=",total)
# multi()
# multi(10)
# multi(1,2,3,4)
# multi(12,34,21)        

# def multi(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("The Sum is=",total) 
# multi()
# multi(2)
# multi(1,2,3,4)       

# def sum(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("The Sum is:",total)
# sum()
# sum(1,2)
# sum(1,2,4,6,9)        

# def sum(*n):
#     total=0
#     for a in n:
#         total+=a
#     print("The SUm is:",total)
# sum()
# sum(1,2,3,4)
# sum(10,20,30,50) 

# def sum(*n):
#     total=0
#     for a in n:
#         total+=a
#     print("The Sum is :",total)
# sum()
# sum(1,2,3)
# sum(10,20,30,40)

# def myFun(n,*s):
#     print(n)
#     for a in s:
#         print(a)
# print("MyFun(10) Output is:")
# myFun(10)
# print("myFun (10,20,30,40) Output:") 
# myFun(10,20,30,40)
# print("myFun (10,'a',20,'b'):")
# myFun(10,'a',20,'b')      

# def myFun(*n,s):
#     for a in n:
#         print(a)
#     print(s)

# myFun('A',"B",s=100)             

# def myFun(*n,s):
#     for a in n:
#         print(a)
#     print(s)
# myFun('A','B',s=100)        

# def myFun(*n,s):
#     for a in n:
#         print(a)
#     print(s)
# myFun('A','B',s=99)        

# def myFun(**n):
#     for a, b in n.items():
#         print(a,"=",b)
# print("Calling myfun(n1=100,n2=200,n3=300,n4=400)")
# myFun(n1=100,n2=200,n3=300,n4=400)
# print("Calling myfun(rno=1, name=Ravi, marks=89, subject=python)")
# myFun(rno=1, name="ravi", marks=89, subject="python")      

# def myfun(**n):
#     for a,b in n.items():
#         print(a,"=",b)
# print("Calling myFun(n1=100,n2=200,n3=300,n4=400")
# myfun(n1=100,n2=200,n3=300,n4=400)
# print("Rno=1, name=Ravi, Marks=300, Sub=Python")
# myfun(Rno=1, name="Ravi", Marks=300, Sub="Python")          

# def myFun(**n):
#     for a, b in n.items():
#         print(a, "=", b)
# print("N1=100, N2=200, N3=300, n4=400")
# myFun(n1=100, n2=200, n3=300, n4=400)
# print("Rno=1, name=ravi, marks=300, SUb=Python")
# myFun(Rno=123, name="Ravi", marks=600, sub="Python" )        

# def myFun(**n):
#     for a,b in n.items():
#         print(a, "=", b)
# print("n1=100, n2=200, n3=300, n4=400")
# myFun(n1=100, n2=200, n3=300, n4=400)
# print("Rno=14627, name=ravi, Marks=900, Sub=Python") 
# myFun(Rno=1387762, name="Ravi", marks=7900, sub="Python")       

# def myFun(**n):
#     for a,b in n.items():
#         print(a,"=",b)
# myFun(n1=100, n2=200, n3=300, n4=400) 
# myFun(Rno=2671, name="Ravi", marks=234, Sub="Python")       

# def myFun(a,b, c=300, d=400):
#     print(a,b,c,d)
# myFun(3,2)
# myFun(1,2,3,4)
# myFun(3,4,2,d=100)
# myFun(d=300, a=2, b=6)

def myFun(a,b,c=100,d=500):
    print(a,b,c,d)
myFun(1,2)
myFun(1,2,3,5)
myFun(1,2,c=400,d=588)
myFun(a=2,c=400,b=7)    
