# def first_diff(s1,s2):
#     if s1==s2:
#         return -1
#     else:
#         if len(s1)==len(s2):
#             for i in range(len(s1)):
#                 if s1[i]!=s2[i]:
#                     return (i+1)

#         else:
#             if len(s1)<len(s2):
#                 i=0
#                 flag=0
#                 while (i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return
#                     i=i+1
#                 if(flag==0):
#                     return(i+1)
#             else:
#                 i=0
#                 flag=0
#                 while (i<len(s2)):
#                     if s2[i]!=s1[i]:
#                         flag=1
#                         return(i+1)
#                     i=i+1
#                 if(flag==0):
#                     return (i+1)
# s1=input("Enter String 1:") 
# s2=input("Enter String 2:")
# x=first_diff(s1,s2)
# if(x==-1):
#     print("Strings are identical")
# else:
#     print("First difference occurs at location:",x)                          

# def first_diff(s1,s2):
#     if s1==s2:
#       return -1
#     else:
#         if len(s1)==len(s2):
#             for i in range(len(s1)):
#                 if s1[i]!=s2[i]:
#                     return (i+1)
#         else:
#             if len(s1)<len(s2):
#                 i=0
#                 flag=0
#                 while (i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return (i+1)
#                     i=i+1 
#                 if(flag==0):
#                     return(i+1)
#             else:
#                 i=0
#                 flag=0
#                 while (i<len(s2)):
#                     if s2[i]!=s1[i]:
#                         flag=1
#                         return(i+1)
#                     i=i+1
#                 if(flag==0):
#                     return(i+1)
# s1=input("Enter First String:")
# s2=input("Enter Second String:")
# x=first_diff(s1,s2)
# if(x==-1):
#     print("Strings are identical:")
# else:
#     print("Strings are not identical at:",x)                                

# def first_diff(s1,s2):
#     if s1==s2:
#         return -1
#     else:
#         if len(s1)==len(s2):
#             for i in range(len(s1)):
#                 if s1[i]!=s2[i]:
#                     return (i+1)
#         else:
#             if(len(s1)<len(s2)):
#                 i=0
#                 flag=0
#                 while (i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return(i+1)
#                     i=i+1
#                     if(flag==0):
#                         return(i+1)
#             else:
#                 i=0
#                 flag=1
#                 while(i<len(s2)):
#                     if(s1[i]!=s2[i]):
#                         flag=1
#                         return(i+1)
#                     i=(i+1)
#                 if(flag==0):
#                     return(i+1)
# s1=input("Enter First String:")
# s2=input("Enter Second String:")
# x=first_diff(s1,s2) 
# if(x==-1):
#     print("Strings are identical:") 
# else:
#     print("First difference occurs at location:",x)                      

# def first_diff(s1,s2):
#     if s1==s2:
#         return -1
#     else:
#         if(len(s1)==len(s2)):
#             for i in range(len(s1)):
#                 if s1[i]!=s2[i]:
#                     return(i+1)
#         else:
#             if(len(s1)<len(s2)):
#                 i=0
#                 flag=0
#                 while (i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return(i+1)
#                     i=i+1
#                 if(flag==0):
#                     return(i+1)
#             else:
#                 i=0
#                 flag=0
#                 while (i<len(s2)):
#                     if s2[i]!=s1[i]:
#                         flag=1
#                         return(i+1)
#                     i=i+1
#                 if(flag==0):
#                     return(i+1)
# s1=input("Enter First String:")
# s2=input("Enter Second Strinng:") 
# x=first_diff(s1,s2)
# if(x==-1):
#     print("Strings are identical:") 
# else:
#     print("First Difference at location:",x)                      

# def first_class(s1,s2):
#     if s1==s2:
#         return -1
#         if (len(s1)==len(s2)):
#             for i in range(len(s1)):
#                 if s1[i]!=s2[i]:
#                     return i+1
#         else:
#             if(len(s1)<len(s2)) :
#                 i=0
#                 flag=0
#                 while (i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return i+1
#                     i=i+1
#                 if (flag==0):
#                     return i+1
#             else:
#                 i=0
#                 flag=0
#                 while (i<len(s2)):
#                     if s2[i]!=s1[i]:
#                         flag=1
#                         return i+1
#                     i=i+1
#                 if (flag==0):
#                     return i+1
# s1=input("Enter String 1:")
# s2=input("Enter String 2:")
# x=first_class(s1,s2)
# if(x==-1):
#     print("Strings are identical:")
# else:
#     print("First difference occurs at location:",x)

# def first_diff(s1,s2):
#     if(s1==s2):
#         return -1
#     else:
#         if(len(s1)==len(s2)):
#             for i in range(len(s1)):
#                if s1[i]!=s2[i]:
#                 return (i+1)
#         else:
#             if(len(s1)<len(s2)):
#                 i=0
#                 flag=0
#                 while(i<len(s1)):
#                     if s1[i]!=s2[i]:
#                         flag=1
#                         return (i+1)
#                     i=i+1
#                 if(flag==0):
#                     return(i+1)
#             else:
#                 i=0
#                 flag=0
#                 while(i<len(s2)):
#                     if s2[i]!=s2[i]:
#                         flag=1
#                         return(i+1)
#                     i=i=1
#                 if(flag==0):
#                     return(i+1) 
# s1=input("Enter String 1:")
# s2=input("Enter String 2:") 
# x=first_diff(s1,s2)
# if(x==-1):
#     print("Strings are identical:")
# else:
#     print("First difference is at:", x)                          

def first_diff(s1,s2):
    if(s1==s2):
        return -1
    else:
        if(len(s1)==len(s2)):
            for i in range(len(s1)):
                if(s1[i]!=s2[i]):
                    return (i+1)
        else:
            if(len(s1)<len(s2)):
                i=0
                flag=0
                while (i<len(s1)):
                    if s1[i]!=s2[i]:
                        flag=1
                        return(i+1)
                    i=i+1
                    if(flag==0):
                      return(i+1)
                else:
                    i=0
                    flag=0
                    while (i<len(s2)):
                        if s2[i]!=s1[i]:
                            flag=1
                            return(i+1)
                        i=i+1
                    if(flag==0):
                        return (i+1)
s1=input("Enter String 1:")
s2=input("Enter String 2:")
x=first_diff(s1,s2)
if(x==-1):
    print("Strings are identical:") 
else:
    print("First difference at loction:",x)                               
                                           
                        





