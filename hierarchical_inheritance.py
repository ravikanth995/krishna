# class Brands:
#     brand_name1="Amazon"
#     brand_name2="Ebay"
#     brand_name3="OLX"
# class Products(Brands):
#     prod1="Online E-commerce Store"
#     prod2="Online Store"
#     prod3="Online Buy Sell Store"
# class Popularity(Brands):
#     prod_popularity1=100
#     prod_popularity2=70
#     prod_popularity3=50
# class value(Brands):
#     prod1_value="Excellent Value"
#     prod2_value="Better Value"
#     prod3_value="Good Value"
# obj1=Products()
# obj2=Popularity()
# obj3=value()
# # print(obj1.brand_name1+" Is an "+obj1.prod1)
# # print(obj1.brand_name2+" is an "+obj1.prod2)
# # print(obj1.brand_name3+" is "+obj1.prod3)
# # print(obj2.brand_name1+"has",obj2.prod_popularity1)
# print(obj3.brand_name1+" has "+obj3.prod3_value)

# class Brands:
#     brand_name1="Amazon"
#     brand_name2="FlipCart"
#     brand_name3="SnapDeal"
# class Products(Brands):
#     Product1="E-Commerce Store"
#     Products2="E-Commerce Platform"
#     Products3="Boycotted Platform"
# class Price(Brands):
#     Product_price1=1000
#     Product_price2=999 
#     Product_price3=8999 
# class Feedback(Brands):
#     Product_Feedback1="Good Product"
#     Product_Feedback2="Excellent Product"
#     Product_Feedback3="Genuine Product"
# obj1=Products()
# obj2=Price()
# obj3=Feedback()
# print(obj1.brand_name1+" is "+obj1.Product1)           

# class Details:
#     def __init__(self):
#         self.__id="<No Id"
#         self.__name="<No Name>"
#         self.__gender="<No Gender>"
#     def setData(self,id,name,gender):
#         self.__id=id
#         self.__name=name
#         self.__gender=gender
#     def showData(self):
#         print("Id:",self.__id)
#         print("Name:",self.__name)
#         print("Gender:",self.__gender)
# class Employee(Details):
#     def __init__(self):
#         self.__company="<No Comapany"
#         self.__dept="<No Department>" 
#     def setEmployee(self,id,name,gender,company,department):
#         self.setData(id,name,gender)
#         self.__company=company
#         self.dept=department
#     def showEmployee(self):
#         self.showData()
#         print("Company:",self.__company)
#         print("Department:",self.__dept)
#     def Main():
#         print("Employee Object")
#         e=Employee()
#         e.showData()
#         e.setEmployee(12387,"Ravikanth","Male","Oscar Academy","Senior Manager")
#         e.showEmployee()                           

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

class Shape:
    def __init__(self,name,length,breadth):
        self.name=name
        self.l=length
        self.b=breadth
    def Display(self):
        print("Length Is:",self.l)
        print("Breadth is:",self.b)
class Rectangle(Shape):
    def rect_info(self):
        a=self.l*self.b
        print("Area of:",self.name,"is",a)
class Triangle(Shape):
    def Tri_info(self):
        a=0.5*self.l*self.b
        print("Area of:",self.name,"is",a)
obj=Rectangle("Rectangle",10,20) 
obj.Display()
obj.rect_info()
print("-"*30)
obj1=Triangle("triangle",80,7)
obj1.Display()
obj1.Tri_info()                           