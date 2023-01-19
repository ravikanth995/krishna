# # #Multiple-Inheritance
# class GrandFather:
#     def func(self):
#         print("Hi.. I am Grandfather!!")
# class Father(GrandFather):
#     def func1(self):
#         print("Hi.. I am Father!!")
# class Child(Father):
#     def func2(self):
#         print("Hi.. I am Child")
# test=Child()
# test.func()
# test.func1() 
# test.func2()     
# print(Child.__mro__)

# class SuperClass:

#     def super_method(self):
#         print("Super Class method called")

# # define class that derive from SuperClass
# class DerivedClass1(SuperClass):
#     def derived1_method(self):
#         print("Derived class 1 method called")

# # define class that derive from DerivedClass1
# class DerivedClass2(DerivedClass1):

#     def derived2_method(self):
#         print("Derived class 2 method called")

# # create an object of DerivedClass2
# d2 = DerivedClass2()

# d2.super_method()  # Output: "Super Class method called"

# d2.derived1_method()  # Output: "Derived class 1 method called"

# d2.derived2_method()  # Output: "Derived class 2 method called"

# class SuperClass:
#     def super_base(self):
#         print("Hi.. This is Superclass")
# class Derived1(SuperClass):
#     def base_class(self):
#         print("Hi.. This is Base class")
# class Derived2(Derived1):
#     def derived_class(self):
#         print("This is Derived class")
# test=Derived2()
# test.super_base()
# test.base_class()
# test.derived_class()
# print(Derived2.__mro__)  

# class Super_Class:
#     def func(self):
#         print("This is Super Class")
# class base_class(Super_Class):
#     def func1(self):
#         print("This is base class")
# class derived(base_class):
#     def func2(self):
#         print("This is Derived class")
# test=derived()
# test.func()
# test.func1()
# test.func2()
# print(derived.__mro__)

#Heirarchical Inheritance.
# class Parent:
#     def func(self):
#         print("This is Parent")
# class child1(Parent):
#     def func1(self):
#         print("This is Child 1!!")
# class Child2(Parent):
#     def func2(self):
#         print("This is Child 2")
# test=child1()
# test1=Child2()

# test.func()
# test.func1()

# test1.func()
# test1.func2()
# print(child1.__mro__)
# print(Child2.__mro__)

# class Parent:
#     def func(self):
#         print("This is Parent")
# class Child1(Parent):
#     def func1(self):
#         print("This is Child 1 !!")
# class Child2(Parent):
#     def func2(self):
#         print("This is Child 2!!")
# test1=Child1()
# test2=Child2()

# test1.func()
# test1.func1()
# test2.func()
# test2.func2()

# class Parent1:
#     def func(self):
#         print("This is Parent1")
# class Parent2:
#     def func1(self):
#         print("This is Parent 2")
# class Child1(Parent1,Parent2):
#     def func2(self):
#         print("Child 2")
# print("-"*30)        
# class Child2(Child1):
#     def func3(self):
#         print("This is Child2")
# test1=Child1()
# test2=Child2()
# test1.func()
# test1.func1()
# print("-"*40)
# test2.func()
# test2.func1()
# test2.func2()
# test2.func3()
# print(Child1.__mro__)
# print(Child2.__mro__)        

# class Parent1:
#     def func(self):
#         print("This is Parent1 !!")
# class Parent2:
#     def func1(self):
#         print("This is Parent2 !!") 
# class Child1(Parent1,Parent2):
#     def func2(self):
#         print("This is Child 1 !!")
# class Child2(Child1,Parent2):
#     def func3(self):
#         print("This is child 2")
# test1=Child1()
# test2=Child2()

# test1.func()
# test1.func1()
# test2.func()
# test2.func1()
# test2.func2()
# test2.func3()
# print(Child1.__mro__)
# print(Child2.__mro__)

#Single Inheritance
# class Parent_Class:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_Details(self):
#         return self.id, self.name
#     def Employee_Check(self):
#         if self.id>50000:
#             return " Is valid Employee" 
#         else:
#             return "Invalid Employee" 
# class Derived_Class(Parent_Class):
#     def End(self):
#         print("End of Program")

