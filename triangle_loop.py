num=int(input("Enter the height of the traingle"))
for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print()    