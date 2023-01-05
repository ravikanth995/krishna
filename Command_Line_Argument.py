# import sys
# n=len(sys.argv)
# print("\nTotal Argument passed:",n)
# print("\nName of the Python Script:",sys.argv[0])
# print("\nArgument passed:")
# for i in range(1,n):
#     print(sys.argv[i],end="")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nresult is:",sum)        

# import sys
# n=len(sys.argv)
# print("\nTotal Argument passed",n)
# print("\nName of the Python Script:",sys.argv[0])
# print("\nArgument Passed:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")

# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nResult is:",sum)

# import sys
# n=len(sys.argv)
# print("\nNumber of Argument Passed:",n)
# print("\nName of the Argument:",sys.argv[0])
# print("\nArguments Passed:",end="")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nResult is:",sum)        

# import sys
# n=len(sys.argv)
# print("\nNumber of Arguments Passed:",n)
# print("\nName of the Argument:",sys.argv[0])
# print("\nArguments Passed:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nSum is:",sum) 

import sys
n=len(sys.argv) 
print("\nNumber of Argument Passed:",n)
print("\nName of the Argument is:",sys.argv[0])
print("\nArguments Passed are:",end=" ")
for i in range(1,n):
    print(sys.argv[i],end=" ")
sum=0
for i in range(1,n):
    sum+=int(sys.argv[i])
print("\nResult is:",sum)              