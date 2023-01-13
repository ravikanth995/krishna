# def test():
#     # print("Test")
#     i=7
#     l=6
#     while i<l:
#         break
#     if i<l:
#         print("Yes")
#     else:
#         print("No")
# test()                       

# roll_no=13629
# print("Students enrolled for Python is {}".format(roll_no))

# x=[1,2,3,4,5]
# y=x
# print(x)
# print(y)
# y[4]=1
# print("This is y:",x)
# print("This is Y:",y)

# x=[1,2,3,4,5]
# y=x
# print(x)
# print(y)
# y[1]=6
# print("This is X:",x)
# print("This is y:",y)

# x=[1,2,3,4,5]
# y=x
# print(x)
# print(y)
# y[1]=7
# print("This is X:",x)
# print("This is Y:",y)

# x=[1,2,3,4,5,6]
# y=x
# print(x)
# print(y)
# print("This is x:",x)
# print("This is y:",y)

#Shalow Copy
# from copy import copy
# x=[1,2,3,4,5]
# y=copy(x)
# # print("This is X:",x)
# # print("This is y:",y)
# y[4]=9
# print("This is x:",x)
# print("This is y:",y)

# from copy import copy
# x=[1,2,3,4,5]
# y=copy(x)
# print(x)
# print(y)
# print("This is x before changes:",x)
# y[4]=7
# print("-"*30)
# print("This is y after changes:",y)

# from copy import copy
# x=[1,2,3,4,5,6]
# y=copy(x)
# print("X is:",x)
# print("y is:",y)
# y[4]=8
# print("This is x before changes:",x)
# print("-"*30)
# print("This is y after changes:",y)

# from copy import copy
# x=[1,2,3,4,5,6]
# y=copy(x)
# print(x)
# print(y)
# y[2]=0
# print("This is x before changes:",x)
# print("-"*30)
# print("This is Y after changes:",y)

#deep copy
# from copy import copy, deepcopy
# x=[[1,2,3],[4,5,6],[7,8,9]]
# print(x)
# y=copy(x)
# print(y)
# #We will see shallow copy Scenerio
# y[2][2]=111
# print("X value is affected:",x)
# print("-"*30)
# print("This is y affected after:",y)
# z=deepcopy(x)
# z[2][1]=45
# print("deep copied z:",z)
# print("deep copied x is:",x)

from copy import copy, deepcopy
x=[[1,2],[4,5],[6,8]]
print(x)
y=copy(x)
print(y)
y[2][1]=90
print("y after changes:",y)
print("This is x:",x)
z=deepcopy(x)
print("this is z:",z)
z[2][1]=121
print("This is z:",z)
print("this is x:",x)