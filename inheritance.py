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

class Science:
    def func(self):
        print("Hi World")
class Maths(Science):
    def func1(self):
        print("Hi SciFi")
test=Maths()
test.func()
test.func1()                                