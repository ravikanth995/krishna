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

def display(name,*args,**kwargs):
    print(name)
    for i in args:
        for key, values in kwargs.items():
            print(f"{key} is a {values}")
name="class"
args=["Phone","Cooling","Magnet","Sneeking"]
d={"praveen":"Instrucor","Ravi":"Student"} 
display(name,*args,**d)         