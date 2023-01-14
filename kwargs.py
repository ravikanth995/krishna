# def display(name, age=18):
#     print(name)
#     print(age)
# display(name="Ravi")   

# def display(name, age):
#        print(name)
#        print(age)
# display(name='ravi', age=37)           

# def display(name="ravi", age=19):
#     print(name)
#     print(age)
# display(name="kanth", age=47)  

# def arbKWargs(*details):
#     for i in details :
#         print(i)
# arbKWargs("ravi","kanth","chavan","buddha")   

# def arbKwargs(*a):
#     for i in a:
#         print(i)
# arbKwargs("Gautam","Buddha","My","Hero")              

# def arbKwargs(*q):
#     for i in q:
#         print(i)
# arbKwargs("Siddhart","gautam","Budhha","Is","My","Hero")         

# def arbKwargs(*a):
#     for i in a:
#         print(i)
# arbKwargs("Ravi","Kanth","Chavan","Shigra","anhg")        

# def arbKwargs(*a):
#     for i in a:
#         print(i)
# arbKwargs("Rare","Single","Shruti","Upanishad","IsaVasya","KathaUpanishad","kena","Mandukya","taittariya")        

# def argKwargs(*folks):
#     for i in folks:
#         print(i)
#         print(folks[2])
# argKwargs("Ravi","Kanth","chavan","Kings","queens") 
# argKwargs("Ashtakam","Zindagi","Apmaam") 

# def ord(name,*items):
#     print("items purchases by Customer:",name)
#     for i in items:
#         print("\t\t",i)
# name="Ravikanth"        
# items=['1','2','3','4','5']
# ord(name,*items)

# def orders(name,*items):
#     print("Items purchased by Customer is:",name)
#     for i in items:
#         print("\t\t",i)
# name="Ravikanth"
# items=["Suzuki","Maruti","Tata","Marcedez","Mahindra"]        
# orders(name,*items)

# def argsKwargs(name,*items):
#     print("Items Purchased by the Customer are:",name)
#     for i in items:
#       print("\t\t",i)
# name="Ravikanth"
# items=["Milk","Books","Curd","Tv","Mobile"]
# argsKwargs(name,*items)      

# def argsKwargs(name,*items):
#     print("The Items Purchased by the Customer:",name)
#     for i in items:
#         print("\t\t",i)
# name="Ravikanth"
# items=["Cloths","Shirts","trousers","Underwear","Brush"]
# argsKwargs(name,*items)        

# def argsKwargs(name,*items):
#     print("Items Purchased by the Customer:",name)
#     for i in items:
#         print("\t\t",i)
# name="Ravikanth"
# items=["iPhone","SamSung","Nokia","Motorola"]
# argsKwargs(name,*items)        

# def display(name,*args,**kwargs):
#     print(name)
#     for i in args:
#         for key, values in kwargs.items():
#             print(f"{key} is a {values}")
# name="class"
# items=["Phone","Cooling","Magnet","Sneeking"]
# d={"praveen":"Instrucor","Ravi":"Student"} 
# display(name,*items,**d)         

# def  myfun(**kwargs):
#     for key, values in kwargs.items():
#         print("%s:%s"%(key, values))
# myfun(First="Hello", Mid="Good", Last="Morning")        

# def fun(**kwargs):
#     for key, values in kwargs.items():
#         print("%s==%s"%(key, values))
# fun(first="Dhammapada", Mid="Gautam", Last="Buddha")

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s==%s"%(key, value))
# myFun(Buddha="Dhammpada", Krishna="Bhagvat geeta",Nanak="GranthSahib")        

# def myFun(**kawrgs):
#     for key, values in kawrgs.items():
#         print("%s==%s"%(key, values))
# myFun(Buddha="Dhammapada", krishna="geeta", Advait="vedant")        

# def myFun(**kwargs):
#     for keys, values in kwargs.items():
#         print("%s==%s"%(keys, values))
# myFun(First="Education", Mid="Job", Last="Salvation")

# def myFunn(*arg,**item):
#         print(arg)
#         print(item)
# myFunn(First="hello", Mid="Chiit", Last="Chnachal")    

# def myFun(*args, **items):
#     print(args)
#     print(items)
# myFun(First="Prakriti", Mid="Suffering", Last="Mukti")    

# def myFun(*args, **kwargs):
#     print(args)
#     print(kwargs)
# myFun(First="Buddha", Mid="Upanishad", Last="Ashtavkra geeta")    

# def myFun(args1, args2, args3):
#     print("args1 :", args1)
#     print("args2:", args2)
#     print("args3:",args3)
# args=("Hello","Python","World")
# myFun(*args)
# kwargs={"args1":"Hello", "args2":"Python", "args3":"World"}
# myFun(**kwargs)    

# def myFun(args1,args2,args3):
#     print("args1=",args1)
#     print("args2=",args2)
#     print("args3=",args3)
# args=("hello","Python","World")
# myFun(*args)
# print("-"*40)
# kwargs={"args1":"Hello", "args2":"Python", "args3":"World"}
# myFun(**kwargs)   

# def myFun(*args, **kwargs):
#     print("*args:",args)
#     print("**kwargs:",kwargs)
# myFun("Hello","Python","World", First="Hello", Mid="Python", Last="World")    

# def myFun(*args, **kwargs):
#     print("args:",args)
#     print("kwargs:",kwargs)
# myFun("Hello","Python","World", First="hello", mid="Python", last="World")    

# def myFun(*args,**kwargs):
#     print("args",args)
#     print("kwargs",kwargs)

# myFun("Hello", "Python", "World", First="Hello", Mid="Python", last="world")    

# def display(name,*args,**kwargs):
    
#     for i in args:
#         print(i)
#     for key, value in kwargs.items():
#         print(f"{key} is a {value}") 
# name="Class"           
# item=["Phone","Cool","Maggie","Sneak"]
# d={"Praveen":"Tutor", "Ravikanth":"Student", "Shagun":"Student2"}
# display(name,*item, **d)

# def display(name, *args, **kwargs):
#     for i in args:
#         print(i)
#         for keys,values in kwargs.items():
#             print(f"{keys} is a {values}")
# name="Ravikanth"
# item=["Xiome","SamSung","Apple","Orange","msutatrd"]
# d={"praveen":"tutor","ravikanth":"student",}
# display(name,*item,**d)

# def display(name,*args,**kwargs):
#     for i in args:
#         print(i)
#         for keys,values in kwargs.items():
#             print(f"{keys} in a {values}")
# name="Ravikanth"
# item=["Arijit Singh", "KK", "Sonu Nigam", "Shaan"]
# d={"Moto":"Archadea","Himesh":"Suroor","KK":"Ajjab se"}            
# display(name,*item,**d)

def display(name,*args,**kwargs):
    for i in args:
        print(i)
        for key,values in kwargs.items():
            print(f"{key} is a {values}")
name="RaviKanth"
item=["Isro","Nasa","Jaxa","Europa"]
d={"Chandrayaan":"isro","NASA":"Apollo","Jaxa":"idk"}
display(name,*item,**d)