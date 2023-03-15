#1. Write a program to print reverse of an given Integer
# n=int(input("Enter Numbern:"))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reverse Integer is:",rev)    

#2. Write a program to print wether a numbers are Palindrome or not
# n=int(input("Enter Number:"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print("Reversed Numbers are:",rev)
# if num==rev:
#     print("Entered Integers are Palindrome")
# else:
#     print("Please.. Enter Valid Palindrome Numbers i.e., 121 or 909 !!")

#3. Write a program to check wether a number is a Prime number or not
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
#     print("Please... Enter Valid Prime Number i.e., 2,3,5,7,9,11 !!")            

#4. Write a program to to check wether an Integer is a Perfect Number or Not
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Entered Integer is a Perfect Number")     
# else:
#     print(("Please.. Enter Valid Perfect Number i.e., 6 or 28 !!!"))    

#5. Write a program to print Armstrong number in the range of 1-407
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

#6. Write a program to print Fibonacci Numbers in the range of 1-9
# n=int(input("Enter Number:"))
# x,y,z=0,1,0
# for i in range(1,n+1):
#     print(z)
#     x,y=y,z
#     z=x+y
# print("Fibonacci Numbers are:",z)    

#7. Write a program to sort the given alphaNumeric with thier respective sort. 
# first Alpha and then numeric values must be printed
# l="T1S2C3O4M5E6I7N8K9H"
# alpha=[]
# num=[]
# for i in l:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         num.append(i)
# final=sorted(alpha)+sorted(num)
# print(" ".join(final))         

#8. Write a program to print remove duplicates
#input= [1,1,2,2,3,4,5]
#output=[1,2,3,4,5]
# l=[1,1,2,2,3,4,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print("List before Duplicates removal:",l)        
# print("List after removal of Duplicate Elements:",l1)        
   
#9. Write a program to removal duplicates 
#input: [1,1,2,2,3,3,4,5,6]
#output=[1,2,3]
# l=[1,1,2,2,3,3,4,5]
# l1=[]
# size=len(l)
# for i in range(size):
#     k=i+1
#     for j in range(k,size):
#         if l[i]==l[j] and l[i] not in l1:
#             l1.append(l[i])
# print("List before elements removal is:",l)
# print("List after elements removal is :",l1)            

#10. Write a program to remove duplicate elements from list
#input: [1,1,2,2,3,4,4,5,6]
#output=[5,6]
# l=[1,1,2,2,3,3,4,4,5,6]
# print("List removal Duplicates removal is:",l)
# print("List after duplicates removal is:",[i for i in l if l.count(i)==1])

#11. Write a python program to reverse a string
#input="Buddha and His Dhamma"
#output="Dhamma His and Buddha"'
# l="Buddha and His Dhamma"
# l1=(l.split()[::-1])
# print("String before reverse is:",l)
# print(" ".join(l1))

#12. Write a program to swap two variables using temp file
# x=int(input("Enter X value:"))
# y=int(input("Enter Y Value:"))
# print("Before X Value Swapp:",x,"\nBefore Y Value Swapp:",y)
# temp=x
# x=y
# y=temp
# print("X Value after Swapping:",x,"\nY Value after Swapping:",y)

#13. Write a python program to swap two varibales without temp variable
# x=int(input("Enter X Value:"))
# y=int(input("Enter Y Value:"))
# print("Before Swapping of X Value:",x,"\nBefore Swapping of Y Value:",y)
# x,y=y,x
# print("After Swapping of X Value:",x,"\nAfter Swapping of Y Value:",y)

#14. Write a python Program to print factorial of a given Number
# n=int(input("Enter Number:"))
# fact=1
# i=1
# while n>=i:
#     fact*=i
#     i+=1
# print("Factorial of a Number is:",fact)    

#Write a program to find sum of all even and odd number upto specified number
# n=int(input("Enter Number:"))
# i=1
# odd_sum=even_sum=0
# while n>=i:
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("Sum of all Odd Numbers are:",odd_sum)
# print("Sum of all Even Number are:",even_sum)            

# n=int(input("Enter Number:"))
# i=1
# sum=0
# while i<=n:
#        sum+=i
#        i+=1
#        print("Sum of Numbers are:",sum)        

# n=int(input("Enter Number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("Sum of Number is:",sum)    

# n=int(input("Enter Number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("The Sum of Specified number is:",sum)    

# n=int(input("Enter Number:"))
# odd_sum=even_sum=0
# i=1
# while i<=n:
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("Sum of Even Number:",even_sum)
# print("Sum of Odd Number:",odd_sum)            


