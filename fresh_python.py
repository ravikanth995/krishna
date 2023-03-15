#1. Reverse an integer
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reversed Integer is:",rev)    

#2. Write a progarm to check a given number is palindrome or not
# n=int(input("Enter Number:"))
# num=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The Reversed:",rev)
# if num==rev:
#     print("The Given Integers are Palindrome")
# else:
#     print("Please.. Enter Valid Palindrome Integer 121 or 545 !!")        

#3. Write a program to Check given integer is Prime Number or not
# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Given Integer is Prime Number")
# else:
#     print("Please.. Enter Valid Prime Number i.e., 2,3,5,7,11,13 !!")  

#4. Write a program to check a number is Perfect or not
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Given Integer is Perfect Integer")
# else:
#     print("Please.. Enter valid perfect integer i.e., 6 or 28")            

#5. Write a program to print fibonacci number
# x,y,z=0,1,0
# n=int(input("Enter Number:"))
# for i in range(1,12):
#     print(z)
#     x,y=y,x
#     z=x+y
# print(z)    

#6. Write a program to print armstrong number upto 407
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     num=i
#     i=str(i)
#     n=len(str(i))
#     sum=0
#     for j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print(num)

#7. Write a program to reverse the given string i.e., String is a Data Type 
#o/p = "Type Data a is String"
# inp="String is a Data Type"
# final=(inp.split()[::-1])
# print(" ".join(final))

#8. reverse every content in the String
# inp="freshner"
# print("reversed string:",inp[::-1])

#9. Write a program to remove duplicates from List
# l=[1,2,1,2,3,4,5]
# #o/p=[1,2,3,4,5]
# l1=[]
# for i in l: 
#     if i not in l1:
#         l1.append(i)
# print("List after duplicates removal:",l1)     

#10.
# l=[1,1,2,2,3,4,5]
# #o/p=[3,4,5]
# print([x for x in l if l.count(x)==1])

#11. 
# l=[1,1,2,2,3,4,5]
# #o/p=[1,2]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("List Before Duplicate removal:",l)
# print("List After Duplicates removal:",l1)       

#12.
# l="A1B2C3D4E5F6G7H8I9"
# alpha=[]
# num=[]
# for i in l:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         num.append(i)
# final=sorted(alpha)+sorted(num)
# print(" ".join(final))       

#13. 
# n=input("Enter String:")
# count=0
# vowels=['a','i','o','u','e']
# for i in n:
#     if i in vowels:
#       count+=1
# print("Number of Vowels:",count)      

# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1    

# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=i:
#         print("*",end="")
#         k+=1
#     print()
#     i+=1            

#Pyramid
# k=1
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end="")
#         j+=1
#     k+=2
#     print()
#     i+=1

# k=1
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end="")
#         j+=1
#     k+=2
#     print()
#     i+=1        

# k=1
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end="")
#         j+=1
#     k+=2
#     print()
#     i+=1        

# k=1
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end="")
#         j+=1
#     k+=2
#     print()
#     i+=1        

# d=1
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end="")
#         b+=1
#     c=1
#     while c<=d:
#         print("*",end="")
#         c+=1
#     d+=2
#     print()
#     i+=1        

# d=1
# a=1
# n=int(input("Enter Number:"))
# while a<=n:
#     b=1
#     while b<=n-a:
#         print(" ",end="")
#         b+=1
#     c=1
#     while c<=d:
#         print("*",end="")
#         c+=1
#     d+=2
#     print()
#     a+=1       

# a=1
# n=int(input("Enter Number:")) 
# while n>0:
#     b=1
#     while b<a:
#         print(" ",end="")
#         b+=1
#     c=1
#     while c<=n*2-1:
#         print("*",end="")
#         c+=1
#     n-=1    
#     print()
#     a+=1        

#1.
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print(rev)   

#2.
# n=int(input("Enter Number:"))
# num=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The Reversed Integer is:",rev)
# if num==rev:
#     print("The Number is Palindrome")
# else:
#     print("The Integer is not Palindrome")        

#3.
# n=int(input("Enter Number:"))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime number")
# else:
#     print("Not Prime Number")            

#4.
# x,y,z=0,1,0
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print("The Fibonacci are:",z)    

#5.
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#    print("Perfect Number")
# else:
#     print("Not Perfect Number")         

#6.
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     num=i
#     i=str(i)
#     n=len(str(i))
#     sum=0
#     for  j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print(num)

#7.
# l="Blue is Sky"
# final=(l.split()[::-1])
# print(" ".join(final))

# #8.
# l="kutra"
# print(l[::-1])

#9.
# l=[1,2,1,2,3,4]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)        

#10.
# l=[1,2,1,2,3,4,5]
# print([i for i in l if l.count(i)==1])
          
# #11.
# l=[1,2,3,4,1,2,3,4,5,6,6]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print(l1)            

#12.
# l="A1B2C3D4E5F6G7H8I9J10"
# alpha=[]
# nums=[]
# for i in l:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         nums.append(i)
# final=sorted(alpha)+sorted(nums)
# print(" ".join(final))            

# l=input("Enter String:")
# count=0
# vowels=['a','e','i','o','u']
# for i in l:
#     if i in vowels:
#         count+=1
# print(count)           

#13.
# i=1
# n=int(input("Enter Number:"))
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1   

#14.
# k=1
# i=1
# n=int(input("Enter number:"))
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end="")
#         j+=1
#     c=1
#     while c<=k:
#         print("*",end="")
#         c+=1
#     k+=2
#     print()
#     i+=1    

# #15.
# fact=1
# i=1
# n=int(input("Enter Number:"))
# while n>=i:
#     fact*=i
#     i+=1
# print("Factorial is:",fact)   

#16.
# pi=3.142
# r=float(input("Enter radius:")) 
# area=pi*r*r
# cirumference=2*pi*area
# print("Area is:",area)
# print("Circumference is:",cirumference)

#17.
# cel=float(input("Enter Celcius:"))
# far=(cel*1.8)+32
# print("Celcius",cel,"Farhenhiet is:",far)

#18.
p=float(input("Enter Principal Amount:"))
t=float(input("Enter Time Period:"))
r=float(input("Enter rate of interest:"))
si=p*r*t/100
amount=si+p
print("Principal Amount is:",p,"\nTime is:",t,"\nRate of Interest is:",r,"\nSimple Interest is:",si)
print("Total Amount is:",amount)

#19.
# p=float(input("Principal Amount:"))
# r=float(input("Enter Rate of Interest:"))
# t=float(input("Enter Time Period:"))
# Amount = p * (pow((1 + r / 100), t))
# CI = Amount - p
# print("Compound interest is", CI)
  




