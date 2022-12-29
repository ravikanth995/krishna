#recursion 
#Write a program to find factorial of a given number
# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# num=input("Enter Number:") 
# if num<0:
#     print("Sorry the Factorial Does not exist for Negative Number:") 
# elif num==0:
#     print("The Fqctorial of 0 is 1") 
# else :
#     print("The Factorial of:",num,"is",rec_fact(num))                

# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# num=int(input("Enter Number:"))
# if num<0:
#     print("Factorial Not Possible")
# elif num==0:
#     print("The Factorial of 0 is 1")
# else:
#     print("The Factorial",num,"is",rec_fact(num))   

# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# num=int(input("Enter Number:")) 
# if num<0:
#     print("Not Possible")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     print("Factorial of",num,"is",rec_fact(num))                      

# def fact_rec(n):
#     if n==1:
#         return n
#     else:
#         return n*fact_rec(n-1)
# num=int(input("Enter Number:")) 
# if num<0:
#     print("The Facto of negative is not possible")
# elif num==1:
#     print("Fact of 0 is 1")
# else:
#     print("fact is",num,"is",fact_rec(num)) 

# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# num=int(input("Enter Number:"))
# if num<0:
#     print("Not Possible")
# elif num==0:
#     print("fact of 0 is 1")
# else:
#     print("Factorial is",num,"is",rec_fact(num))

# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# num=int(input("Enter Number:"))
# if num<0:
#     print("Not Possible")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     print('Factorial of',num,'is',rec_fact(num))     

#Write a recursive function to find the sum of digits of a number
# l=[]
# def sum_digits(b):
#     if b==0:
#         return 1
#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)                                                                        
# num=int(input("Enter Number:"))
# sum_digits(num)
# print(sum(l))    

# l=[]
# def sum_digit(b):
#     if b==0:
#         return 1
#     dig=b%10
#     l.append(dig)
#     sum_digit(b//10)
# num=int(input("Enter Number:"))
# sum_digit(num)
# print(sum(l))        

# l=[]
# def sum_digits(b):
#     if b==0:
#         return 1

#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)
# num=int(input("Enter Number:"))
# sum_digits(num)
# print(sum(l))    

# l=[]
# def sum_digits(b):
#     if b==0:
#         return 1
#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)
# num=int(input("Enter Number:"))
# sum_digits(num) 
# print(sum(l))       

#Write a program to find the power of a number using recursion
# def power(base,p):
#     if p==0 or p==1:
#         return base
#     else:
#         return base*power(base, p-1)
# base=int(input("Enter Base:"))
# p=int(input("Enter power value:"))
# print("result",power(base,p))            

# def power(base,power1):
#     if power1==0 or power1==1:
#         return base
#     else:
#         return base*power(base, power1-1) 
# base=int(input("Enter Number:")) 
# power1=int(input("Enter Number:"))
# print("Results",power(base,power1))          

#Fibonacci Number
def fib_sum(n):
    if n<2:
        return 1
    else:
        return fib_sum(n-1)+fib_sum(n-2)  
fabseries=int(input("Enter a Number:"))
for i in range(fabseries):
    print(i,"=",fib_sum(i))    

# def fib_sum(n):
#     if n<2:
#         return 1
#     else:
#         return fib_sum(n-1)+fib_sum(n-2)
# fabseries=int(input("Enter Numbers:")) 
# for i in range(fabseries):
#     print(i,"=",fib_sum(i))                 