# Employee1=Parent_Class("Ravikanth",1537199)
# print(Employee1.Employee_Details(),Employee1.Employee_Check())

# Employee2=Derived_Class("Employee 1", 1537198)
# print(Employee2.Employee_Details, Employee2.Employee_Check())

# class Parent_class(object):
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_details(self):
#            return self.id, self.name
    
#     def Employee_check(self):
#           if self.id>500:
#             return "Is a Valid Employee"
#           else:
#             return "Is not a Valid Employee"
# class Derived_class(Parent_class):
#     def end(self):
#         print("End of PRogram")

# Employee1=Parent_class("ravi",5000)
# print(Employee1.Employee_details(), Employee1.Employee_check())

# class Parent_Class:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_check(self):
#         return self.name,self.id
#     def Employee_Details(self):
#         if self.id>5000:
#             return "Valid Employee"
#         else:
#             return "Invalid Employee"
# class Derived_class(Parent_Class):
#     def End(self):
#         print("End of Program")
# Employee1=Parent_Class("RaviKanth",59000)
# Employee2=Derived_class("ShivRaj",4999)
# print(Employee1.Employee_Details(),Employee1.Employee_check())
# print(Employee2.Employee_Details(),Employee2.Employee_check())
# print(Parent_Class.__mro__)
# print(Derived_class.__mro__)

# class Parent_Class:
#     def __init__(self,name,Id):
#         self.name=name
#         self.Id=Id
#     def Employee_Details(self):
#         return self.Id, self.name
#     def Employee_Check(self):
#         if self.Id>5000:
#             return "Valid Employee"
#         else:
#             return "Not a Valid Employee"
# class Child_class(Parent_Class):
#     def End(self):
#         print("End of program")
# Employee1=Parent_Class("RaviKanth",5001)
# print(Employee1.Employee_Details(),Employee1.Employee_Check())
# Employee2=Child_class("Rajkumar",4999)
# print(Employee2.Employee_Details(),Employee2.Employee_Check())                  

# class Parent_class:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_Details(self):
#         return self.id, self.name
#     def Employee_Check(self):
#         if self.id>5000:
#             return "Valid Employee"
#         else:
#             return "Not valid Employee"
# class Child_class(Parent_class):
#     def End(self):
#         print("End of Program")
# Employee1=Parent_class("Ravikanth",50000)
# print(Employee1.Employee_Details(),Employee1.Employee_Check())
# Employee2=Child_class("Giriraj",80000)
# print(Employee2.Employee_Details(),Employee2.Employee_Check())                  

# class Parent_Class:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_details(self):
#         return self.name, self.id
#     def Employee_Check(self):
#         if self.id>4999:
#             return "Valid Employee"
#         else:
#             return "not valid Employee"
# class Child_class(Parent_Class):
#     def End(self):
#         print("End of Program") 
# Employee1=Parent_Class("Ashtavkra",90000)
# print(Employee1.Employee_details(),Employee1.Employee_Check())
# Employee2=Child_class("freidrick",99999)
# print(Employee2.Employee_details(), Employee2.Employee_Check())                                                   

# class Parent:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Employee_Details(self):
#         return self.name, self.id
#     def Employee_check(self):
#         if self.id>4999:
#             return "Valid Employee"
#         else:
#             return "Not valid Employee"
# class Child(Parent):
#     def end(self):
#         print("End")            
# e1=Parent("ravikanth",15291)
# print(e1.Employee_Details(),e1.Employee_check())
# e2=Child("Baby",50000)
# print(e2.Employee_Details(),e2.Employee_check())                        
        
