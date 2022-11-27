from itertools import permutations
# s=input("Enter a word:")
# for i in range(2,len(s)):
#     for p in permutations(s,i):
#         print(s.join(p),end='')

# s=input("Enter a word:")
# for i in range(2,len(s)):
#     for p in permutations(s,i):
#         print(s.join(p),end="")

# s=input("Enter a Word:")
# for i in range(2,len(s)):
#     for p in permutations(s,i):
#         print(s.join(p),end="")

# s=input("Enter a Word:")
# for i in range(len(s)):
#     for p in permutations(s,i):
#         print(s.join(p),end="")

s=input("Enter a Word:")
for i in range(len(s)):
    for p in permutations(s,i):
        print(s.join(p),end='')