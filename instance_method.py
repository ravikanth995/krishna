# class Student:
#     def __init__(self,Name,Marks):
#         self.Name=Name
#         self.Marks=Marks
# std1=Student("Ravikanth",27)
# std2=Student("Kurkure",90)
# std3=Student("Lays",98)
# print(std1.__dict__)

# class Student:
#     def __init__(self,name,marks):
#         self.Name=name
#         self.Marks=marks
# std1=Student("Ravikanth",88)
# std2=Student("Kshmira",87)
# std3=Student("Shaitan",77)
# print(std1.__dict__)
# print(std2.__dict__)
# print(std3.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
# std1=Student("Ravikanth",27)
# std2=Student("ShashiKanth",29)
# std3=Student("Shalini",30)
# print(std1.__dict__)
# print(std2.__dict__)
# print(std3.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
# s1=Student("Ravikanth",17)
# s2=Student("Shalini",29)
# s3=Student("Harisingh",28)
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
# s1=Student("ravikanth",28)
# s2=Student("ShashiKanth",12)
# s3=Student("Shalini",17)
# print(s1.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def display(self):
#         print(self.Age)
#         print(self.Name)
# s1=Student("Akshay",23)
# s2=Student("ShahRukhKahna",36)
# s3=Student("Guna",24)
# print(s1.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def display(self):
#         print(self.Age)
#         print(self.Name)
# s1=Student("Dhobi",23)
# s2=Student("SafaiWala",26)
# s3=Student("MilkMAn",27)
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)

# class Student:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age

#     def display(self):
#             print(self.name)
#             print(self.Age)

#     def changeData(self):
#         self.name=input("Enter Name")
#         self.Age=int(input("Enter age"))

# s1=Student("Ravikanth",27)
# s2=Student("Ravi Chavan",65)
# s3=Student("Ram Charan",17)
# # print(s1.__dict__)
# # print(s2.__dict__)
# # print(s3.__dict__)
# s1.changeData()
# print(s1.changeData())

# class Studemt:
#     collage="Govt. degree College"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Studemt("Akshay",65)
# print(s1.__dict__)

# class Employee:
#     comapanyName="Ostlo pvt ltd."
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# s1=Employee("Jay Shah",27)
# s2=Employee("Ajlan Shah",38)
# print(Employee.comapanyName)

# Employee.comapanyName="Tisco"
# print(Employee.comapanyName)
# s1.comapanyName="radha lrishna"
# print(Employee.comapanyName)

# class Employee:
#    company_name="RudraMan Pvt Ltd."
#    def __init__(self,name,age):
#         self.name=name
#         self.age=age
#    def display(self):
#         self.name=input("Enter name:")
#         self.age=int(input("Enter Age:"))

# s1=Employee("Deepika Paddukone",32)
# s2=Employee("Aish",23)
# print(s1.company_name)
# # print(s1.display())
# Employee.company_name="Buddha Lounge"
# print(Employee.company_name)

# class Employee:
#     company_name="Govt. degree College"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         self.name=input("Enter Name:")
#         self.age=int(input("Enter Age:"))
#     def change_Name(self):
#         print(Employee.company_name)
# s1=Employee("Ravi",19)
# s2=Employee("Shashi",20)
# # s1.company_name="S.B College"
# print(s1.company_name)

# class Employee:
#     college="Appa Medical College"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def get_name(cls):
#         print(f"company name is:",cls.college)
# e1=Employee("Ajay",2000000)
# e2=Employee("Ajatashatru",65555)
# print(Employee.college)
# print(e1.__dict__)

#Class Method
# class myClass:
#     def __init__(self,value):
#         self.value=value
#     def get_name(self):
#         return self.value
# obj=myClass(10)
# print(obj.__dict__)

# class myClass:
#     def __init__(self,Value):
#         self.Value=Value
#     def get_name(cls):
#        cls.Value
#     def get_value(self):
#         return self.Value
# obj=myClass(10)
# print(obj.get_value)
# # print(obj.get_name)
# print(obj.Value)

# class Employee:
#     company_name="InfoSys"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def get_comapny_name(cls):
#         cls.get_comapny_name="TataCS"
#         print(cls.company_name)
#         print(f"comapny name is:",cls.company_name)

# e1=Employee("Ajyani",50000)
# e2=Employee("Ajan shah",4000)
# Employee.get_comapny_name()
# print(e2.company_name)

#Static Method
# class myClass:
#     def __init__(self,value):
#         self.value

#     @staticmethod
#     def get_max_value(x,y):
#         return max(x,y)    
# obj=myClass
# print(myClass.get_max_value(20,30))
# print(obj.get_max_value(30,20))

# class myClass:
#     def __init__(self,value):
#         self.value=value
#     @staticmethod    
#     def get_max_value(x,y):
#         return max(x,y)
        
# obj=myClass(10)
# print(myClass.get_max_value(10,8))
# print(obj.get_max_value(90,7))       
# from datetime import date
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def fromBirthYear(cls,name,year):
#         return cls
#     @staticmethod
#     def isAdult(age):
#         return age>18
# person=Person("mayank",18)
# person1=Person.fromBirthYear("Mayank",25)
# print(person.age)
# # print(person1.age)
# print(person.isAdult(45))            

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name+" "+self.age)
# print("\nObject 1:")
# s1=Student("Ravikanth","36")
# # print(s1.name)
# # print(s1.age)
# s1.display()                 

# print("\nObject 2:")
# s2=Student("ShashiKanth","24")
# # print(s2.name)
# # print(s2.age)
# s2.display()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name+' '+self.age)
# print("Object 1:")
# s1=Student("RaviKanth","24")
# s1.display()
# print("\nObject 2:")
# s2=Student("Bhagvata","23")
# s2.display()
     
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name+" "+self.age)
# print("Object 1")
# s1=Student("NanaSutta","12")
# s1.display()
# print("\nObject 2")
# s2=Student("MamaSutta","25")
# s2.display()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name+" "+self.age)
# print("Object 1:") 
# s1=Student("Example 1:","21")
# s1.display()
# print("\nObject 2:")
# s2=Student("Example 2:","23")
# s2.display()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name+" "+self.age)
print("Object 1:")
s1=Student("Bhaga","22")
s1.display()
print("\nObject 2") 
s2=Student("Amman","25") 
s2.display()          