# class Parent_class:
#     def __init__(self, value1,value2):
#         self.value1=value1
#         self.value2=value2
#     def add(self):
#         print("Addition value1:", self.value1)
#         print("Addition of value2:",self.value2)
#         return self.value1+self.value2
#     def multi(self):
#         print("Multiplication of value1:",self.value1)
#         print("Multiplication value 2:",self.value2) 
#         return self.value1*self.value2
#     def Sub(self):
#         print("Subtraction of two values:",self.value1)
#         print("Subtraction of Value 2:",self.value2)
#         return self.value1-self.value2
#     def div(self):
#         print("Division of value1:",self.value1)
#         print("division of value2 :",self.value2)
#         return self.value1/self.value2 
# class Child_class(Parent_class):
#         pass
# obj1=Child_class(10,18)
# print("Added values:",obj1.add())
# print("-"*30)
# obj2=Child_class(90,13)
# print("Multiplication of two values:",obj2.multi())          
# print("-"*30)                
# obj3=Child_class(90,60)
# print("Subtraction of values:",obj3.Sub())
# print("-"*40)
# obj4=Child_class(140,10)
# print("Division of two values:",obj4.div())

# class Parent_class:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("Addition A:",self.a)
#         print("Addition B:",self.b)
#         return self.a+self.b 
#     def sub(self):
#         print("Subtraction a:",self.a)
#         print("Subtraction b :",self.b)
#         return self.a-self.b
#     def multi(self):
#         print("A Multiplication:",self.a)
#         print("B Multiplication:",self.b)
#         return self.a*self.b
#     def div(self):
#         print("A Division:",self.a)
#         print("B Division: ",self.b)               
#         return self.a/self.b
# class Child_class(Parent_class):
#     pass
# obj1=Child_class(20,30) 
# print("Addition of a and b:",obj1.add())
# print("-"*40)
# obj2=Child_class(30,10)
# print("Subtraction of a and b:",obj2.sub())
# print("-"*30) 
# obj3=Child_class(30,4)
# print("Multiplication of a and b is:",obj3.multi())
# print("-"*40) 
# obj4=Child_class(30,2)
# print("Division of a and b is:",obj4.div())
# print("End"*30)     

# class Parent_class:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("A Addition value is:",self.a)
#         print("B Addition Value is:",self.b)
#         return self.a+self.b 
#     def sub(self):
#         print("A Subtracting value is:",self.a)
#         print("B Subtracting value is:",self.b)
#         return self.a-self.b
#     def multi(self):
#         print("A Multiplied value is:",self.a)
#         print("B Multiplied value is:",self.b)
#         return self.a*self.b
#     def Div(self):
#         print("A Divisible value is:",self.a)
#         print("B Divisible value is:",self.b)
#         return self.a/self.b
# class Child_class(Parent_class):
#     pass

# obj1=Child_class(50,8)
# print("Addition is:",obj1.add())
# print("-"*20)
# obj2=Child_class(30,6)
# print("Subtraction is:",obj2.sub())
# print("-"*30)
# obj3=Child_class(50,3)
# print("Multiplication value is:",obj3.multi())
# print("-"*34)
# obj4=Child_class(30,10)
# print("Divisional Value is:",obj4.Div())

# class Parent_class:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def multi(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
# class Child_class(Parent_class):
#     pass
# obj1=Child_class(120,20)
# print("Addition is:",obj1.add())
# print("-"*30) 
# obj2=Child_class(30,60)
# print("Subtraction is:",obj2.sub())
# print("-"*39)
# obj3=Child_class(40,20)
# print("Multiplication is:",obj3.multi())
# print("-"*40) 
# obj4=Child_class(30,40)
# print("Division is:",obj4.div())

class Parent_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("A and B Values are:",self.a, self.b)
        return self.a+self.b
    def sub(self):
        print("A nd B values are:",self.a,self.b)
        return self.a-self.b
    def multi(self):
        print("A and B values are:",self.a,self.b)
        return self.a*self.b
    def div(self):
        print("A and B Values are:",self.a,self.b)
        return self.a/self.b
class Child_class(Parent_class):
    pass
obj1=Child_class(30,30)
print("Addition of A and B is:",obj1.add())
print("-"*30)
obj2=Child_class(19,20)
print("Subtraction of A and B is:",obj2.sub())
print("-"*30)
obj3=Child_class(60,30) 
print("Multiplication of A and B is:",obj3.multi())
print("-"*30)
obj4=Child_class(40,2)
print("Division of two values:",obj4.div())
                   
