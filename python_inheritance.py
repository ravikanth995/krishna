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

class Parent:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def Employee_Details(self):
        return self.name, self.id
    def Employee_check(self):
        if self.id>4999:
            return "Valid Employee"
        else:
            return "Not valid Employee"
class Child(Parent):
    def end(self):
        print("End")            
e1=Parent("ravikanth",15291)
print(e1.Employee_Details(),e1.Employee_check())
e2=Child("Baby",50000)
print(e2.Employee_Details(),e2.Employee_check())                        
        

