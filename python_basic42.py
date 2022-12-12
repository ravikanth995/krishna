#Using Mathematical operations for List Objects
#1. Concatenation Operator := (+)
#We can use '+' for concatenation 2 lists into a single list
# x=[10,20,30]
# y=[40,50,60]
# z=x+y
# print(z)

# x=[1,3,5,7]
# y=[2,4,6]
# z=x+y
# print(z)

# x.append(2)
# y.append(1)

# x.insert(1,2)
# y.insert(0,1)

# print(x)
# print(y)

# x.extend([1,2,3,4])
# y.extend([2,3,4,5])
# print(x)
# print(y)


# x=[1,2,3]
# z=x*3
# print(z)

# x=[1,2,3]
# z=x*2
# print(z)

# x=[0,1,2]
# z=x*5
# print(z)

#Comparison List Objects
# x=[1,2,3]
# y=[1,2,3]
# z=[2,3,1]
# print(x==y)
# print(x==z)
# print(x!=z)

# x=[1,2,3]
# y=[1,2,3]
# z=[2,3,1]
# print(x==y)
# print(x==z)
# print(x!=z)

# x=['a','b','c']
# y=['a','b','c']
# z=['A','B','C']
# print(x==y)
# print(x==z)
# print(x!=y)
# print(x!=z)

#Ralational Operator
#Whenever we are using relational operator [<,<=,>,>=] between list objects, then only first element comparison will be performed.
# x=['a','b','c']
# y=['a','b','c']
# z=['A','B','C']
# print(x>y)
# print(x>=z)
# print(x<z)
# print(z<x)

#Membership Operators
#1. in

# x=['a','b','c']
# print('a' in x)
# print('d' in x)
# print('b' in x)
# print('c' in x)

# #2. not in
# x=['a','b','c']
# print('a' not in x)
# print('d' not in x)
# print('c' not in x)
# print('f' not in x)

#Nested Lists
# #List inside 7the another list is called Nested List
# a=[10,20,[30,40]]
# print(a)
# print(a[0])
# print(a[2])
# print(a[2][0])
# print(a[2][1])


# a=[1,2,[30,39,40]]
# print(a[2][0])
# print(a[2][1])
# print(a[2][2])

# a=[1,2,[23,34,26]]
# print(a[2][0])
# print(a[2][1])
# print(a[2][2])

# a=[2,1,0,2,[5,6,7,0]]
# print(a[4][3])

# a=[1,2,[3,4,5]]
# print(a[2][2])

# a=[8,6,[3,2,1,6,4]]
# print(a[2][2])
# print(a[2][3])
# print(a[2][4])

#we represent matrix by using nested lists
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     print(i)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     print(i)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     print(i)

# a=[[7,4,8],[2,5,3],[9,0,4]]
# for i in a:
#     print(i)

# a=[[1,3,2],[4,7,4],[5,9,1]]
# for i in a:
#     print(i)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=" ")
#     print()    

# a=[1,2,3],[4,5,6],[7,8,9]
# for i in a:
#     print(i)
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()   

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print((a[i][j]),end=" ")
#         print()    

# a=[[1,2,3],[4,5,6],[5,4,3]]
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()

# a=[[0,1,2],[4,5,6],[5,6,3]]  Its Highlight. 
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i],[j],end=" ")
#         print() 

# a=[[2,4,1],[5,7,1],[0,8,6]]
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()    

# a=[[0,7,4],[3,6,1],[0,5,1]]
# for i in a:
#     print(i)
    
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()    

# a=[[2,3,4],[8,1,5],[8,5,1]]
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()    

# a=[[0,1,3],[4,6,1],[5,7,1]]
# for i in a:
#     print(i)

#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()          

a=[[0,1,2],[5,1,2],[0,5,2]]
for i in a:
    print(i)

    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=" ")
        print()    