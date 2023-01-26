# class Duck:
#     def walk(self):
#         print("Tapak tapak")
# class Horse:
#     def wallk(self):
#         print("Tapdak pabdak")
# def my_function(obj):
#     obj.walk()
# d=Duck()
# my_function(d)                

# class Duck:
#     def walk(self):
#         print("Phurr Phurrr")
# class Snake:
#     def Prowl(self):
#         print("Rolling Rolling")
# class Horse:
#     def walk(self):
#         print("Tabdak tabdak")
# def my_function(obj):
#     obj.walk()
# b=Duck()
# b.walk()    
# c=Horse()
# c.walk() 
# a=Snake()
# a.walk()

# class theHobbit:
#     def __len__(self):
#         return 8987
# the_hobbit=theHobbit()
# print(len(the_hobbit))

# class Duck:
#     def swim(self):
#         print("Duck Walk")
# class Sparrow:
#     def swim(self):
#         print("Sparrow Walk")
# class Crocodile:
#     def swim(self):
#         print("Crocodile PRowls")
# def my_function(obj):
#     obj.swim()

# a=Duck()
# my_function(a)

# class Duck:
#     def swim(self):
#         print("Duck Walk")
# class Sparrow:
#     def swimm(self):
#         print("Sparrow Walk")
# class Dog:
#     def walk(self):
#         print("Dog walk")
# def my_function(obj):
#     obj.swim()
# obj1=Duck()
# obj1.swim()                            
# obj2=Sparrow()
# obj2.swimm()
# obj3=Dog()
# obj3.swim()

# class Duck:
#     def swim(self):
#         print(" I am a Duck...")
# class Sparrow:
#     def swim(self):
#         print("I am Sparrow")
# class crododile:
#     def prowl(self):
#         print("I am Crocodile..")
# def my_func(obj):
#     obj.swim()
# ind=Duck()
# ind.swim()        
# pak=Sparrow()
# pak.swim()                    

#Opertor Overloading
# class asEmployee:
#     def __init__(self,job):
#         self.job=job
#     def  __add__(self,other):
#         return self.job+other.job
# class asTutor:
#     def __init__(self,job):
#         self.job=job
# a=asEmployee(23500)
# b=asTutor(7000)
# print(a+b)

# class A:
#     def __init__(self,x):
#         self.x=x
#     def  __add__(self,other):
#         return self.x+other.x
# class B:
#     def __init__(self,x):
#         self.x=x
# a=A(200)
# b=B(300)
# print(a+b)        

# class A:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,o):
#         return self.a+o.a
# obj1=A(1)
# obj2=A(2)
# obj3=A("Geeks")
# obj4=A("For")
# print(obj1+obj2)
# print(obj3+obj4)

# class complex:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b
# a=complex(1,6) 
# b=complex(3,4)
# print(a+b)

# class A:
#     def __init__(self,a):
#         self.a=a
#     def __lt__(self,other):
#         if self.a<other.a:
#             return "Object 1 is less Object 2"
#         else:
#             return "Object 2 is greater than Object 1"
#     def __eq__(self,other):
#         if self.a==other.a:
#             return "Both are equal"
#         else:
#             return "Not Equal"
# a=A(2)
# b=A(3)
# print(a<b)
# c=A(4)
# d=A(4)
# print(c==d)          

# def product(a,b):
#     p=a*b
#     print(p)
# def product(a,b,c):
#     p=a*b*c
#     print(p)
# product(3,4,8)laa

# class myClass:
#     def sum(self,a,b,c):
#         s=a*b*c
#         return s
# obj=myClass()
# print(obj.sum(10,20,30)) 

# class my_class:
#     def sum(self,a=None, b=None, c=None):
#         if a!=None and b!=None:
#             s=a+b+c
#             return s
# obj=my_class()
# print(obj.sum(20,20,20))

# class myClass:
#     def sum(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c 
#             return s
#         elif a!=None and b!=None:
#             s=a*b
#             return s
#         else:
#             s="Provide atleast two digit number"
#             return s
# obj=myClass()
# print(obj.sum(20,20,20))                

# class myClass:
#     def sum(self,a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#             return s
#         elif a!=None and b!=None:
#             s=a*b
#             return s
#         else:
#             return "Please.. Provide atleast two integers" 
# obj=myClass()
# print(obj.sum(20,20))    

# class my_class:
#     def sum(self,a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#             return s
#         elif a!=None and b!=None:
#             s=a*b
#             return s
#         else:
#             return "Please.. Enter atleast two integer...!!"
# obj=my_class()
# print(obj.sum(90,59))

#Method Over-loading
# class College:
#     def attendance(self,x):
#         print("College attendance is 99%")
# class Professor(College):
#     def attendance(self,x):
#         print("Professor attendence is 98%")
# class Student(College):
#     def attendance(self,x):
#         super().attendance(10)
#         print("Student is Lethargic")
# obj=Student()
# obj.attendance(10)            

class Company:
    def work(self,x):
        print("Comapany has some projects")
class Employee(Company):
    def work(self,x):
        super().work("Project name is Flutter Payment app")
        print("Project has been given to Employee")
obj=Employee()
obj.work("Project Flutter Payment App is Completed")