#List Methods
#Returns the count of the required value in the list
#list_name.count(value)

# list=[1,2,3,3,3,5,6,4,5,3]
# l2=list.count(3)
# print(l2)

# list=[2,3,3,4,4,5,5,5,5,5,5,5,6,7,8,9]
# l1=list.count(5)
# print(l1)

#Index():
#Index of the value in the list is returned
#list_name.index(value)

# list=[1,2,3,4,5,6]
# l1=list.index(3)
# print(l1)

#pop
#removes the value according to the given index number. if index is not given then the argument is considered to be '-1' in default(i.e, the element in the end of list is removed)
#list_name.pop(index)
# list=[1,2,3,4,5]
# l1=list.pop(3)
# print(l1)

# list=[1,2,3,4,5,6,7]
# l1=list.pop(4)
# print(l1)

# list=[1,2,3,4,5,6,7,8,9]
# l1=list.pop(7)
# print(l1)

# list=[1,2,'ravi','kant',5,6,7,8]
# l1=list.pop(2)
# print(l1)
# print(list)

# list=[1,2,3,4,5]
# l1=list.extend([6,7,8])
# print(list)

list=[1,2,3]
l1=list.extend([4,5])
print(list)