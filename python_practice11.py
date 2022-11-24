import random
l=[]
for i in range(20):
    l.append(random.randint(1,100))
    print("list:",l)
    print("Average:", round(sum(l)/len(l),2))
    print("Largest value in List:", max(l))
    print("Samllest Value in List:", min(l))
    l1=sorted(l)
    print("Second Largest Value in List:", l1[1])
    print("Second Samllest Value in List:", l1[1])
    count=0
    for i in l:
        if i%2==0:
            count+=1
    print("Number of Even Number in the List:", count)        