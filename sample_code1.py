
list1=[10,20,30,20,10,40,50,30]
size=len(list1)
new_list=[]
for i in range(size):
    k=i+1
    for j in range(k,size):
        if list1[i]==list1[j] and list1[i] not in new_list:
            new_list.append(list1[i])
print(new_list)        