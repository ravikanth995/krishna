# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# class Child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name)
#         self.age=age
#     def get_Age(self):
#         return self.age
# class Grand_child(Child):
#     def __init__(self,name,age,location):
#         Child.__init__(self,name,age)
#         self.location=location
#     def getLocation(self):
#         return self.location

# ge=Grand_child("Ravikanth",59,"Chittapur")
# print(ge.getName(),ge.get_Age(), ge.getLocation())      

# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
# class child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name)
#         self.age=age
#     def get_age(self):
#         return self.age
# class Grandchild(child):
#     def __init__(self,name,age,location):
#         child.__init__(self,name,age)
#         self.location=location
#     def get_location(self):
#         return self.location
# ge=Grandchild("Ravikanth",27,"Chittapur")
# print(ge.get_name(),ge.get_age(),ge.get_location())                                    

# class Parent_class:
#     def __init__(self,name):
#         self.name=name
#     def get_Name(self):
#         return self.name
# class Child(Parent_class):
#     def __init__(self,name,age):
#         Parent_class.__init__(self,name)
#         self.age=age
#     def get_age(self):
#         return self.age
# class Grand_Child(Child):
#     def __init__(self,name,age,location):
#         Child.__init__(self,name,age)
#         self.location=location 
#     def get_Location(self):
#         return self.location
# Obj=Grand_Child("ravikanth",89,"Chittapur")
# print(Obj.get_Name(),Obj.get_age(),Obj.get_Location())                               

# class Parent_class:
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
# class Child_class(Parent_class):
#     def __init__(self,name,age):
#         Parent_class.__init__(self,name)
#         self.age=age
#     def get_Age(self):
#         return self.age
# class GrandChild_class(Child_class):
#     def __init__(self,name,age,location):
#         Child_class.__init__(self,name,age)
#         self.location=location
#     def get_Location(self):
#         return self.location
# Obj=GrandChild_class("Ravikanth",27,"Chittapur")
# print(Obj.get_name(),Obj.get_Age(),Obj.get_Location())                                    

# class Parent_class:
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
# class Child_class(Parent_class):
#     def __init__(self,name,age):
#         Parent_class.__init__(self,name)
#         self.age=age
#     def get_age(self):
#         return self.age
# class GrandChild_class(Child_class):
#     def __init__(self,name,age,location):
#         Child_class.__init__(self,name,age)
#         self.location=location
#     def get_Location(self):
#         return self.location
# Obj1=GrandChild_class("RaviKanth",77,"Chittapur")
# print(Obj1.get_name(),Obj1.get_age(),Obj1.get_Location()) 
# Obj2=GrandChild_class("ShaShiKanth",23,"Hyderabad")
# print(Obj2.get_name(),Obj2.get_age(),Obj2.get_Location())                   
# obj3=Parent_class("Ravi")
# print(obj3.get_name())
# obj4=Child_class("Ravi",66)
# print(obj4.get_name(),obj4.get_age())

# class XYZ:
#     def __init__(self):
#         print("Hey.. I have been Initiliazed :",XYZ)
#     def sub_xyz(self,b):
#         print("Printing from class xyz:",b)
# class XYZ1(XYZ):
#     def __init__(self):
#         print(" I am Initiliazed XYZ1") 
#         super().__init__()
# class XYZ2(XYZ1):
#     def __init__(self):
#         print("Hey I am Initialize XYZ2")
#         super().__init__()
#     def sub_xyx2(self,b):
#         print("printing from Class XYZ2")
#         super().__init__()
# if __name__=="__main__":
#     Obj=XYZ2()
#     Obj.sub_xyz(10)        

