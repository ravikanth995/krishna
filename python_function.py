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

def tupleFun(*args):
    m_List=[]
    for args in args:
        m_List.append(args*19)
    return tuple(m_List)
t=tupleFun(2,4,6,10,19,16,18,19000)
print("Into Tuple:",t)        

