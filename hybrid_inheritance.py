
# class Vehicle:
#     def info(self):
#         print("Vehicle")
# class Car(Vehicle):
#     def car_info(self):
#         print("Car Information")
# class truck(Vehicle):
#     def truck_info(self):
#         print("truck")
# obj=Car()
# obj.info()
# obj.car_info()

# obj1=truck()
# obj1.info()
# obj1.truck_info()

# class Vehicle:
#     def info(self):
#         print("It is Vehicle")
# class Car(Vehicle):
#     def car_info(self):
#         print("It is a BMW Car")
# class Truck(Vehicle):
#     def truck_info(self):
#         print("It is a Ashok Laylands")
# obj=Car()
# obj.info()
# obj.car_info()
# obj1=Truck()
# obj1.info()
# obj1.truck_info()

# class Animals:
#     def animal_info(self):
#         print("Animals")
# class Cat(Animals):
#     def cat_info(self):
#         print("This is Cat.. Mewow")
# class Dog(Animals):
#     def dog_info(self):
#         print("This is Dog.. bhow")
# obj=Cat()
# # obj.animal_info()
# obj.cat_info()
# obj1=Dog()
# # obj1.animal_info()
# obj1.dog_info()               

# class Shape:
#     def __init__(self,name,length,breadth):
#         self.name=name
#         self.l=length
#         self.b=breadth
#     def display(self):
#         print("Length is:",self.l)
#         print("Breadth is:",self.b)
# class Rect(Shape):
#     def rect_area(self):
#         a=self.l*self.b
#         print("Area of:",self.name, "is",a)
# class Tri(Shape):
#     def Tri_area(self):
#         a=0.5*self.l*self.b
#         print("Area of:",self.name, "is",a) 
# obj=Rect("Rectangle",10,20)
# obj.display()
# obj.rect_area()
# obj1=Tri("Triangle",10,10) 
# obj1.display()
# obj1.Tri_area()                                   

# class Shape:
#     def __init__(self,name,length,breadth):
#         self.name=name
#         self.l=length
#         self.b=breadth
#     def Display(self):
#         print("Length Is:",self.l)
#         print("Breadth is:",self.b)
# class Rectangle(Shape):
#     def rect_info(self):
#         a=self.l*self.b
#         print("Area of:",self.name,"is",a)
# class Triangle(Shape):
#     def Tri_info(self):
#         a=0.5*self.l*self.b
#         print("Area of:",self.name,"is",a)
# obj=Rectangle("Rectangle",10,20) 
# obj.Display()
# obj.rect_info()
# print("-"*30)
# obj1=Triangle("triangle",80,7)
# obj1.Display()
# obj1.Tri_info()   

# class Vehicle:
#     def __init__(self,model,mileage,price):
#         self.price=price
#         self.model=model
#         self.mileage=mileage
#         self.price=price
#     def showData(self):
#         print(f"model : {self.model}") 
#         print(f"price : {self.price}")
#         print(f"mileage : {self.mileage}")
# class Bike(Vehicle):
#     def __init__(self,model,mileage,price,tyre,cc):
#         super().__init__(model,mileage,price)
#         self.cc=cc
#         self.tyre=tyre
#     def showDetails(self):
#         super().showData()
#         print(f"CC :{self.cc}")
#         print(f"tyres: {self.tyre}")
#     # Method of derived class
#     def rating(self):
#         print("4 Star")
# class Car(Bike,Vehicle):
#     def rating(self):
#         print("5 Star")
# Bajaj=Bike("Dommar",40,145000,2,500)
# print("-"*30) 
# Tata=Car("Safari",25,80000,7,2000)
# Bajaj.showDetails()
# Bajaj.rating()
# print("-"*30)
# Tata.showDetails()
# # Bajaj.showData()
# Tata.rating()
# print("-"*30)

