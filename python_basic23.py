def count(str1):
    a={}
    for n in str1:
        keys=a.keys()
        if n in keys:
            a[n]+=1
        else:
            a[n]=1
    print(a)
count("Speed")                