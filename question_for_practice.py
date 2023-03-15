#1. Write a program to reverse an integer
#output  : 12345
#input : 54321
# n=int(input("Enter Integers:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The Reversed Number is:",rev)    

#2. Write a program to prove which one is Palindrome
#input : 121 or 123
# n=int(input("Enter Number:"))
# num=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The reversed number is:",rev)
# if num==rev:
#     print("The Number is Palindrome")
# else:
#     print("The Number is not Palindrome")        

#3. Write a program to print sum of given fibonacci numbers
# x,y,z=0,1,0
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print("Fibonacci Numbers are:",z)    

#4. Write a program to print Prime Numbers
# #input: 7 or 9
# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Number is Prime Number") 
# else:
#     print("Given Integer is not Prime Number")      

#5. Write a program to print perfect number
# n=int(input("Enter Number:"))
# num=n
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==num:
#     print("given Integer is Perfect")
# else:
#     print("Not Perfect number")       

#6. Armastrong Number
# for i in range(1,408):
#     num=i
#     i=str(i)
#     n=len(str(i)) 
#     sum=0
#     for j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print(num)     

# 7. 
# l=[1,1,1,2,3,4,5,5,6]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print("Duplicates after removal is :",l1)        

#8. 
#  l=[1,1,1,2,2,3,4,4,4,5,6]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("After Duplicates removal:",l1)            


