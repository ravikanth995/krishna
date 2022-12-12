# l=[]
# for i in range(1,11):
#     l.append(i **2)
# print("Output:",l)
# print(type(l))    

# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print(l)
    
# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print("Squares are:",l)       

# l=[]
# for  i in range(1,11):
#     l.append(i**2)
# print("Square are:",l)    

# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print("Square are:",l)    

# l=[]
# for i in range(1,12):
#     l.append(i**2)
# print("Square is:",l)    

# l=[]
# for i in range(1,13):
#     l.append(i**2)
# print("Output is:",l)    

# l=[]
# for i in range(1,15):
#     l.append(i**2)
# print(l)    

# l=[]
# for i in range(1,13):
#     l.append(i**2)
# print("output is:",l)    

# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print("Square is:",l)    

# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print("Squares are:",l)    


#Tuple 
# tpl=()
# print(tpl)

# tpl=100,200,300
# print(tpl)

# tpl=(10)
# print(type(tpl)) it will consider it as a int not tuple

# tpl=(10,)
# print(type(tpl)) 

# lst=[1,2,3,4]
# lst=tuple(lst)
# print(lst)

# tpl=tuple(range(100,120,2))
# print(tpl)

# tpl=tuple(range(100,120,5))
# print(tpl)

# tpl=tuple(range(100,150,10))
# print(tpl)

# tpl=tuple(range(100,190,10))
# print(tpl)

# tpl=tuple(range(100,130,5))
# print(tpl)

# tpl=tuple(range(1,20,2))
# print(tpl)

# tpl=tuple(range(1,10,1))
# print(tpl)

# lst=list(range(1,10,1))
# print(lst)

#Accessing elements of tuples
# tpl=('a','b','c','f')
# print(tpl[0])
# print(tpl[1])

# tpl=('a','b','c','d','e')
# print(tpl[1])
# print(tpl[2])

# tpl=(1,2,3,4)
# for i in tpl:
#     print(i)

# tpl=(1,2,3,4,5)
# for i in tpl:
#     print(i)

# tpl=('a',1,2.2,3)
# for i in tpl:
#     print(i)

# tpl=('Ravi',[1,2,3],('jeele',2))
# # for i in tpl:
# print(tpl[1][2])
# print(tpl[2][0])

# tpl=('prashant',[1,2,3],(8,6,3))
# print(tpl[0])
# print(tpl[1][2])
# print(tpl[1][2])

# #Negative Slicing
# tpl=('p','y','t','h','o','n')
# print(tpl[::-1])
# print(tpl[-2])    

# tpl=('p','y','t','h','o','n')
# print(tpl[2])
# print(tpl[-3])

# tpl=('a','b','c','d','e','d')
# print(tpl[-2])
# print(tpl[-3])

#Accessing tuple elements using slicing
# tpl=(1,2,3,4,5,6)
# print(tpl[1:4])

# tpl=(1,2,3,4,5)
# print(tpl[1:4])
# print(tpl[:-4])
# # print(tpl[:-2])
# print(tpl[:-3])
# print(tpl[:-4])

#Tuple is Im-mutable

#Mathematical operators for tuple
#We can use + and * operators for tuple
# tpl=(10,20,30)
# print(tpl+tpl)
# print(tpl*2)

# tpl=(10,20,40)
# print(tpl*2)
# print(tpl+tpl)

# #Tuple Packing and Unpacking
# a=10
# b=2.2
# c='hello'
# d=1+5j
# e=True
# tpl=(a,b,c,d,e)
# print(tpl)

# tpl=10,2.2,'hello',1+5j,True
# a,b,c,d,e=tpl
# print('a=',a, 'b=',b, 'c=',c, 'd=',d, 'e=',e)

# a=2
# b='r'
# c=1+5j
# d=True
# e=2.4
# tpl=(a,b,c,d,e)
# print(tpl)

# tpl=2,'r',1+5j,True,2.4
# a,b,c,d,e=tpl
# print('a=',a, 'b=',b, 'c=',c, 'd=',d,'e=',e)

# a=1
# b=2.2
# c=1+5j
# d='ravi'
# e=True
# f=False
# g=None
# tpl=(a,b,c,d,e,f,g)
# print(tpl)
# tpl=1,2.2,1+5j,'ravi',True,False,None
# a,b,c,d,e,f,g=tpl
# print('a=',a, 'b=',b, 'c=',c, 'd=',d, 'e=',e, 'f=',f, 'g=',g)

# a=1
# b=2.1
# c=1+5j
# d='r'
# e=True
# tpl=(a,b,c,d,e)
# print(tpl)

# tpl=1,1.1,1+5j,'r',True
# print('a=',a,'b=',b,'c=',c,'d=',d,'e=',e)

#We are packing variables in tuple paranthesis
# a=1
# b=1.1
# c=1+5j
# d='a'
# e=True
# tpl=(a,b,c,d,e)
# print(tpl)

# #Now, we are Unpacking tuple
# tpl=1,1.1,1+5j,'a',True
# print(a,b,c,d,e)

#Tuple Comprehension
# tpl=(x*2 for x in range(1,5))
# for x in tpl:
#     print(x)

tpl=(x*2 for x in range(1,5))
for x in tpl:
    print(x)
