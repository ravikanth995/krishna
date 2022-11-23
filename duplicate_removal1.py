num=list(map(int, input("Enter the elements into list with duplicates:").split(',')))
s=[]
for i in num:
    if i not in s:
        s.append(i)
print(s)