# class vehicle:
#     def __init__(self,model,mileage,price):
#         self.price=price
#         self.model=model
#         self.mileage=mileage
#         self.price=price
#     def showData(self):
#         print(f"model : {self.model}")
#         print(f"price : {self.price}")
#         print(f"mileage : {self.mileage}") 
# class bike(vehicle):
#     def __init__(self,model,mileage,price,tyre,cc):
#         super().__init__(model,mileage,price)          
#         self.cc=cc
#         self.tyre=tyre
#     def showDetails(self):
#         super().showData()
#         print(f"CC :{self.cc}")
#         print(f"tyres: {self.tyre}") 
#     def rating(self):
#         print("4 Star")
# class Car(bike,vehicle):
#     def rating(self):
#         print("5 Star")

# Bajaj=bike("Chetak",40,120000,2,500)
# Tata=Car("Tata Sumo",25,8000000,4,2000)
# Bajaj.showDetails()
# Bajaj.showData()
# Bajaj.rating()
# print("-"*40)
# Tata.showDetails()
# Tata.showData()
# Tata.rating()

# class vehicle:
#     def __init__(self,model,mileage,price):
#         self.price=price        
#         self.model=model
#         self.mileage=mileage
#         self.price=price
#     def showData(self):
#         print(f"model : {self.model}")
#         print(f"price : {self.price}")
#         print(f"mileage : {self.mileage}")
# class bike(vehicle):
#     def __init__(self,model,mileage,price,tyre,cc):
#         super().__init__(model,mileage,price)          
#         self.cc=cc
#         self.tyre=tyre
#     def showDetails(self):
#         super().showData()
#         print(f"CC :{self.cc}")
#         print(f"tyres: {self.tyre}") 
#     def rating(self):
#         print("4 Star")
# class Car(bike,vehicle):
#     def rating(self):
#         print("5 Star")

# Bajaj=bike("Chetak",40,120000,2,500)
# Tata=Car("Tata Sumo",25,8000000,4,2000)
# Bajaj.showDetails()
# Bajaj.showData()
# Bajaj.rating()
# print("-"*40)
# Tata.showDetails()
# Tata.showData()
# Tata.rating()

# class vehicle:
#     def __init__(self,model,mileage,price):
#         self.model=model
#         self.mileage=mileage
#         self.price=price
#     def showDetails(self):
#         print(f"Model is : {self.model}")
#         print(f"Price is : {self.price}")
#         print(f"Mileage is : {self.mileage}") 
# class Bike(vehicle):
#     def __init__(self,model,mileage,price,tyre,cc):
#         super().__init__(model,mileage,price)
#         self.cc=cc
#         self.tyre=tyre
#     def showDetails(self):
#         super().showDetails()
#         print(f"CC : {self.cc}") 
#         print(f"Tyre: {self.tyre}") 
#     def rating(self):
#         print("4 rating")

# class Car(Bike,vehicle):
#     def rating(self):
#         print("5 Star")
# Bajaj=Bike("Honda Shine",39, 120000, 2, 125)
# Bajaj.showDetails()
# Bajaj.rating()
# print("-"*40)
# Tata=Car("Tata Nano",8929, 100000, 4, 1670) 
# Tata.showDetails()
# Tata.rating()
# print("-"*40)       

# class Computer:
#     def func1(self):
#         print("I am Computer")
# class Laptop(Computer):
#     def func2(self):
#         print("I am Laptop")
# class Mouse(Laptop):
#     def func3(self):
#         print("I am Mouse")
# class Student(Mouse,Laptop):
#     def func4(self):
#         print(" I am Student")
# obj=Student()
# obj.func4()
# obj.func1()        
# obj.func2()
# obj.func3()

# class CP:
#     def func(self):
#         print("I am PC")
# class Laptop(CP):
#     def func1(self):
#         print("I am Laftop")
# class Mouse(Laptop):
#     def func2(self):
#         print(" I am Mouse")
# class Student(Mouse,Laptop):
#     def func3(self):
#         print("I am Student")
# obj=Student()
# obj.func()
# obj.func1()
# obj.func2()                          
# obj.func3()

# class parent:
#     def func(self):
#         print("I am Parent")
# class Child(parent):
#     def func1(self):
#         print("This is Function 1")
#         super().func()
#         print("This is function 2")        
# obj=Child()
# obj.func1()        

