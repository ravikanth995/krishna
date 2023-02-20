# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     def sides(self):
#         pass
# class Triangle(Polygon):
#     def sides(self):
#         print("Triangle")
# class Pentagon(Polygon):
#     def sides(self):
#         print("Pentagon")
# class Hexagon(Polygon):
#     def sides(self):
#         print("Hexagon")                        
# t=Triangle()
# t.sides()
# p=Pentagon()
# p.sides()
# h=Hexagon()
# h.sides()        

# from abc import ABC, abstractmethod
# class llgm:
#     pass
# class Square(llgm):
#     length=6
#     def Area(self):
#         return self.length*self.length
# class Circle(llgm):
#     radius=7
#     def Area(self):
#         return self.radius*self.radius        

# sq=Square()
# print(sq.Area())
# ci=Circle()
# print(ci.Area())        

# from abc import ABC, abstractmethod
# class Maths:
#     pass
# class Cube(Maths):
#     x=int(input("Enter X value:"))
#     def sides(self):
#         return self.x*self.x
# class Square(Maths):
#     y=int(input("Enter Y Number:"))
#     def sides(self):
#         return self.y*self.y*self.y
# c=Cube()
# print("Cube of X is:",c.sides())
# s=Square()
# print("Square of Y is:",s.sides())             

# from abc import ABC, abstractmethod
# class Maths:
#     pass
# class Square(Maths):
#     x=int(input("Enter X value:"))
#     def sides(self):
#         return self.x*self.x
# class Cube(Maths):
#     y=int(input("Enter Y Value:"))
#     def sides(self):
#         return self.y*self.y*self.y
# s=Square()
# print("Square of X Value is:",s.sides())
# c=Cube()
# print("Cube of Y is:",c.sides())                   

# from abc import ABC, abstractmethod
# class Subject:
#     @abstractmethod
#     def subject(self):
#         pass
# class math(Subject):
#     def subject(self):
#         print("Mathematics")
# class Physics(Subject):
#     def subject(self):
#         print("Physics Subject")
# class Chemistry(Subject):
#     def subject(self):
#         print("Chemistry subject")
# class Biology(Subject):
#     def  subject(self):
#         print("Biology Subject")
# obj=math()
# obj.subject()
# obj=Physics()
# obj.subject()
# obj=Chemistry()
# obj.subject()
# obj=Biology()
# obj.subject()

# from abc import ABC, abstractmethod
# class Payment:
#     @abstractmethod
#     def payment(self,amount):
#         pass
#     def print_slip(self,amount):
#         print("Purchase of Rs...:",amount)
# class CreditCardPayment(Payment):
#     def payment(self, amount):
#         print("Credit Card Payment of Rs...:",amount)    
# class PayTmPayment(Payment):
#     def payment(self, amount):
#          print("PayTm payment of Rs...:",amount) 
# obj=CreditCardPayment()
# print(obj.payment(600))
# print(obj.print_slip(700))
# print(isinstance(obj,CreditCardPayment))
# print(issubclass(CreditCardPayment,Payment))
# print("-"*50)
# obj1=PayTmPayment()
# print(obj1.payment(700))
# print(obj1.payment(8777))
# print(isinstance(obj1,PayTmPayment))
# print(issubclass(PayTmPayment, Payment))
