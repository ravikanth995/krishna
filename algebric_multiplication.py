alexpre=input("Enter a algebric expression")
l=list(alexpre)
result=""
i=0
while(i<len(l)):
    if[i]=='(':
        index=l.index(')')
        s2=".join(i[i:index+1]"
        result=result+'*'+s2
        i=i+len(s2)
    elif l[i].isalpha():
        result=result+'*'+[i]
        i=i+1
    else:
        result=result+[i]
        i=i+1
        print(result)    