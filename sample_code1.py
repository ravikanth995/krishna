class Parent_class(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def Employee_details(self):
           return self.id, self.name
    
    def Employee_check(self):
          if self.id>50000:
            return "Is a Valid Employee"
          else:
            return "Is not a Valid Employee"
class Derived_class(Parent_class):
    def end(self):
        pass
Employee1=Parent_class(156281, "Ravikanth")
print(Employee1.Employee_details(), Employee1.Employee_check())
Employee2=Derived_class("RajKumar",27171)
print(Employee2.Employee_details(),Employee2.Employee_check())