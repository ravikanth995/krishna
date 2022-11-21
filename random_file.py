import random
l=[]
for i in range(0,20):
    l.append(random.randint(1,90))
    print("list:",l)
    print("Average:", round(sum(l)/len(l),2))
    print("Largest Value in List:", max(l))
    print("Smaller value in List:", min(l))
    l1=sorted(l)
    print("Second Largest value in list:", l1[-2])
    print("Second smallest:", l1[1])
    count=0
    for i in l:
        if i%2==0:
            count+=1
    print("Number of even Numbers in the List:", count)        