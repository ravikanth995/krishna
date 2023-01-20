# class Cal1:
#     def Sum(self,a,b):
#         return a+b
# class Cal2:
#     def Sub(self,a,b):
#         return a-b
# class Cal3:
#     def Multi(self,a,b):
#         return a*b
# class derived_class(Cal1,Cal2,Cal3):
#     def divide(self,a,b):
#         return a/b
# d=derived_class()
# print(d.Sum(3,4)) 
# print(d.Sub(90,5))
# print(d.Multi(30,5))
# print(d.divide(30,90))                

# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Subtraction(self,a,b):
#         return a-b
# class Calculation3:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived_class(Calculation1,Calculation2,Calculation3):
#     def Divide(self,a,b):
#         return a/b
# Cal=Derived_class()
# print(Cal.Summation(40,50))
# print(Cal.Subtraction(70,90))
# print(Cal.Multiplication(40,60))
# # print(Cal.Divide(40,60))                                 

# class Calculation1:
#     def Addition(self,a,b):
#         return a+b
# class Calculation2:
#     def Subtraction(self,a,b):
#         return a-b
# class Calculation3:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2,Calculation3):
#     def Divide(self,a,b):
#         return a/b
# a=Derived()
# print(("Addition is:",a.Addition(40,50)),("Subtraction is:",a.Subtraction(80,80)),("Multiplication is:",a.Multiplication(90,80),("Division is:",a.Divide(60,50))))                                          

# class Cars:
#     def __init__(self,carName,carModel):
#         self.name=carName
#         self.model=carModel
#     def showName(self):
#         print(self.name)
#     def showModel(self):
#         print(self.model)
# class ID:
#     def __init__(self,carId):
#         self.carId=carId
#     def getId(self):
#         return self.carId
# class Main(Cars,ID):
#     def __init__(self,name,model,id):
#         Cars.__init__(self,name,model)
#         ID.__init__(self,id)                            
# Obj=Main(15628,"Benz",898)
# print(Obj.showModel(),Obj.showName(),Obj.getId())

# class Cars:
#     def __init__(self,carModel,carName):
#         self.name=carName
#         self.model=carModel
#     def showName(self):
#         print(self.name)
#     def showModel(self):
#         print(self.model)
# class ID:
#     def __init__(self,carId):
#         self.carID=carId
#     def getId(self):
#         return self.carID
# class Derived_class(Cars,ID):
#     def __init__(self,name,model,id):
#         Cars.__init__(self,name,model)
#         ID.__init__(self,id)
# Obj1=Derived_class("Mercedez Benz","Benz&8E",897)
# print(Obj1.showName(),Obj1.showModel(),Obj1.getId())                                  

class Cars:
    def __init__(self,carName,carModel):
        self.name=carName
        self.model=carModel
    def showName(self):
        return self.name
    def showModel(self):
        return self.model
class ID:
    def __init__(self, carid):
         self.carid=carid
    def getid(self):
        return self.carid
class Main_class(Cars,ID):
    def __init__(self,name,model,id):
        Cars.__init__(self,name,model)
        ID.__init__(self,id)
obj=Main_class("Rolls Roys","BKU8D4",9000)
print(obj.showName(),obj.showModel(),obj.getid())                     

