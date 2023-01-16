#Single Inheritance
# class parent:
#     def func(self):
#         print("Parent")
# class Child(parent):
#     def func1(self):
#         print("Child")
# test=Child()
# test.func()
# test.func1() 

# class parent:
#     def func(self):
#         print("Hello Parent")
# class Child(parent):
#     def func1(self):
#         print("Hello Child")
# test=Child()
# test.func()
# test.func1()                             

# class Parent:
#     def func(self):
#         print("Hello Parent")
# class Child(Parent):
#     def func1(self):
#         print("Hello Child")
# test=Child()
# test.func1()
# test.func()

# class Parent:
#     def func(self):
#         print("Hello Parent")
# class Child(Parent):
#     def func1(self):
#         print("Hello Child")
# test=Child()
# test.func()
# test.func1()                

# class Parent:
#     def func(self):
#         print("Hello Parent")
# class Child(Parent):
#     def func1(self):
#         print("hello Child")
# test=Child()
# test.func()
# test.func1()        

# class Teacher:
#     def class1(self):
#         print("This is Teacher")
# class Student(Teacher):
#     def Class2(self):
#         print("Hi Student")
# test=Student()
# test.class1()
# test.Class2()        

# class Teacher:
#     def outer(self):
#         print("Hi World")
# class Student(Teacher):
#     def inner(self):
#         print("Hi Chittapur")
# test=Student()
# test.outer()
# test.inner()      

# class HOD:
#     def DoC(self):
#         print("Chmistry Department")
# class Proffesor(HOD):
#     def Class(self):
#         print("Bio-Chemistry Department")
# test=Proffesor()
# test.DoC()
# test.Class()          

# class Science:
#     def func(self):
#         print("Hi World")
# class Maths(Science):
#     def func1(self):
#         print("Hi SciFi")
# test=Maths()
# test.func()
# test.func1()                  

# #Multi-ple Inheritance
# class GrandFather:
#     def func(self):
#         print("GrandFather India")
# class Father:
#     def func1(self):
#         print("Hello.. Father")
# class Mother:
#     def func2(self):
#         print("Mother India")
# class Child(GrandFather,Father,Mother):
#     def func3(self):
#         print("Hi... Child")
# test=Child()
# test.func()
# test.func1()
# test.func2()
# test.func3()
# print(Child.__mro__)                

# class Indus_Valley:
#     def func(self):
#         print("Harappan Valley")
# class Vedic_Period:
#     def func1(self):
#         print("Vedic Age") 
# class Later_Vedic:
#     def func2(self) :
#         print("Later Vedic Period")
# class Present_Time(Indus_Valley,Vedic_Period,Later_Vedic):
#     def func3(self):
#         print("At Present is 2023")
# test=Present_Time()
# test.func()
# test.func1()
# test.func2()
# test.func3()  
# print(Present_Time.__mro__)              

class Hinduism:
    def func(self):
        print("Hinduism is the Mother")
class Buddhism:
    def func1(self):
        print("Buddha is reformer")
class Jainism:
    def func2(self):
        print("Mahaveer Vardhaman is peaceful")
class Logic(Hinduism,Buddhism,Jainism):
    def func3(self):
        print("Logic is evolved from Dharmic religions")
test=Logic()
test.func()
test.func1()
test.func2()
test.func3()                