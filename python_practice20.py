# def merge(s1,s2):
#     s=s1+s2
#     s.sort()
#     return s
# a=list(map(int, input("Enter Sorted List 1:").split()))
# b=list(map(int, input("Enter Sorted List 2:").split()))
# x=merge(a,b) 
# print("Sorted List After Merging:",x)       

# def merge(s1,s2):
#     s=s1+s2
#     s.sort()
#     return s
# a=list(map(int,input("Enter Sorted LIst 1:").split()))
# b=list(map(int, input("Enter Sorted List 2:").split()))
# x=merge(a,b) 
# print("Sorted List After Merging",x)   

# def merge(s1,s2):
#     s=s1+s2
#     s.sort()
#     return s
# a=list(map(int, input("Enter List Item 1:").split()))
# b=list(map(int, input("Enter List Items 2:").split()))
# x=merge(a,b)
# print("Sorted List after merging:",x)    

# def merge(s1,s2):
#     s=s1+s2
#     s.sort()
#     return s
# a=list(map(int,input("Enter Sorted List 1:").split()))
# b=list(map(int,input("Enter Sorted List 2:").split()))
# x=merge(a,b)
# print("List After Sorted:",x)    

def merge(s1,s2):
    s=s1+s2
    s.sort()
    return s
a=list(map(int, input("Enter List 1:").split()))
b=list(map(int, input("Enter List 2:").split()))
x=merge(a,b) 
print("Sorted after:",x)   