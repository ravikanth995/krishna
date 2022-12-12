#Alisasing and Cloning of List Objects
#The Process of giving another reference variable to the existing list 
# x=[10,20,'zero','one']
# y=x
# print("x",id(x))
# print("Y",id(y))

# x=[10,20,'zero','one']
# y=x
# print("x",id(x))
# print("y",id(y))

# y[0]=15
# print(y)
# print(x)

# x=[10,20,40,60]
# y=x[:]
# y[1]=30
# print("Y",y)
# print("x",x)

# x=[1,2,3,'chitt','sayyanm','vairagyam']
# y=x[:]
# y[3]=5
# print("Of x is",x)
# print("Copied y",y)

# x=['mann','kshan','bhangur','chir','kaal']
# y=x.copy()
# y[0]=3
# y[1]=2
# print("X:",x)
# print("Y:",y)

x=['brutrahari','shatakam','Vairagya']
y=x.copy()
y[0]='upanishad'
y[1]='Dhammapada'
print("Before cloning:",x)
print("After Cloning:",y)