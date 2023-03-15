#Write a python program to reverse an integer in Python
# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("reversed number is:",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The Reversed Number :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("Reversed Number is:",rev)    

#Palindrome NUmber
# num=int(input("Enter Number:"))
# rev=0
# x=num
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("Reverse of a nmber is :",rev)    
# if rev==x:
#     print("Number is Palindrome")
# else:
#     print("The Number is not Palindrome")    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The Reversed Number is :",rev)

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num//=10
# print("The reversed number is :",rev)    

# num=int(input("Enter Number:"))
# count=0
# i=1
# while num>=i:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Prime NUmber")
# else:
#     print("Not Prime Number")    

# num=int(input("Enter Number:"))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime Number") 
# else:
#     print("Not Prime Number")           

# num=int(input("Enter Number:"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime Number")
# else:
#     print("Not prime Number")     

# num=int(input("Enter Number:"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")           

# n=int(input("Enter Number:"))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime number")
# else:
#     print("Not prime")                

#Perfect number
# n=int(input("Enter Number:"))
# sum=0
# num=n
# for  i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Perfect number")
# else:
#     print("Not Perfect number")    

# n=int(input("Enter Number:"))
# num=n
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Number is Perfect Number") 
# else:
#     print("Not Perfect number")         

# n=int(input("Enter Number:"))
# sum=0
# num=n
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Perfect Number")
# else:
#     print("Not Perfect number")       

# n=int(input("Enter Number:"))
# sum=0
# num=n
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Perfect number")
# else:
#     print("not")           

# n=int(input("Enter Number:"))
# num=n
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")      

# n=int(input("Enter Number:"))
# sum=0
# num=n
# i=1
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if num==sum:
#     print("Perfect Number")
# else:
#     print("Not Perfect number")     

#1. Reverse Number.
#Input : 65432
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The reversed numbers are:",rev)    
                    
#2. Find the Number is a palindrome is or not
#input : 909
# n=int(input("Enter Number:"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The reversed number is:",rev)
# if num==rev:
#     print("The Given integer is Palindrome") 
# else:
#     print("The Given Integer is not Palindrome")      

#3. Write a program to print armstrong number between 1-407
# for i in range(1,408):
#     num=i
#     i=str(i)
#     n=len(str(i))
#     sum=0
#     for j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print("Armstrong Numbers is:",num) 

#4. Write a program to print sum of Fibonacci Numbers between 1-9 integer
# x,y,z=0,1,0
# num=int(input("Enter Number:"))
# for i in range(1,num):
#     print(z)
#     x,y=y,z
#     z=x+y
# print(z)    

#5. Write a program to check wether a given number is perfect or  not.
# n=int(input("Enter NUmber:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Given Integer is Perfect") 
# else:
#     print("Please.. Enter Valid Perfect Number")    

#6. Write a program to print Prime numbers by using input method
# num=int(input("Enter Number:"))
# i=1
# count=0
# while num>=i:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Given integer is Prime") 
# else:
#     print("Please.. Enter Valid Prime Number")           

#Write a program to remove repeated duplicates from the list
# l=[1,1,2,2,3,3,4,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print("The list after removal of duplicates:",l1)  

#Write a program to print only repeated integers in a list
# l=[1,1,1,2,2,3,3,4,5]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("Raw List numbers:",l)            
# print("Printing only repeated numbers:",l1)     

# l=[1,1,2,2,3,3,5,6]
# print([x for x in l if l.count(x)==1])        

# l=input("Enter String:")
# l1=['a','e','i','o','u']
# count=0
# for i in l:
#     if i in l1:
#         count+=1
# print("NUmbers of vowels:",count)      

#Write a program to sort alphabets and numners, first alphabets and numbers
# l="S1F5J0M7G5D3"
# alpha=[]
# num=[]
# for i in l:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         num.append(i)
# final=sorted(alpha)+sorted(num)
# output=" ".join(final)
# print(output)         

#1. Write a program to print reversed by using input method
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reversed Integers are:",rev)    

#Write a program to print wether a integer is a palindrome or not
# n=int(input("Enter Number:"))
# num=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The reversed integer are:",rev)
# if num==rev:
#     print("The Given Integer is Palindrome")
# else:
#     print("The Given Integer is not Palindrome")

#3. Write a program to print armstrong number
# n=int(input("Enter Number:"))
# for i in range(1,n):
#     num=i
#     i=str(i)
#     n=len(str(i))
#     sum=0
#     for j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print(num)

