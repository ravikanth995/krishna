def Prime(num,i):
    count=0
    if num>1:
        for i in range(9):
            if i%num==0:
                # count=count+1
                # if count==2:
                   print(i, "Is  not a Prime Number")
            else:
                    print(num,"is not a prime number")

Prime(21,1)                            
