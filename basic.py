# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.current += 1
#         if self.current < self.high:
#             return self.current
#         raise StopIteration

# for elem in Counter(1, 10):
#     print(elem)

# l=[]
# for i in range(3):
#     name=input("Enter Name:")
#     print(l.append(name))
# for i in l:
#     print(i,end=" " )

# num=1111
# reverse1=int(str(num)[::-1])
# if num ==reverse1:
#     print("yes palindrome")
# else:
#     print("no palindrome")    
# def cute(str):
#     l=list(str.split(" "))
#     return l
# str="hi"   
# print(cute(str))

# def num(str):
#     l=list(str.split(" "))
#     return l
# str="raviaknth"
# print(num(str))    

def func(str):
    l=list(str.split(" "))
    return l
str="Ravikanth"
print(func(str))

            
