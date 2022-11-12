import sys
m=sys.argv
n=len(sys.argv)
print("Total Argument passed", n)
print(m)
print("\n Name of Python Script", sys.argv)

print("\n Argument passed:", end="")
for i in range(1,n):
    print(sys.argv[i], end="")
    print("\n\n")
    print(sys.argv)
    print(int(sys.argv[i])+int(sys.argv[2])+int(sys.argv[3]))
    

    a=sys.argv[1]
    b=sys.argv[2]
    c=sys.argv[3]

    print(a,b,c)
    sum=0
    for i in range(1,n):
        sum+=int(sys.argv[i])
        print("\n\n result:", sum)