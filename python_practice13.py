# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
# max_zero=0
# count=0
# for i in range(len(l)):
#     if(l[i]==0):
#         count=count+1
#         if(i==len(l)-1):
#             if(count>max_zero):
#                 max_zero=count
#     if(l[i]==1):
#         if(count>max_zero):
#             max_zero=count
#         count=0
# print("Longest run of Zeroes in a row is:", max_zero)            

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_zero):
#                     max_zero=count
#             if(l[i]==1):
#                 if(count>max_zero):
#                     max_zero=count
#                 count=0
# print("Longest run of zeroes in a row is:", max_zero)

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_zero):
#                     max_zero=count
#             if(l[i]==1):
#                 if(count>max_zero):
#                     max_zero=count
#                 count=0
# print("Longest Run of Zeroes in a Row:", max_zero)      

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_zero):
#                     max_zero=count
#             if(count>max_zero):
#                 max_zero=count
#             count=0

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(max_zero>count):
#                     max_zero=count
#             if(count>max_zero):
#                 max_zero=count
#             count=0            

# print("Longest run of zeroes in the row is :", max_zero)

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if((l[i])==0):
#             count=count+1
#             if(i==len(l)-1):
#                 max_zero=count
#         if(count>max_zero):
#             max_zero=count
#             count=0
# print("Longest run of zeroes in the row", max_zero)            

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_count=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 max_count=count
#         if(count>max_count):
#             max_count=count
#             count=0
# print("Longest run of zeroes inn the row is:",max_count)                    

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_count=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_count):
#                   max_count=0
#                   count=0
#         if(l[i]==1):        
#             if(count>max_count):
#                 max_count=count
#             count=0    

# print("Longest run of zeroes in the row:", max_count)                

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_count=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_count):
#                   max_count=0
#                   count=0
#         if(l[i]==1):
#             if(count>max_count):
#                 max_count=count
#             count=0
# print("Longest run of the zeroes in the row:",max_count)

# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(0,1))
#     max_zero=0
#     count=0
#     for i in range(len(l)):
#         if(l[i]==0):
#             count=count+1
#             if(i==len(l)-1):
#                 if(count>max_zero):
#                   max_zero=0
#                   count=0
#         if(i==len(l)-1):
#             if(count>max_zero):
#               max_zero=count
#             count=0
# print("Longest run of the zeroes of the row:", max_zero)                    

import random
l=[]
for i in range(100):
    l.append(random.randint(0,1))
    max_count=0
    count=0
    for i in range(len(l)):
        if(l[i]==0):
            count=count+1
            if(i==len(l)):
                if(count>max_count):
                    max_count=count
                    count=0
            if(i==len(l)-1):
                if(count>max_count):
                    max_count=count
                    count=0
print("Longest zeroes of the row is:", max_count)                            







