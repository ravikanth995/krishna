
num=input("Enter Algebric Expression")
l=list(num)
result=" "
i=0
while (i<len(l)):
    if l[i]=='(':
        index=l.index(')')
        s2=" ".join(l[i:index+1])
        result=result+'*'+s2
        i=i+len(s2)
    elif l[i].isalpha():
        result=result+'*'+[i]
        i=i+1
    else:
        result=result+l[i]
        i=i+1
        print(result)       