#Write a program to print fibonacci number
# x,y,z=0,1,0
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print("Fibonacci Number:",z)    

#Write a program to print perfect number
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("Perfect Number")
# else:
#     print("No Perfect")  

#perfect number
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Integer is an Perfect")
# else:
#     print("Please... Enter Valid Perfect Number")   

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Integer is Perfect Number")
# else:
#     print("Please.. Enter Valid Integer")         

# n=int(input("Enter Integer:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Intger is an Perfect Number") 
# else:
#     print("Please.. Enter Valid Perfect Integer")  

# n=int(input("Enter Integer:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Integer is a Perfect Number")
# else:
#     print("Please.. Enter Valid Perfect Integer")        

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Integer is a Perfect Number:") 
# else:
#     print("Please.. Enter Valid Perfect Number")   

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Given Integer is Perfect Number")
# else:
#     print("Please... Enter Valid Perfect Integer")                                                       

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Integer is Perfect Number")
# else:
#     print("Please... Enter Valid Perfect Integer")    

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("The Integer is Perfect Number")
# else:
#     print("Please... Enter Valid Perfect Integer")    

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("The Integer is Perfect Number")
# else:
#     print("Please... Enter valid perfect integer") 

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Integer is Perfect Number")
# else:
#     print("Please.. Enter Valid Perfect Number")     

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Integer is Perfect Number:")
# else:
#     print("Please... Enter Valid Perfect Number")          

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Number is Perfect") 
# else :
#     print("Please... Enter Valid Perfect Number")

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Entered Number is Perfect")
# else:
#     print("Please... Enter Valid Perfect Number")            

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Integer is Perfect Number")
# else:
#     print("Please... Enter Valid Perfect Number")            

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Number is Perfect")
# else:
#     print("Please... Enter Valid Perfect Number")            

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Number is Perfect Number")
# else:
#     print("No Perfect Number")          

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Integer is Perfect Number")
# else:
#     print("Please.. Enter Valid Perfect Number")              

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Perfect Number")
# else:
#     print("No Perfect")            

#Prime Number
# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Given Number is Prime")
# else:
#     print("The Given integer is not Prime")            

# n=int(input("Enter Number:"))
# i=1
# count=0
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")     

# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Entered Integer is Prime Number")
# else:
#     print("Please... Enter Valid Prime Number i.e., 2,3,5,7,11,13 !!")                   

# n=int(input("Enter Number:"))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Entered Integer is Prime Number")
# else:
#     print("Please.. Enter Valid Prime Number i.e., 2,3,5,7,11,13!!")       

# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Entered Integer is Prime Number")
# else:
#     print("Please.. Enter Valid Prime Number i.e., 2,3,5,7,11,13 !!")    

# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Entered Integer is Prime Number")
# else:
#     print("Please... Enter Valid Prime Number i.e., 2,3,5,7,11 !!")           

#1. Reverse an Integer
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reversed Integer:",rev)    
            
#2. Write a program to check a wether a number is a Palindrome or not
# n=int(input("Enter Number:"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# if num==rev:
#     print("The Entered Integers are Palindrome")
# else:
#     print("Please.. Enter Valid Integer i.e., 121, 131, 909 !!")    

#3. Write a program to print Fibonacci numbers
# n=int(input("Enter Number:"))
# x,y,z=0,1,0
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print(z)    

#4. Prime Number
# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Integer is Prime")
# else:
#     print("Not prime")            

# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Integer is Prime")
# else:
#     print("Not prime")          

# n=int(input("Enter Number:")) 
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Entered integer is Prime")
# else:
#     print("Not prime")             

# l="Sky is Blue"
# final=(l.split()[::-1])
# print(" ".join(l))

# l="Sky is Blue"
# final=(l.split()[::-1])
# print(" ".join(l))          

#1.
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The reversed integers are:",rev)    

#2.
# n=int(input("Enter Number:"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reversed Integers are:",rev)
# if num==rev:
#     print("The Entered Integer is Palindrome")
# else:
#     print("Please.. Enter Valid Palindrome i.e., 121 or 545")        

#3.
# n=int(input("Enter Number:"))
# i=1
# count=0
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Integer is Prime")
# else:
#     print("Please.. Enter Valid Prime Number i.e., 2,3,5,7,11,13")            

