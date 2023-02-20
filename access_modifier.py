#Public Modifier
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         pass
#         # print("Name:",self.name, "Salary is :",self.salary)
# emp=Employee("Jessa",1000000)
# print("Name",emp.name, "Salary is:",emp.salary)
# emp.show()            

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print("Name is:",self.name, "\nSalary is:",self.salary)
# emp=Employee("RavKanth",120000) 
# emp.show() 

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print("Name is =",self.name, "\nSalary is =",self.salary)
# emp=Employee("Ravi",12000)
# emp.show()                      

# Private Access Modifier
# class Employee:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
# emp1=Employee("Shashi",12999)
# # emp1.__name
# # emp1.__salary
# print(emp1._Employee__name)
# print(emp1._Employee__salary)

# class Employee:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#     def show(self):
#         print(self.__name,"salary",self.__salary)
# e1=Employee("Ravikanth",12000)
# print(e1._Employee__name)
# print(e1._Employee__salary)

# class College:
#     def __init__(self,name,registerNo,fee):
#         self.__name=name
#         self.__registerNo=registerNo
#         self.__fee=fee
#     def show(self):
#         print(self.__name,"Register No is:",self.__registerNo, "Fee remaining is:",self.__registerNo)
# e1=College("Ravikanth",1537199, 12000)
# e1.show()
# print(e1._College__name)
# print(e1._College__registerNo)
# print(e1._College__fee)            

# class Student:
#     def __init__(self,name,age,registerNo):
#         self.__name=name
#         self.__age=age
#         self.__registerNo=registerNo
#     def show(self):
#         print(self.__name,"age is:",self.__age,"Register Number is:",self.__registerNo)
# e1=Student("Ravikanth\'s",27,1537199)
# # print(e1._Student__show())
# print(e1._Student__name)
# print(e1._Student__age)
# print(e1._Student__registerNo)            
# print(e1.show())

# class Student:
#     def __init__(self,name,age,regNo,marks):
#         self.__name=name
#         self.__age=age
#         self.__regNo=regNo
#         self.__marks=marks
#     def show(self):
#         print(self.__name,"age is ",self.__age,"Register No:",self.__regNo,"Marks is: ",self.__marks)
# e1=Student("Ravikanth\'s",27,1537199,598)
# print(e1._Student__name)
# print(e1._Student__age)
# print(e1._Student__regNo)
# print(e1._Student__marks) 
# print(e1.show())           

#protected
# class Company:
#     def __init__(self,name,project):
#         self._name=name
#         self._project=project
# class Employee(Company):
#     def __init__(self,name,project):
#         self.name=name
#         super().__init__(name,project)
#     def show(self):
#         print("Employee Name is:",self._name)
#         print("Is Working on:",self._project)
# e1=Employee("RaviKanth","ATM Fund")
# print(e1.show())
# # print("ATM Depsoite",e1._project)  

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age=age
# e1=Student("Ravi",27)
# #retriving age using getter
# print("Name is:",e1.name, e1.get_age())
# e1.set_age(17)
# print(" new age is:",e1.name,e1.get_age())   









