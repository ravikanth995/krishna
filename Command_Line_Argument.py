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

# import sys
# n=len(sys.argv) 
# print("\nNumber of Argument Passed:",n)
# print("\nName of the Argument is:",sys.argv[0])
# print("\nArguments Passed are:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\nResult is:",sum)    

# import sys
# import os
# n=len(sys.argv)
# print("Nuumber of Argument Passed:",n)
# print("Name of the Argument is:",sys.argv[0])
# print("Argument passed:")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("Sum is:",sum)           

# import sys
# n=len(sys.argv)
# print("\nNumber of Argument Passed:",n) 
# print("\nName of the Argument is:",sys.argv[0])
# print("Argument Passed:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for  i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\nResult is:",sum)     

# import sys
# n=len(sys.argv)
# print("\nNumber of Argument is:",n)
# print("\nName of the Argument is:",sys.argv[0])
# print("\nArguments are:",end=" ") 
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\n\nResult is:",sum)        

# import sys
# n=len(sys.argv)
# print("\nNumber of Arguments are:",n)
# print("\nName of the Argument is:",sys.argv[0])
# print("\nArguments are:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print("\nSum is:",sum)        

import getopt, sys
argumentList=sys.argv[1:]
options="hmo:"
long_options=["Help","my_file","output="]
try:
    argument, values=getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in argument:
        if currentArgument in ("-h","__help"):
           print("Displaying help")
        elif currentArgument in ("-m","__help"):
           print("Displaying file name",sys.argv[0]) 
        elif currentArgument in ("-o","__output"):
           print("Enabling Special Output mode(%s)")%currentValue
except getopt.error as err:
    print(str(err))