#4.
# n=int(input("Enter Number:"))
# sum=0
# num=n
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==num:
#     print("The Entered Integer is Perfect Number")
# else:
#     print("Please.. Enter Valid Perfect Integer i.e., 6 or 28")            

#5.
# n=int(input("Enter Number:"))
# for i in range(1,n):
#     num=i
#     i=str(i)
#     n=len(str(i))
#     sum=0
#     for j in i:
#         sum+=int(j)**n
#         if num==sum:
#             print(num)

#6.
# x,y,z=0,1,0
# n=int(input("Enter Number:"))
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print(z)

#7.
# l="Ravi is Dark"
# print(l)
# final=(l.split()[::-1])
# print(" ".join(final))

#8.
# l="Python is Best"
# print(l[::-1])

#9.
# l=[1,2,3,4,1,2,3,5,6]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print("List Before Duplicates Removal:",l)
# print("List After duplicates removal:",l1)        

#10.
# l=[1,2,3,1,2,3,4,5]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("List Before Duplicates Removal:",l)
# print("List After Duplicates removal:",l1)            

#11. o/p = [4,5]
# l=[1,2,3,1,2,3,4,5]
# print([i for i in l if l.count(i)==1])

# n=int(input("Enter Number:"))
# i=1
# sum=0
# while n>=i:
#     sum+=i
#     i+=1
# print("Sum is :",sum)
    
#13.
# n=int(input("Enter Number:"))
# even_sum=odd_sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("The Sum of Even Number is:",even_sum)
# print("The Sum of Odd Number is",odd_sum)            
    
# n=int(input("Enter Number:"))
# fact=1
# i=1
# while n>=i:
#     fact*=i
#     i+=1
# print("factorial iS:",fact)    

# celcius=int(input("Enter Number:"))
# far=(celcius*1.8)+32
# print("convertinng {0} into {1}".format(celcius,far))

#1.
# n=int(input("Enter Number:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The Reversed Integers are:",rev)    

# n=int(input("Enter Number:"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("The Reversed Integers are:",rev)
# if num==rev:
#     print("The Entered Integer is Palindrome")
# else:
#     print("Please... Enter Valid Palindrome i.e., 121 or 545 !!")        

# n=int(input("Enter Number:"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("The Entered Integer is Prime Number")
# else:
#     print("Please.. Enter Valid Prime Number i.e., 2,3,5,7,11,13 !!")            

# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("The Entered Integer is Perfect Number")
# else:
#     print("Please.. Enter Valid Perfect Integer e.g., 6 or 28!!")    

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

# n=int(input("Enter Number:"))
# x,y,z=0,1,0
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print(z)    

#i/p = "boAt is a company"
#o/p = "company a is boAt"
# l="boAt is a company"
# print((" ".join(l.split()[::-1])))

# l="company of strings"
# print(l[::-1])

# l=[1,1,2,2,3,3,5,5,4]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l)
# print(sorted(l1))        

# l=[1,1,2,2,3,3,4,4,5,6,7,7]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("List Elements before duplicates removal:",l)
# print("List Elements after duplicates removal:",l1)             

# l=[1,2,1,2,3,3,4,5,4,6]
# print(l)
# print([x for x in l if l.count(x)==1])

# l="A1S2D3F4G5H6J7K8L9"
# alpha=[]
# nums=[]
# for i in l:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         nums.append(i)
# final=(sorted(alpha)+sorted(nums))
# print(" ".join(final))               

# n=int(input("Enter Number:"))
# i=1
# sum=0
# while n>=i:
#     sum+=i
#     i+=1
# print("The Sum of Given Integer is:",sum)        

# n=int(input("Enter Number:"))
# i=1
# even_sum=odd_sum=0
# while n>=i:
#     if n%i==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("The Sum of Even Integers is:",even_sum)
# print("The Sum of Odd Integers is:",odd_sum)            

# fact=1
# i=1
# n=int(input("Enter Number:"))
# while n>=i:
#     fact*=i
#     i+=1
# print("factorial of the given integer is:",fact)    

# celcius=int(input("Enter celcius degree:"))
# far=(celcius*1.8)+32
# print("%.2f of celcius degree is equal to %.2f of farhenheit"%(celcius,far))

# PI=3.142
# r=int(input("Enter Radius of the Circle:"))
# area=2*r*r
# circumference=2*PI*area
# print("Area of Circle is:",area)
# print("Circumference of the Circle is:",circumference)




