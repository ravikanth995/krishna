# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and col>0 and col<5):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()          

# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and col>0 and col<5):
#             print("*",end=" ")
#         else:
#             print(end=" ")    
#     print()        

# for row in range(6):
#     for col in range(9):
#         if col==0 or col==5 or (row==col and col>0 and col<5):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()            

# for row in range(6):
#     for col in range(7):
#         if col==0 or col==5 or (row==col and col>0 and col<5):
#             print("*",end=" ")
#         else:    
#             print(end=" ")
#     print()        
# This is The actual Star * shaped N
for row in range(6):
    for col in range(7):
        if col==0 or col==5 or (col==row and col>0 and col<5):
            print(end="*")
        else:
            print(end=" ")
    print()            
