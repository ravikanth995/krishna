#Command Line Argument
# import sys
# m=sys.argv
# n=len(sys.argv)
# print("Total Argument Passed",n)
# print(m)
# print("\nName of Python Script",sys.argv[0])
# print("\nArgument Passed:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# print("\n\n") 
# print(sys.argv[i])
# print(int(sys.argv[1]+int(sys.argv[2])+int(sys.argv[3])))
# a=sys.argv[1] 
# b=sys.argv[2] 
# c=sys.argv[3] 
# print(a,b,c)
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nResult:",sum)    


 
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)