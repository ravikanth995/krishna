# class Parent:
#     def func(self):
#         print("This is Function")
# class Child(Parent):
#     def func(self):
#         print("This is Function 1")
# c=Child()
# c.func()         

# class Parent:
#     def func1(self):
#         print("Hello Parent")
# class Child(Parent):
#     def func2(self):
#         print("Hello Child")
# c=Child()        
# print(isinstance(c,Parent))
    
# class Parent:
#     def func1(self):
#         print("Hello Parent")
# class Child(Parent):
#     def func1(self):
#         print("Hello Child")
# print(issubclass(Child,Parent))               

# class Students:
#     def __init__(self,name,rank,points):
#         self.name=name
#         self.rank=rank
#         self.points=points
#     def demo_func(self):
#         print("I am "+self.name)
#         print("I Got",+self.rank,"rank")
# st1=Students("Ravi",1,100)
# st1.demo_func()
# print("-"*40) 
# st2=Students("Steve",2,90)
# st2.demo_func()
# print("-"*40) 
# st3=Students("John",3,59)
# st3.demo_func()
# print("-"*49)
# st4=Students("Baptiste",4,68)
# st4.demo_func()               

# class Students:
#     def __init__(self,name,rank,points):
#         self.name=name
#         self.rank=rank
#         self.points=rank
#     def demo_func(self):
#         print("I am:"+self.name)
#         print("I Have Got",+self.rank)
# st1=Students("Steve",1, 90)
# st1.demo_func()            
# print("-"*40)
# st2=Students("John",2,98)
# st2.demo_func()
# print("-"*40)
# st3=Students("Smith",3,97)
# st3.demo_func()
# print("-"*40)
# st4=Students("Adam",4,88)
# st4.demo_func()

# class Employee:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.salary=salary
#         self.project=project
#     def show(self):
#         print("Name",self.name,"Salary is:",self.salary) 
#     def work(self):
#         print(self.name,"is working on",self.project)
# emp=Employee("Ravi",8000,"MTS")
# emp.show()
# emp.work()               

